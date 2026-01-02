---
layout: post
title: "Visual Studio 2010: Add an extra context menu item to the document tab"
date: 2009-11-28T07:46:26.084500-08:00
tags: ["Visual Studio", "Visual Studio 2010"]
author: "adminKris"
guid: "822596f0-78ab-4533-87ac-fc17bd3420d7"
published: true
comments: true
show_on_front: true
last_modified_at: 2009-11-28T07:46:26.084500-08:00
---

I got this question in one of the [new forums over at ASP.NET](/images/1213.aspx "Visual Studio 2010"). I took a bit of time to search and this is the result I came up with:

**Default**:

By default when you right click on the MDI document tab you get this context menu which will look familiar to most people from previous versions of Visual Studio.

[![vs2010_mdi_01](/images/vs2010_mdi_01_thumb_1.png "vs2010_mdi_01")](/images/vs2010_mdi_01_4.png)

**Solution**:

Use the menu and to go **Tools**, **Customize**…

[![vs2010_mdi_02](/images/vs2010_mdi_02_thumb.png "vs2010_mdi_02")](/images/vs2010_mdi_02_2.png)

Then from the new window select the second tab **Commands**. Check the radiobutton **context menu** and from the combobox choose **Other Context Menus | Easy MDI Document Window**:

[![vs2010_mdi_03](/images/vs2010_mdi_03_thumb.png "vs2010_mdi_03")](/images/vs2010_mdi_03_2.png)

Click the **Add Command…** button and from the new window choose on the left **Window** and on the right **Close all documents**.

[![vs2010_mdi_04](/images/vs2010_mdi_04_thumb.png "vs2010_mdi_04")](/images/vs2010_mdi_04_2.png)

Click on the OK and then on the Close button and you’re done. Nice and easy.

**Result**:

Your newly added context menu item for the MDI tab in all its glory:

[![vs2010_mdi_05](/images/vs2010_mdi_05_thumb.png "vs2010_mdi_05")](/images/vs2010_mdi_05_2.png)

Grz, Kris.
