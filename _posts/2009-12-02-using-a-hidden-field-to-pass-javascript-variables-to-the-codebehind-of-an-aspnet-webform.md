---
layout: post
title: "Using a hidden field to pass javascript variables to the codebehind of an ASP.NET webform"
date: 2009-12-02T12:46:59.335375-08:00
tags: ["ASP.NET", "CDN", "jQuery"]
author: "adminKris"
guid: "8e372fa8-2fcd-4fd1-999d-137a02e40cbc"
published: true
comments: true
show_on_front: true
last_modified_at: 2009-12-02T12:46:59.335375-08:00
---

With a lot of ajax, sometimes too much, being used in modern web applications it usually means that also calculations or data is being kept on the client. That’s all great but sometimes one has to perform a postback to the server. When the browser unloads and all form data’s passed to the server the javascript variables that were living happily in the browser are lost. A possible solution is to use a hidden field to send it back and forth. Some source code explains this scenario better:

Markup:

```
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="passjsdataviahiddenfield.aspx.cs" Inherits="betslap.passjsdataviahiddenfield" %>




 
 
 


 

Fill in your name please:
```

Codebehind:

```
using System;

namespace betslap
{
 public partial class passjsdataviahiddenfield : System.Web.UI.Page
 {
 protected void btnGo_Click(/images/object sender, EventArgs e)
 {
 Literal1.Text = hidden1.Value;
 }
 }
}
```

In the markup I make use of the new CDN (/images/Content Delivery Network) from Microsoft. In the piece of javascript that follows a click event is wired and to the button control. The value of the textbox prefixed with the string Hello is put in a local variable txtValue. Then that variable’s used to fill up the hidden field value attribute. Once the button gets clicked this value passing to the hidden field gets processed and then the postback occurs. There we set in the Click eventhandler, on the server, the text of the literal control to the text of the hidden field, in which we passed our javascript variable. The page gets processed, html is rendered and sent back to the browser. Both the value of the hidden field and the text of the literal are the same right now. This demonstrates the working.

Something else that I touched is this syntax:

```
<%= btnGo.ClientID %>
```

Since ASP.NET generates the ids of the html that gets rendered it can be sometimes something else than you expect. Especially when using master pages and javascript a lot of people get surprised with the, in their eyes, unpredictable behavior as it also generates a lot of prefixes. ASP.NET exposes the [ClientID property](/images/system.web.ui.control.clientid.aspx "ClientID property") on server controls which provides us with the rendered id on the client. With this line we inject that ClientID directly into the code of javascript, which gets rendered to the browser and there the correct id is always available.

To learn more about Microsoft CDN take a look at this page: [http://www.asp.net/ajaxlibrary/CDN.ashx](/images/CDN.ashx "Microsoft CDN").

Grz, Kris.
