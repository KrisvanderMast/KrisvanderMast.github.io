---
layout: post
title: "Change the language version of a C# project"
date: 2019-02-26 07:48:00 +0200
comments: true
published: true
categories: ["post"]
tags: ["Visual Studio", "C#"]
author: Kris van der Mast
---
The C# team brings out new features in small releases like C# 7.1, 7.2 or 7.3 for example. Now you might notice that when you create a new project that not all of these little additions to the language appear, just like they're not there on your machine yet even though you're 200% sure you got them.  

Well this could be due to the project settings. Know however that you can change them following these simple steps:  

1. right click on the project name in the Solution Explorer pane
2. select the __build__ tab
3. scroll down to the bottom to find the __Advanced...__ button and click it
4. select the appropriate __Language version__ in the dropdownlist according to your preferred C# version

![Advanced settings - Language version](/images/build-advanced-7-1.png)

You can also select to use the latest minor version for your project. Making sure that if you would obtain C# 7.4 if that woul become available your project makes use of that the next time you open it:

![Advanced settings - Language version - default to minor version](/images/build-advanced-latest-minor-version.png)

Kris.