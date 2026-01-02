---
layout: post
title: "Office 2007 MSDN evening chapter"
date: 2006-06-24T10:30:22.075250-07:00
tags: ["Office", "MSDN"]
author: "adminKris"
guid: "99f2a1aa-57ce-45e0-8a13-2ebe5c3990c1"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-06-24T10:30:22.075250-07:00
---

Last thursday I attended a session presented by [Jan Tielens](/images/default.aspx) in Mechelen on the subject of Office 2007. 
The session was dedicated for developers and because I haven't tried it out myself I found the new possibilities of Office 2007 very interesting. Especially the new file formats and the distinction between macro enabled and macro disabled documents are great. I still remember the time that macro virusses became available and the harm they could do to someones computer. Also the files themselves are smaller than in the past because they're, behind the scenes, compressed zip files. So in order to take a look at what's inside you just have to rename the file and add .zip behind the file extension of the document and you can open it with winzip for example. After that you can clearly see that all the data is now inside xml files and there are dedicated subfolders available to hold the embedded data like for example images.

The fact that the data is now xml means that a developer can quite easily manipulate the data, or create documents, with .NET. Especially because the next version will hold extra capabilities to interact with the so called "packages".

Besides the new file formats and what a developer can do with it we also had a demo about how to use the VSTO to create custom task panes or to create custom ribbons.

Well, I hope to get into experimentation on this topic soon because it really looks great to me.

Grz, Kris.
