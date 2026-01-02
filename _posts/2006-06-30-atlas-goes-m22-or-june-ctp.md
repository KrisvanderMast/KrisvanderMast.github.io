---
layout: post
title: "Atlas goes M2.2 or June CTP"
date: 2006-06-30T11:57:28.787000-07:00
tags: ["ASP.NET", "ASP.NET|Atlas"]
author: "adminKris"
guid: "1d4dae9c-99d3-450a-874c-a805b10b4769"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-06-30T12:37:44.833932-07:00
---

Dynamic updatepanels, bugfixes, ...

I just read it on [Nikhil's blog](/images/Entry.aspx?id=134) and downloaded it from the the [Atlas site](/images/default.aspx?tabid=47&subtabid=471).

Details of the new CTP:

UpdatePanel:

* UpdatePanels can be added to a page dynamically throughout the page lifecycle, including UpdatePanels inside templates. UpdatePanels now also work inside WebParts, and WebParts can be inside UpdatePanels.* UpdatePanel will preserve cookies set during an async postback when Response.Redirect() is called. This fixes Login control scenarios where an authorization cookie is set and the user gets redirected to the previous page.

Networking:

* ServiceMethod uses default error handler if none specified.* XsltBridgeTransformer now works with VirtualPathProviders* DBNull.Value now should be serialized as null* ServiceReferences now support optional InlineProxy attribute for generating service proxies in the page rather than through a serviceurl/js script reference.* Fix for scenarios where web service proxy contained the wrong port (/images/webfarms, port forwarding)

Drag and Drop:

* Drag and drop will no longer produce debug output* Interactive HTML elements (/images/input, button, textarea, select, label, anchors with an href) can no longer be dragged directly

Miscellaneous Changes:

* Date.toFormattedString improvements* Client-side data: SaveData fix for strongly-typed DataSets

I for one hope that the RTM version is coming close.

Grz, Kris.
