---
layout: post
title: "In what order does HttpRequest go through the collections?"
date: 2009-11-17T21:02:00-08:00
tags: [".NET Reflector", "ASP.NET", "HttpRequest", "Indexers"]
author: "adminKris"
guid: "f0efeb51-f21c-4679-9828-41c3a15e7936"
published: true
comments: true
show_on_front: true
last_modified_at: 2009-11-16T13:02:14.369679-08:00
---

I found this question on the [ASP.NET forums](/images/ "ASP.NET forums"). The member asking this question already knew that the collections were Cookies, Form, Servervariables and Querystring but wanted to know the exact order. Well I got curious but instead of making a dedicated test project I opened up [Reflector](/images/ ".NET Reflector"). Looking up the HttpRequest class’ indexer gave me this code:

```
public string this[string key]
{
 get
 {
 string str = this.QueryString[key];
 if (/images/str != null)
 {
 return str;
 }
 str = this.Form[key];
 if (/images/str != null)
 {
 return str;
 }
 HttpCookie cookie = this.Cookies[key];
 if (/images/cookie != null)
 {
 return cookie.Value;
 }
 str = this.ServerVariables[key];
 if (/images/str != null)
 {
 return str;
 }
 return null;
 }
}
```

It’s on the other hand always better to directly call the most specific collection directly. This avoids getting strange things in your code like expecting a key in the Form collection and getting the same key from the QueryString collection which could have a different, or none at all, value than what you expect. Fun debugging sessions follow after that…

Grz, Kris.
