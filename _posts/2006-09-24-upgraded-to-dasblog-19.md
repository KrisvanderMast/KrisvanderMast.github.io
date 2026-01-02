---
layout: post
title: "Upgraded to dasBlog 1.9"
date: 2006-09-24T00:17:12.210625-07:00
tags: ["CSS", "dasBlog"]
author: "adminKris"
guid: "411d1177-3024-40ec-ad20-256a15ea4ab3"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-09-24T01:27:05.335625-07:00
---

Yesterday evening I [upgraded my blog from 1.8 to 1.9](/images/dasblogce).

The things I like already is the easier way to navigate to the previous or next day in the statistics (/images/admin pages). Also the better way to navigate in the itemview to navigate to the previous or next blog article. It makes it much easier for someone to start reading a blog post and navigate to the follow up blog items. The tagcloud control is something I like a lot. It doesn't have the same advanced use like the tagcloud control of [del.icio.us](/images/KvdM) where you can further select "subtags".

When I downloaded the code and tested it on my laptop I quickly noticed that my IE7 RC1 didn't show the tagcloud correctly. After taking a look at the .css files of the dasBlog theme that I use, I quickly noticed that dasBlog.css contains definitions for the css classes that are used by the tagcloud but they were overridden in the base.css file. Commenting these overrides fixed it for me.

I also made the necessary adjustments to the itemtemplate in order to get my custom macros working. If you're interested in creating custom macros yourself you can check out my article about it: [Creating custom macros for dasBlog](/images/CreatingCustomMacrosForDasBlog.aspx).

Grz, Kris.
