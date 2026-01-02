---
layout: post
title: "Update for the ASP.NET Sprite and Image Optimization Toolkit"
date: 2011-03-03T19:48:00-05:00
tags: ["ASP.NET", "CodePlex", "Optimization", "Sprites", "Toolkit"]
author: "adminKris"
guid: "b995513d-1f3f-460f-9398-cf978e1c9ff7"
published: true
comments: true
show_on_front: true
last_modified_at: 2011-03-04T15:50:41.693002-05:00
---

Last year the [ASP.NET](/images/asp.net) team released a Sprite and Image Optimization Toolkit which allows [ASP.NET](/images/asp.net) web sites to be optimized for higher performance where applicable by merging images together and lowering the number of request the browser must make to serve a page. Microsoft just released a new version of the toolkit today with many enhancements including support for MVC 3 and Web Pages 1. Here is a short list of the updates:

* Updated to support Web Pages 1 and MVC 3 (/images/still support Web Forms as well)
* No module registration required for machines with Web Pages 1 / MVC 3 installed, dropping assembly in BIN just works
* Automatic namespace registration in Web Pages, dropping in BIN automatically registers the namespace
* Fully updated documentation
* Common helper between Web Pages and MVC 3
* Many improvements and bug fixes since the last release

You can grab the new release via:

NuGet: <http://www.nuget.org/Packages/Search?packageType=Packages&searchCategory=All+Categories&searchTerm=sprite>

CodePlex: <http://aspnet.codeplex.com/releases/view/61896>

Grz, Kris.
