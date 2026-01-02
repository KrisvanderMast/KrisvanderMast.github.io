---
layout: post
title: "Keeping your ASP.NET webform's position on postback"
date: 2007-06-09T11:02:12.025000-07:00
tags: ["ASP.NET", "Scroll position"]
author: "adminKris"
guid: "f87c3ea9-736c-43ce-b060-79959c06780f"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-06-09T12:08:01.806750-07:00
---

I see that question appearing on the ASP.NET forums over and over again so I decided to dedicate a post on the subject. There are, depending on the .NET framework properties available that can help one out:

* ASP.NET 1.x: use [SmartNavigation](/images/system.web.ui.page.smartnavigation.aspx).* ASP.NET 2.0: use [MaintainScrollPositionOnPostBack](/images/system.web.ui.page.maintainscrollpositiononpostback.aspx).* Use an [UpdatePanel control](/images/UpdatePanelOverview.aspx) to asynchronously update parts of a page.

Grz, Kris.
