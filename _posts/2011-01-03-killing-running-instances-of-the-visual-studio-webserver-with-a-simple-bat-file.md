---
layout: post
title: "Killing running instances of the Visual Studio webserver with a simple bat file"
date: 2011-01-03T16:42:53.995217-05:00
tags: ["Cassini", "Technet", "Tools"]
author: "adminKris"
guid: "efe4378d-3402-46cc-9034-1ddfc1b31f30"
published: true
comments: true
show_on_front: true
last_modified_at: 2011-01-03T16:42:53.995217-05:00
---

As (/images/web)developer mainly living inside Visual Studio during the day at work I usually make use of the built in webserver of this IDE, namely [Cassini](/images/HowToRunningTheBuiltInWebserverOfVisualStudio2005Yourself.aspx "Cassini web server"). However when I close the debugging session one or more instances, especially more when I’m inside one of my test projects, keep on running. I don’t like to stop them all one by one so I created a simple file with notepad and saved it as **KillAllRunningCassinis.bat**. For people old enough to remember, .bat files were much used in MS-DOS but still can be used in Windows.

The content of this simple file is:

**taskkill /im webdev.webserver.exe**

Taskkill is a handy tool to instantly kill processes on your Windows machine. To read more about it take a look at the [Technet documentation](/images/bb491009.aspx "Taskkill").

Grz, Kris.
