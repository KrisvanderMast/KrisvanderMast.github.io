---
layout: post
title: "RouteConfig part for WCF svc files in MVC to avoid the 404 http status code"
date: 2014-01-20T13:52:16.753778-05:00
tags: ["ASP.NET MVC", "MVC", "WCF"]
author: "adminKris"
guid: "4fd9162a-1d4e-4ea4-b05c-1fb0f4f24227"
published: true
comments: true
show_on_front: true
last_modified_at: 2014-01-20T13:52:16.753778-05:00
---

Recently we upgraded to Visual Studio 2013 at my client. This morning my colleague came over and had a small problem. Some of the .svc services gave 404 errors. As I had another solution open of which I knew the in project .svc services simply worked I sat down with him. Some searching on the internet, trying out http activation, reregistering WCF, … it didn’t work out.

The difference between both solutions was that the one I was looking at was Webforms while the other one was MVC4 based. Aha! I used [Nuget](/images/ "Nuget") to include [routedebugger](/images/ "routedebugger Nuget package"). A super handy package for, well, debugging MVC routes. However since the .svc files themselves were put into a /Services subfolder I had to make it up like this:

```
routes.IgnoreRoute("Services/{resource}.svc/{*pathInfo}");
```

Put this at pretty much of the top of all the route configuration so that it gets picked up early.

The funny part was that the .svc was working pretty fine, even the wsdl could get obtained. However when we wanted to make a REST call to a specific method it gave 404 mistakes. Turned out to be that the default {controller}/{action}/{id} that ships with every template caught it. Making a more specific rule near the top of the configuration dealt with it and it all started out working smoothly again.

After testing it locally with IIS Express we also tested it out on Cassini due to the fact that the servers are still not up to IIS 8 at the moment and that also worked out fine.

Grz, Kris.
