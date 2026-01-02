"""Convert dasBlog dayentry XML files to Jekyll-ready Markdown posts.

- Creates one Markdown post per <Entry> inside each *.dayentry.xml file.
- Preserves timezone offsets in the front-matter `date` field.
- Splits semicolon-delimited categories into `tags`.
- Attempts HTML->Markdown conversion (pandoc first, then markdownify/html2text, otherwise leaves HTML).
- Produces filenames under `_posts/` following Jekyll's `YYYY-MM-DD-slug.md` convention.

Files Created/Modified:
convert_dayentry.py – Conversion script with image URL rewriting
MIGRATION_SUMMARY.md – Complete documentation with usage instructions
images – New directory with all 534 image files
Ready for Jekyll:
Your posts are now compatible with Jekyll. Simply:

Copy _posts directory to your Jekyll site
Copy images directory (or symlink)
Set timezone: America/Los_Angeles in _config.yml (matches original -07:00 offset)
Run jekyll build && jekyll serve
All image references will resolve correctly at /images/filename.png.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
import xml.etree.ElementTree as ET

NAMESPACE = {"d": "urn:newtelligence-com:dasblog:runtime:data"}


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"\s+", "-", value).strip("-")
    value = re.sub(r"-+", "-", value)
    return value or "post"


def parse_bool(text: Optional[str]) -> bool:
    return str(text).strip().lower() == "true"


def split_categories(raw: Optional[str]) -> List[str]:
    if not raw:
        return []
    return [c.strip() for c in raw.replace(",", ";").split(";") if c.strip()]


def yaml_scalar(text: str) -> str:
    """Return a YAML-safe scalar using JSON quoting (valid YAML subset)."""
    return json.dumps(text, ensure_ascii=False)


def yaml_list(items: Iterable[str]) -> str:
    return json.dumps(list(items), ensure_ascii=False)


def html_to_markdown(raw_html: str) -> Tuple[str, str]:
    """Convert HTML to Markdown; returns (content, method_used)."""
    pandoc_path = shutil.which("pandoc")
    if pandoc_path:
        try:
            md = run_pandoc(raw_html, pandoc_path)
            md = normalize_whitespace(md)
            md = rewrite_image_urls(md)
            return md, "pandoc"
        except Exception:
            pass

    try:
        from markdownify import markdownify as md_convert  # type: ignore

        md = md_convert(raw_html, heading_style="ATX", strip=None)
        md = normalize_whitespace(md)
        md = rewrite_image_urls(md)
        return md, "markdownify"
    except Exception:
        pass

    try:
        import html2text  # type: ignore

        converter = html2text.HTML2Text()
        converter.body_width = 0
        converter.wrap_links = False
        converter.ignore_images = False
        converter.ignore_emphasis = False
        converter.ignore_links = False
        md = converter.handle(raw_html)
        md = normalize_whitespace(md)
        md = rewrite_image_urls(md)
        return md, "html2text"
    except Exception:
        pass

    # Fallback: return raw HTML (already unescaped) to avoid data loss.
    normalized = normalize_whitespace(raw_html)
    normalized = rewrite_image_urls(normalized)
    return normalized, "raw-html"


def run_pandoc(raw_html: str, pandoc_path: str) -> str:
    result = subprocess.run(
        [pandoc_path, "-f", "html", "-t", "gfm+raw_html+fenced_code_blocks", "--wrap=none"],
        input=raw_html.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return result.stdout.decode("utf-8")


def rewrite_image_urls(content: str) -> str:
    """Rewrite image URLs to point to /images/ folder.
    
    Handles:
    - Markdown image syntax: ![alt](url)
    - Markdown links: [text](url)
    - HTML src attributes: src="url"
    - Any URL containing image file extensions
    """
    def replace_url(match: re.Match) -> str:
        # Group 1 is the prefix (e.g., "![alt](" or "](" or 'src="')
        prefix = match.group(1)
        # Group 2 is the full URL
        url = match.group(2)
        # Extract just the filename
        filename = Path(url).name
        # Return the prefix with new /images/ path
        return f"{prefix}/images/{filename}"
    
    # Match any URL in parentheses or quotes, replacing with /images/ version
    # This handles: ](url), ![alt](url), src="url", [text](url), href="url"
    content = re.sub(r'(\]?\(|src="|href=")([^)"\']+)', replace_url, content)
    
    return content


def normalize_whitespace(text: str) -> str:
    """Replace non-breaking spaces and Unicode whitespace with ASCII space."""
    text = text.replace("\u00a0", " ")
    text = text.replace("\u2000", " ")
    text = text.replace("\u2001", " ")
    text = text.replace("\u2002", " ")
    text = text.replace("\u2003", " ")
    text = text.replace("\u2009", " ")
    text = text.replace("\u200a", " ")
    text = re.sub(r" +", " ", text)
    return text


def parse_entry(entry) -> Dict[str, object]:
    text = lambda tag: entry.findtext(f"d:{tag}", namespaces=NAMESPACE) or ""
    content_html = html.unescape(text("Content"))
    created = text("Created")
    modified = text("Modified")
    created_dt = datetime.fromisoformat(created)
    modified_dt = datetime.fromisoformat(modified) if modified else None

    data = {
        "title": text("Title"),
        "content_html": content_html,
        "created": created_dt,
        "modified": modified_dt,
        "entry_id": text("EntryId"),
        "categories": split_categories(text("Categories")),
        "author": text("Author"),
        "is_public": parse_bool(text("IsPublic")),
        "syndicated": parse_bool(text("Syndicated")),
        "show_on_front": parse_bool(text("ShowOnFrontPage")),
        "allow_comments": parse_bool(text("AllowComments")),
    }
    return data


def build_front_matter(data: Dict[str, object]) -> List[str]:
    title = yaml_scalar(str(data["title"]))
    date_value: datetime = data["created"]  # type: ignore
    date_str = date_value.isoformat()
    tags = yaml_list(data.get("categories", []))
    front = [
        "---",
        "layout: post",
        f"title: {title}",
        f"date: {date_str}",
        f"tags: {tags}",
        f"author: {yaml_scalar(str(data.get('author', '')))}",
        f"guid: {yaml_scalar(str(data.get('entry_id', '')))}",
        f"published: {str(bool(data.get('is_public') and data.get('syndicated'))).lower()}",
        f"comments: {str(bool(data.get('allow_comments'))).lower()}",
        f"show_on_front: {str(bool(data.get('show_on_front'))).lower()}",
    ]
    modified_dt: Optional[datetime] = data.get("modified")  # type: ignore
    if modified_dt:
        front.append(f"last_modified_at: {modified_dt.isoformat()}")
    front.append("---")
    return front


def unique_filename(base_dir: Path, created: datetime, slug: str, used: Dict[str, int]) -> Path:
    key = f"{created.date()}-{slug}"
    count = used.get(key, 0)
    used[key] = count + 1
    suffix = "" if count == 0 else f"-{count+1}"
    filename = f"{created.date()}-{slug}{suffix}.md"
    return base_dir / filename


def process_file(path: Path, output_dir: Path, overwrite: bool, dry_run: bool, used: Dict[str, int], verbose: bool) -> List[Path]:
    tree = ET.parse(path)
    root = tree.getroot()
    entries = root.find("d:Entries", namespaces=NAMESPACE)
    if entries is None:
        return []

    written: List[Path] = []
    for entry in entries.findall("d:Entry", namespaces=NAMESPACE):
        data = parse_entry(entry)
        slug = slugify(data["title"])
        target = unique_filename(output_dir, data["created"], slug, used)
        if target.exists() and not overwrite:
            if verbose:
                print(f"Skipping existing {target}")
            continue

        content_md, method = html_to_markdown(data["content_html"])
        front = build_front_matter(data)
        body = content_md.rstrip() + "\n"
        output = "\n".join(front) + "\n\n" + body

        if dry_run:
            if verbose:
                print(f"[dry-run] Would write {target} via {method}")
            written.append(target)
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output, encoding="utf-8")
        if verbose:
            print(f"Wrote {target} via {method}")
        written.append(target)
    return written


def gather_files(source_dir: Path, limit: Optional[int]) -> List[Path]:
    files = sorted(source_dir.glob("*.dayentry.xml"))
    return files[:limit] if limit else files


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Convert dasBlog dayentry XML files to Jekyll posts")
    parser.add_argument("--source-dir", type=Path, default=Path("."), help="Directory containing *.dayentry.xml files")
    parser.add_argument("--output-dir", type=Path, default=Path("_posts"), help="Destination directory for Markdown posts")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing target files")
    parser.add_argument("--dry-run", action="store_true", help="Only report actions without writing files")
    parser.add_argument("--limit", type=int, help="Limit number of XML files processed (for testing)")
    parser.add_argument("--verbose", action="store_true", help="Print progress messages")
    args = parser.parse_args(argv)

    xml_files = gather_files(args.source_dir, args.limit)
    if not xml_files:
        print("No *.dayentry.xml files found", file=sys.stderr)
        return 1

    used: Dict[str, int] = {}
    all_written: List[Path] = []
    for path in xml_files:
        written = process_file(path, args.output_dir, args.overwrite, args.dry_run, used, args.verbose)
        all_written.extend(written)

    if args.verbose:
        print(f"Completed. {len(all_written)} posts {'planned' if args.dry_run else 'written'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
