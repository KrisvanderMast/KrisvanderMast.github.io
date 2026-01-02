---
layout: post
title: "Node.js Web Application using the Windows Azure Table Service working example"
date: 2012-10-17T13:21:20.415857-04:00
tags: ["node.js", "Sample application", "Windows Azure", "Windows Azure Table Storage"]
author: "adminKris"
guid: "fdb8aac6-28f7-4c26-88c7-f131e4bba44d"
published: true
comments: true
show_on_front: true
last_modified_at: 2012-10-17T13:21:20.415857-04:00
---

Lately I’ve been fiddling around with node.js and like it a lot. Since I also like Windows Azure a lot I decided to try some of the [samples from the site](/images/ "NODE.JS DEVELOPER CENTER").

When I tried out the sample from [Node.js Web Application using the Windows Azure Table Service](/images/ "Node.js Web Application using the Windows Azure Table Service") it turned out that there were some mistakes in the provided sample code. I gave direct feedback to the people at hand but as long as it’s not updated, or is just not up to all the typing, [a working example can be found here](/images/downloads.html "Node.js Windows Azure Table Service sample download"). The only thing to do as an extra, I wrote a readme.txt but I know nobody will read it…, so simply create a new storage account. Then copy over the STORAGE ACCOUNT NAME and the PRIMARY ACCESS KEY (/images/both can be found in the modal window that shows when you select a storage account and hit the *i manage keys* button at the bottom bar) and put these in place of the variables in server.js.

Hint: you can make use of [WebMatrix 2](/images/ "WebMatrix 2") to open the project and run it by hitting F12, after having filled in the needed keys of course. Enjoy!

Grz, Kris.
