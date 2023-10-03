---
layout: post
title: Make use of colored braces in Visual Studio
date: 2023-10-03 18:15:03 +0200
comments: true
published: true
categories: ["post"]
tags: ["visual studio"]
author: Kris van der Mast
---
I have always been a fan of extensions that make my life easier. One of those extensions was the [Rainbow braces extension by Mads Kristensen][1]. This extension colors the braces in your code. This makes it easier to see where a block starts and ends. Especially when you have a lot of nested blocks like when writing Linq queries.  

It seems many people liked the extension so Microsoft decided a while ago to integrate it into Visual Studio. The only thing you need to do is enable it.  

You can either enable it by going to `Tools` > `Options` > `Environment` > `Text Editor` and then select `Enable brace pair colorization`. Another way to get to it is by using the keyboard combination <kbd>ctrl</kbd> + <kbd>q</kbd> and then type `brace pair colorization`. It will land you on the same option:  

![Enable brace pair colorization](../images/enable_brace_pair_colorization.png)

Of course you want to see some results so here is a screenshot of the same code with and without brace pair colorization:

Without brace pair colorization:

![without brace pair colorization](../images/colored_braces_disabled.png)

With brace pair colorization:

![with brace pair colorization](../images/colored_braces_enabled.png)

Personally I like the colored braces. It makes it easier to see where a block starts and ends.

[1]: https://marketplace.visualstudio.com/items?itemName=MadsKristensen.RainbowBraces