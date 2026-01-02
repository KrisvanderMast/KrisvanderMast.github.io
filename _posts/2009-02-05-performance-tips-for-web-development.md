---
layout: post
title: "Performance tips for web development"
date: 2009-02-05T02:46:00-08:00
tags: ["Javascript", "Performance"]
author: "adminKris"
guid: "34368bf8-0f61-46f8-aa29-5957c965b598"
published: true
comments: true
show_on_front: true
last_modified_at: 2009-02-07T02:47:01.210875-08:00
---

With all the web 2.0 buzz that started a couple of years ago javascript gets used more and more in modern websites and –applications. Most of the time everyone wants to plug in some cool flashy effect but forgets completely about performance or download size of all that goodness. Also correct placement of certain file types can make your application more performing. I recently found a very interesting article: **[Best Practices for Speeding Up Your Web Site](/images/rules.html)**.

Making css and javascript files external so that they can get cached by the browser is something known to a lot of (/images/web)developers. However placing css as high as possible in the page and the scripts as low as possible is mostly something new. ASP.NET AJAX introduced the scriptmanager control in which one can add **[scriptreferences](/images/system.web.ui.scriptreference.aspx)**. Seen in the light of placing script files at the bottom one can also make benefit of the property **[LoadScriptsBeforeUI](/images/system.web.ui.scriptmanager.loadscriptsbeforeui.aspx)** which got introduced with ASP.NET 3.5. It defaults to true, so the scripts will still render at the top. However I suggest that you don’t just switch it to false that lightly but carefully test everything before going to acceptance/production.

Other interesting articles are **[10 ASP.NET Performance and Scalability Secrets](/images/10ASPNetPerformance.aspx)** and [10 Tips for Writing High-Performance Web Applications](/images/cc163854.aspx).

Grz, Kris.
