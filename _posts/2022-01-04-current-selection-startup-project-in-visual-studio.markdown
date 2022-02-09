---
layout: post
title: "Using the current selected project as startup project in Visual Studio"
date: 2022-01-04 09:17:00 +0200
comments: true
published: true
categories: ["post"]
tags: ["visual studio"]
author: Kris van der Mast
---
A feature in Visual Studio which I noticed already being available in VS 2019 before, likely after an update, is the ability to set a project as startup in an alternative way.  

In the past we only had the following options:

- Single startup project
- Multiple startup projects

Since the update, and it ships out of the box with Visual Studio 2022, we got another setting:  

![Current selection for Startup Project in Visual Studio 2022](/images/visual-studio-current-selection-startup-project.png)

What it does is simple: if you have _focus_ on a file in a specific project that project becomes automatically the startup project. Just hit (`ctrl` +) `F5` and get that project running.  

When I have a file open in Console02 in my solution then by using the above mentioned _Current selection_ setting Console02 automatically gets selected as the startup project:

![Current selection is set to Console02](/images/visual-studio-current-selection-startup-project-console02-selected.png)

Something that happens to me from time to time is that when I'm so focussed on the code and `F12` my way into code which is in a class library, that project then gets the focus and as you can guess: it just became the startup project. And no, that won't start :bowtie:.

I noticed that this _tip_ wasn't as widespread as I thought it would be so here you go dear reader. Enjoy!
