import argparse
from datetime import datetime

def format_tags(tags):
    a = ''
    for s in tags.split():
        a += f'"{s.replace("_", " ")}",'
        
    return a[:-1]

def format_filename(date, title):
    return f'{date}-{title.replace(" ", "-").lower()}.markdown'

def write_frontmatter(args, current_time):
    folder = "_drafts" if args.draft else "_posts"

    f = open(f"./{folder}/{format_filename(args.date, args.title)}", "w")
    f.write("---\n")
    f.write("layout: post\n")
    f.write(f"title: {args.title}\n")
    f.write(f"date: {args.date} {current_time} +0200\n")
    f.write("comments: true\n")
    f.write("published: true\n")
    f.write("categories: [\"post\"]\n")
    f.write(f"tags: [{format_tags(args.tags)}]\n")
    f.write(f"author: {args.author}\n")
    f.write("---\n")
    f.close()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new post')
    parser.add_argument("title", type=str, help="Provide a title")
    parser.add_argument("tags", type=str, help="Provide a comma separated list of tags")
    parser.add_argument("--date", type=str, help="Provide a date in format yyyy-mm-dd", default=datetime.now().strftime("%Y-%M-%d"))
    parser.add_argument("--author", type=str, help="Provide a name for the author of the post", default="Kris van der Mast")
    parser.add_argument("--draft", type=bool, help="Create a draft post", default=False)
    args = parser.parse_args()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    write_frontmatter(args, current_time)
