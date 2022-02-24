---
layout: post
title: "Using the switchstartup extension in Visual Studio"
date: 2022-01-11 09:17:00 +0200
comments: true
published: true
categories: ["post"]
tags: ["visual studio", "switchstartup", "extension"]
author: Kris van der Mast
---
Last week I wrote about [making use of the _Current selection_ setting to quickly have the startup project set][1] when you're having the focus on that particular project.

That's quite handy if you only need to startup only one particular project. But sometimes you need to have multiple running to test something. The solution at my current project contains 72 projects as we speak. Several class libraries, code generators, console ([TopShelf][2]) applications and [ASP.NET Web API][3]'s. As we make use of [NServiceBus][4] a lot in our solutions we like to test with different projects running at the same time. But also to quickly switch between other different publishers or receivers. In the past I went into the properties of the solution, select in the multiple startup projects and had to scroll, find and check the ones I wanted to start. Same again when switching to other applications. Quite a time waster...  

It 



[1]:/post/2022/01/04/current-selection-startup-project-in-visual-studio.html
[2]:http://topshelf-project.com/
[3]:https://dotnet.microsoft.com/en-us/apps/aspnet/apis
[4]:https://www.particular.com/