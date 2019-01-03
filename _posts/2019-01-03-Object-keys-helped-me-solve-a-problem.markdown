---
layout: post
title: "Object.keys helped me solve a problem"
date: 2018-11-11 12:14:00 +0200
comments: true
published: true
categories: ["post"]
tags: ["JavaScript", "Debugging"]
author: Kris van der Mast
---
Last week I took a day out of my holiday to help out a colleague. I basically already left the client but didn't want to leave my follow up in the cold.  

There were still some small changes recently that lead to some client templates in the Kendo UI MVC charts I had to change and trying to solve it at first glance was going to be difficult. Simply writing `dataItem` didn't do the trick (basically the result didn't show). Now trying to debug such a third party component could become _interesting_... So I went for an alternative approach and did a search on how to get easily to all the properties of an object in JavaScript without making use of the F12 tools and trying to figure out where Kendo would inject the template code.  

Turned out that there's a easy way to do it with

```javascript
    Object.keys()
```

So I wrote simply in the template part console.log(Object.keys(dataItem)) and got what I was after in the F12 console log :relaxed:.

Apparently this was already around since IE9 and further according to [caniuse](http://kangax.github.io/compat-table/es5/#test-Object.keys).  

For a sample of how it works:

```javascript
const object1 = {
  a: 'somestring',
  b: 42,
  c: false
};

console.log(Object.keys(object1));
// expected output: Array ["a", "b", "c"]
```
Sample code taken from [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys).


Kris.