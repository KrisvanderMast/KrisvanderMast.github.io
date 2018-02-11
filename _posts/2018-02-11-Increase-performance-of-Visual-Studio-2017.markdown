---
layout: post
title: "Increase performance of Visual Studio 2017"
date: 2018-02-11 11:18:00 +0100
comments: true
published: true
categories: ["post"]
tags: ["Performance", "Visual Studio", "Tips and tricks"]
author: Kris van der Mast
---
Visual Studio 2017 is a great tool and I spend quite a lot of my professional days in it. On its own it's already a great editor but the power is in extensions to add that extra dedicated power to it to make ones life easier and get to production faster. I also like several extensions and usually on a fresh install of Visual Studio I install these extensions before even opening a project, I'm that much attached to them.  

I've been wanting to blog about this one already for some time and finally here goes. When I installed Visual Studio 2017 on my Surface Book and installed the extensions I wanted I started Visual Studio and noticed it taking quite a lot of time before it actually was up and running. Like 27 seconds on a machine with great hardware. I tried starting up the tool with the [/SafeMode switch][1]:

> devenv /SafeMode 

I could directly notice the difference so there had to be something going on with some of the extensions but which one? In former version this would've likely resulted in me trying to turn off or uninstall extensions. In Visual Studio 2017 however it's way simpler nowadays:

![Visual Studio 2017 performance window](/images/visual-studio-2017-performance-window.png)


Long story short: for me it turned out that it wasn't an extension but rather a pane that was reaching out to Azure and taking a long time to respond while halting the rest. I turned it off on startup and found that the startup time became way better and very acceptable. So in case that you're suffering from the same, take a look under:

> Help > Manage Visual Studio Performance

and see where you can squeeze out several seconds.

Kris.

[1]:https://docs.microsoft.com/en-us/visualstudio/ide/reference/safemode-devenv-exe