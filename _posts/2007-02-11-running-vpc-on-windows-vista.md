---
layout: post
title: "Running VPC on Windows Vista"
date: 2007-02-11T07:29:36.728500-08:00
tags: ["Virtual PC", "Vista"]
author: "adminKris"
guid: "ecc523ab-078e-4d7e-8a5f-2d4e8e2663fc"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-02-11T07:29:36.728500-08:00
---

For a course I'm going to follow, starting tomorrow, I needed VPC to run on my laptop. Unfortunately my old VPC software didn't run but one can obtain the [beta of VPC 2007](/images/default.mspx "VPC 2007"). Just installing that and trying to add an existing vpc image gave this error:

[![](/images/vpcunabletorun_thumb.png)](/images/vpcunabletorun%5B2%5D.png)

Pretty nasty. Apparently this comes thanks to the new UAC that ships with Vista. One can set it off, like Gill Cleeren describes in his blog post: [Windows Vista tips & tricks #3: Disable UAC (/images/User Access Control)](/images/Windows+Vista+Tips+Tricks+3+Disable+UAC+User+Access+Control.aspx). This did the trick but setting UAC off is something that I don't want to do at the moment before I know the consequences.

Another tip I saw gave me what I wanted: [Run programs as administrator in Windows Vista](/images/run-programs-as-administrator-in-windows-vista). I use Vista Enterprise but am unable to see the extra tab Compatibility under the properties and the Run as administrator's also not available to me. However the other tip, typing in the name "virtual pc" and then pressing the combination ctrl + shift + enter. This causes the program to be ran as an administrator.

Grz, Kris.
