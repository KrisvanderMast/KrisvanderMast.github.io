---
layout: post
title: "Setting or looking up keyboard shortcuts in Visual Studio"
date: 2007-04-28T04:44:52.352375-07:00
tags: ["Visual Studio", "Tutorial"]
author: "adminKris"
guid: "bc7f705d-b894-4438-a7a4-7ca53ebffa3f"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-04-28T04:48:28.618000-07:00
---

As a moderator on the ASP.NET I often see a request for a certain keyboard shortcut to do a specific thing. Since I like shortcuts myself and use them very often I wanted to provide a little how to here:

First you go to Tools | Customize and click the button Keyboard...

The following screen appears:

[![](/images/keyboardcustomization_thumb%5B7%5D.png)](/images/keyboardcustomization%5B11%5D.png)

If you want to check out which shortcut corresponds to which command you can point the cursor to the textbox at **1**. There you can type in the keyboard shortcut like ctrl + K, ctrl + D. In the dropdownlist at the bottom you can then see where the shortcut is used at that moment like in the following figure:

[![](/images/keyboardcustomization2_thumb%5B1%5D.png)](/images/keyboardcustomization2%5B3%5D.png)

You can clearly see that the command in the Text editor, that's where you type your code, is the Edit.FormatDocument which outlines your code properly.

The other way around can also be done. If you type into **2** the command you're after, in my example Edit.FormatDocument you get to see which shortcut combination in the dropdownlist right underneath it (/images/Shortcuts for selected command). If you're not satisfied with it you can then, in textbox 1, type in your own shortcut combination and click the Assign button.

If you want to fine grain where a certain keyboard combination is used you can select where to use it in the dropdownlist "Use new shortcut in".

Grz, Kris.

Technorati tags: [Visual Studio 2005](/images/Visual%20Studio%202005), [Keyboard shortcuts](/images/Keyboard%20shortcuts)

[![kick it on DotNetKicks.com](/images/SettingOrLookingUpKeyboardShortcutsInVisualStudio.aspx)](/images/SettingOrLookingUpKeyboardShortcutsInVisualStudio.aspx)
