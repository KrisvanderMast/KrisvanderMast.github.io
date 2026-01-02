---
layout: post
title: "How to get Intellisense back in standalone javascript files in Visual Studio"
date: 2011-09-01T16:18:55.550917-04:00
tags: ["Intellisense", "Javascript", "jQuery", "Visual Studio 2010"]
author: "adminKris"
guid: "a7ed40c8-5361-4dbe-a4a4-94b80070b661"
published: true
comments: true
show_on_front: true
last_modified_at: 2011-09-01T16:18:55.550917-04:00
---

Visual Studio is a great tool but not all tooling is well known. I see this question still way too often on the [ASP.NET forums](/images/ "ASP.NET forums") so I thought I would blog about it.

### Problem:

You have a nice -vsdoc.js file sitting in your solution explorer and are used to get that great Intellisense kicking in when you work inside a webpage or webform doing some cool ASP.NET coding.

[![scriptsinsolutionexplorer](/images/scriptsinsolutionexplorer_thumb.png "scriptsinsolutionexplorer")](/images/scriptsinsolutionexplorer.png)

**Figure 1**: Solution Explorer showing our –vsdoc.js files

However if you want to follow good habits and make use of best practices and opt for a non obtrusive javascript approach, meaning simply that you put your script in a separate file with .js extension, you find yourself out of luck. Intellisense is gone!

[![nointellisenseforjavascript](/images/nointellisenseforjavascript_thumb.png "nointellisenseforjavascript")](/images/nointellisenseforjavascript.png)

**Figure 2**: No Intellisense when we expect to see some assistance for jQuery

Yikes!

### Solution:

Of course there’s a solution. And luckily for us, a very easy one:

1. Open the .js file
2. In the Solution Explorer pick the right –vsdoc.js file
3. Drag and drop that in the .js file like in figure 3
4. Now try to type $(/images/ again and you’ll see like in figure 4 that Intellisense is back again.
5. Drink a beer and celebrate (this last step isn’t really necessary but can spice up the fun factor)

[![dragdropjsfileonjsfile](/images/dragdropjsfileonjsfile_thumb_1.png "dragdropjsfileonjsfile")](/images/dragdropjsfileonjsfile_4.png)

**Figure 3**: Drag and drop from the Solution Explorer into the opened .js file

[![intellisenseisbackforjavascript](/images/intellisenseisbackforjavascript_thumb.png "intellisenseisbackforjavascript")](/images/intellisenseisbackforjavascript_2.png)

**Figure 4**: Intellisense is way back. Woohoo!

Grz, Kris.
