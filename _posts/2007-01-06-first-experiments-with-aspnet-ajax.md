---
layout: post
title: "First experiments with ASP.NET AJAX"
date: 2007-01-06T10:35:12.281000-08:00
tags: ["ASP.NET|ASP.NET AJAX"]
author: "adminKris"
guid: "e0635c26-60c5-4d24-8684-09c50e09a082"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-01-13T03:12:38.270874-08:00
---

Though I'm already quite familiar with ASP.NET I'm just now starting to experiment with ASP.NET AJAX for real. I did some testing with the early alpha's about a year ago.

After installing the Extensions (/images/RC1) and the December CTP I also downloaded and installed the samples to get a look at how it could work. I started with the **SimpleList** application and after copying the assemblies Microsoft.Web.Preview.dll and System.Web.Extensions.dll I soon found out that the webform 2\_SimpleList\_AutoComplete\_DragandDrop.aspx doesn't really behave that great. So I did some digging around and I soon found out that the web.config wasn't entirely correct. I added the following parts:

23 <profile>

 24 <properties>

 25 <add name="dragOverlayPosition"/>

 26 properties>

 27 profile>

because this part's used by the DragOverlayExtender control in the page of which it's the content of the ProfileProperty attribute. After that was done the page could be opened but after dragging the "Notes" around I got a javascript error. It seemed that the in the web.config was still commented out and that the properties weren't set properly. I uncommented the part and filled in the properties like this in order to get it to work properly:

92 <profileService enabled="true"

 93 readAccessProperties="dragOverlayPosition"

 94 writeAccessProperties="dragOverlayPosition" />

And now the application works like a charm.

Now I hope to find something in ASP.NET AJAX like drag & drop and auto updating of where an element was. Just like the demo of script.aculo.us' shopping cart. Hmm, guess I still have quite some learning to do.

Grz, Kris.

[![kick it on DotNetKicks.com](/images/FirstExperimentsWithASPNETAJAX.aspx)](/images/FirstExperimentsWithASPNETAJAX.aspx)
