---
layout: post
title: "Making use of the tree command in DOS"
date: 2019-03-14 07:48:00 +0200
comments: true
published: true
categories: ["post"]
tags: ["cmd", "dos", "tree"]
author: Kris van der Mast
---
A couple of weeks ago I was playing around with [NServicebus](https://particular.net/nservicebus) on localhost. The nice thing about it is that it'll make use of files in different subfolders if the handling part was turned down so it couldn't receive the messages.

To quickly see what remained in which subfolder I found it easy to make use of the __tree__ command from the good old DOS days. It seems quite some people either forgot or didn't even know about this particular command in the first place hence why I'm creating a blog post about it.

So when opening a CMD box in Windows you can navigate to a particular folder of interest and type in the following command:

> tree

The output of that for the subfolder of this website would be like:

![Tree command](/images/tree.png)

It'll show you exactly that, a tree of all the subfolders. If you also want to see the filenames in those folders you can add the extra parameter like this:

> tree /f

This would generate the following for the same subfolder as above:

![Tree /f command](/images/tree-f.png)

Now if you want to save this to a file for later use, or to search for something specific you can do that via the following command:

> tree /f > treedata.txt

With as output:

![Tree /f command and save to treedata.txt file](/images/tree-f-file.png)

That looks rather odd so if you want to beautify that you can also add the /a parameter like:

> tree /f /a > treedata.txt

And now it becomes

![Tree /f /a command and save to treedata.txt file](/images/tree-f-a-file.png)

Kris.