---
layout: post
title: "Exporting embedded resources from the .NET framework with .NET Reflector"
date: 2009-06-07T14:55:00-07:00
tags: [".NET Reflector"]
author: "adminKris"
guid: "83ecb901-afe2-43d6-b2a7-6f260fc4ff46"
published: true
comments: true
show_on_front: true
last_modified_at: 2009-06-07T10:38:44.707375-07:00
---

The first time I encountered .NET Reflector was at Techdays Belgium in 2003 during a session. I got interested in this valuable tool and used it ever since for disassembling .NET assemblies to code and take a look at the inner workings. If you haven’t downloaded it already then you can [grab it here](/images/index.htm "Download .NET Reflector").

A little known fact is that one can also extract embedded resources with this marvelous tool. When you simply open .NET reflector like in figure 1 you can navigate in the treeview to System.Web > Resources.

[![reflector01](/images/reflector01_thumb.png "reflector01")](/images/reflector01_2.png) 
**Figure 1**: .NET Reflector assemblies overview

Then scroll down until you find the resource with the name WebUIValidation.js. Right click on it and select **Save As…** like in figure 2:

[![reflector02](/images/reflector02_thumb.png "reflector02")](/images/reflector02_2.png) 
Figure 2: Save the resource.

After this action a Filesavedialog window will open so you can save the resource to disk.

Also be sure to check out this [demo movie](/images/video.htm ".NET Reflector demo movie") from Redgate itself which shows some nice standard features if you’re not used to working with the product.

Grz, Kris.
