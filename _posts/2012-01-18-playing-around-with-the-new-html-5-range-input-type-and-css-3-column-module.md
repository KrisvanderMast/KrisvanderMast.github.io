---
layout: post
title: "Playing around with the new HTML 5 range input type and CSS 3 column module"
date: 2012-01-18T07:41:22.705697-05:00
tags: ["CSS3", "HTML5", "range"]
author: "adminKris"
guid: "1c3adb39-ef82-4c62-83a6-f193179858c5"
published: true
comments: true
show_on_front: true
last_modified_at: 2012-01-18T07:45:07.555203-05:00
---

In a [former post](/images/CSS3NewColumnModule.aspx "CSS 3 column module") I already presented the new [CSS 3 column module](/images/CSS3NewColumnModule.aspx "CSS 3 column module") and some funky stuff one can do with it.

However sometimes you want to provide your end users the possibility to decide for themselves how many columns they want to see. The following sample will do just that with the help of some javascript and the new HTML 5 [range input type](/images/Overview.html#range-state-type-range "HTML 5 range input type").

The following CSS is used to style up some range of text from the beginning:

```
#test {
 column-count: 3;
 column-rule:2px solid #000;
 column-gap:80px;
}
```

to style up a div element with id test:

```
### How many columns?



Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla dignissim mattis justo, 
 sit amet volutpat turpis convallis vel. Etiam pulvinar tincidunt diam, sit amet ornare justo
```

Note the type of the input element: **range**. I specified the min and max values so there can be only one column or a maximum of five columns. The onchange event will call the following javascript function which takes care of the behavior part and makes the magic happen:

```
	
```

The meter value gets set to the column-count CSS property. Notice the way it is done in javascript, not via column-count but via the element’s property **style.columnCount**. Make sure that you have the casing right as javascript is a case sensitive language!

I used [Internet Explorer](/images/home "Internet Explorer") 10 on Windows 8 and Opera on Windows 7 to test the feature:

[![IE10PreviewWin8](/images/IE10PreviewWin8_thumb.png "IE10PreviewWin8")](/images/IE10PreviewWin8_2.png)

[![IE10Win8](/images/IE10Win8_thumb.png "IE10Win8")](/images/IE10Win8_2.png)

The second IE10 is the Metro version. Note the number 4 coming over the meter. This shows up when dragging the slider from one value to another and disappears again when you release the slider.

The full code to test this out:

Have fun with this!

Grz, Kris.
