---
layout: post
title: "Dealing with the maximum upload size of ASP.NET"
date: 2006-06-02T07:31:52.962000-07:00
tags: ["ASP.NET"]
author: "adminKris"
guid: "9e97d223-d4f3-443a-9034-51aaf77d8555"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-06-02T07:34:25.431216-07:00
---

A lot of sites allow people to upload a file like pictures, word documents, ... or even videos. ASP.NET provides an easy way to do this(/images/1).

What not everyone seems to know that ASP.NET only allows, by default to upload 4Mb of formdata to the server. Endusers can get frustrated when they try to upload their large sized document or video and see, after wasting bandwidth and time, that they don't succeed. This leaves your endusers with a bad taste in their mouth about your application and most likely they won't return or go to the competition.

However, as with many things in ASP.NET, this can be easily adjusted. Open up the web.config file of your current application and check the line, or add it in case it isn't already in the config file, (/images/2). This has an attribute maxRequestLength that you can set. The number represents the amount of kilobytes that the total form can transfer to the server. Setting this to a higher number than the default 4098 allows you, the developer, to let endusers upload larger sized files.

Grz, Kris.

(/images/1): [Uploading Files in ASP.NET 2.0](/images/UploadASP2.asp), [Uploading Files Using the File Field Control](/images/aspnet-fileupload.asp) or [Uploading in ASP.NET](/images/091201-1.shtml) to name a few. 
(/images/2): [Take a look at the documentation](/images/e1f13641.aspx) for other settings that you can make.
