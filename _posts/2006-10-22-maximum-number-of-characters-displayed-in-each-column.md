---
layout: post
title: "Maximum number of characters displayed in each column"
date: 2006-10-22T06:22:30.075000-07:00
tags: ["SQL Server"]
author: "adminKris"
guid: "5ae20a90-c308-45cb-ad7f-52dec3748976"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-10-22T06:25:50.310125-07:00
---

I was unaware of this at first, which gave me some frowns on my face when I found out the hard way, but results in SQL Server Management studio are truncated to a certain amount of characters. Normally you won't notice this but when a certain line exceeds that amount you'll notice the truncated text. I experienced it while concatenating several columns casted as varchars.

By default the maximum amount of characters is 256 but you can easily edit this setting by going to Tools | Options. There you set a higher number of maximum displayed characters in the right lower corner of the screen when you navigate to Query results |SQL Server | Results to Text (/images/or to Grid):

[![](/images/SQL2005ResultToTextMaximumC_thumb1.png)](/images/SQL2005ResultToTextMaximumC3.png)

Grz, Kris.Recenet

[![kick it on DotNetKicks.com](/images/MaximumNumberOfCharactersDisplayedInEachColumn.aspx)](/images/MaximumNumberOfCharactersDisplayedInEachColumn.aspx)
