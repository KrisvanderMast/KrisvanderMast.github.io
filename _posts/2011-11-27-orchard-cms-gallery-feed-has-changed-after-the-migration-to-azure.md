---
layout: post
title: "Orchard CMS Gallery feed has changed after the migration to Azure"
date: 2011-11-27T13:17:07.126266-05:00
tags: ["Azure", "Orchard"]
author: "adminKris"
guid: "a1ef9c73-615e-4b9e-8dfd-130792dc35c7"
published: true
comments: true
show_on_front: true
last_modified_at: 2011-11-27T13:17:07.126266-05:00
---

Last week [Orchard](/images/ "Orchard CMS"), the new cool CMS system from the Microsoft stables, was migrated to the cloud. More precisely to [Windows Azure](/images/ "Windows Azure"). That’s of course great news as it shows that this puppy is growing up fast as [I stated in my live meeting a couple of weeks ago](/images/MyFirstLiveMeetingIsOnline.aspx "My first live meeting for Microsoft is online").

However with the migration it turns out to be that the default Gallery service url doesn’t function anymore and you get to see something like the following when trying to either install a module or a theme:

[![InstallingAModuleFails](/images/InstallingAModuleFails_thumb.png "InstallingAModuleFails")](/images/InstallingAModuleFails_2.png)

To change the Gallery url go to the Dashboard > Settings > Gallery

Add a new feed and provide the following url: [http://packages.orchardproject.net/FeedService.svc/](/images/ "http://packages.orchardproject.net/FeedService.svc/"). So you’ll end up with the following:

[![ChangeTheGalleryFeedUrl](/images/ChangeTheGalleryFeedUrl_thumb.png "ChangeTheGalleryFeedUrl")](/images/ChangeTheGalleryFeedUrl_2.png)

Now delete the first, original, url (/images/FeedService.svc>).

You’re now back in control to add new modules and themes.

Grz, Kris.
