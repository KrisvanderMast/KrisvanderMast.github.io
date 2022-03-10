---
layout: post
title: Python script to generate a new Jekyll post with front matter
date: 2022-03-08 15:51:15 +0200
comments: true
published: true
categories: ["post"]
tags: ["jekyll","python","front matter"]
author: Kris van der Mast
---
Even though I stopped blogging for a while due to various reasons I tried to pick up the pace again since beginning of this year.  
The old blog was hosted on a shared server by a third party vendor and made use of dasBlog.
That ran on ASP.NET 2.0 since 2006 but was phased out last year.
Since this year I moved over my DNS settings to make use [Github pages][1].  

To make my life easier to generate new posts (I don't run a local setup of [Jekyll][2]) I created a small snippet in [Python][3] that I can make use of to create a new _post_ with some _front matter_. The script goes like:  

```python
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
    f = open(f"./_posts/{format_filename(args.date, args.title)}", "w")
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
    parser.add_argument("date", type=str, help="Provide a date in format yyyy-mm-dd")
    parser.add_argument("title", type=str, help="Provide a title")
    parser.add_argument("tags", type=str, help="Provide a comma separated list of tags")
    parser.add_argument("--author", type=str, help="Provide a name for the author of the post", default="Kris van der Mast")
    args = parser.parse_args()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    write_frontmatter(args, current_time)
```

If you want to run it yourself simply create a new [Python][3] file, I chose `create_post.py`, and copy paste the above code into it. Then run it with the command (for example):

> python .\create_post.py 2022-03-08 "Python script to generate a new Jekyll post with front matter" "jekyll python front_matter"

To get help you can write:

> python .\create_post.py -h

Which will give the following output:

```text
usage: create_post.py [-h] [--author AUTHOR] date title tags

Create a new post

positional arguments:
  date             Provide a date in format yyyy-mm-dd
  title            Provide a title
  tags             Provide a comma separated list of tags

optional arguments:
  -h, --help       show this help message and exit
  --author AUTHOR  Provide a name for the author of the post
```

I used the script to generate this post and running it with the following command:

> python .\create_post.py 2022-03-08 "Python script to generate a new Jekyll post with front matter" "jekyll python front_matter"

generated a file under the __posts_ folder with name `2022-03-08-python-script-to-generate-a-new-jekyll-post-with-front-matter.markdown` with front matter:

```text
---
layout: post
title: Python script to generate a new Jekyll post with front matter
date: 2022-03-08 15:51:15 +0200
comments: true
published: true
categories: ["post"]
tags: ["jekyll","python","front matter"]
author: Kris van der Mast
---
```

If you want to reuse this Python script by all means do so. I placed it under the root of my [Github pages][1] [Krisvandermast.github.io][4] repo to keep it close to my site's source code. I'll make a separate repo in the coming days for these kinds of scripts.

[1]: https://pages.github.com/
[2]: https://jekyllrb.com/
[3]: https://www.python.org/
[4]: https://github.com/KrisvanderMast/KrisvanderMast.github.io
