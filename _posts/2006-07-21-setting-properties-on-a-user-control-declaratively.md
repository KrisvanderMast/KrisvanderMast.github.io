---
layout: post
title: "Setting properties on a User Control declaratively"
date: 2006-07-21T11:39:14.865000-07:00
tags: ["ASP.NET", "ASP.NET|User Controls", "Tutorial"]
author: "adminKris"
guid: "783e984c-f19b-45f1-975a-6230dfce1458"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-10-23T07:50:32.403875-07:00
---

Most people that have even limited experience with ASP.NET know that you can set the properties of a server control quite easily in the Properties pane of vs.net. Once done this gets set declaratively in the attributes collection of the control. You can see this quite easily when you take a look at the markup of your webform.

A little less known however is the fact that this also can be done with user controls. You can create a public property on the user control, place it on a webform and set, declaratively, the property in the markup of your webform. 
I did it myself a couple of years ago when I crafted a user control that on a certain webform would show the entire list coming from a database and on another webform it should only let a subset of that list be seen. So using this technique I was able to set which list would be shown, from the webform. Keeping the webform in control of what's shown once it was rendered.

A small example is in place here:

First I have my user control:

1 <%@ Control Language="C#" ClassName="PropertySetDeclaratively" %>

 2

 3 <script runat="server">

 4

 5 public string ShowValue

 6 {

 7 set { Label1.Text = value; }

 8 }

 9

 10 script>

 11

 12 <asp:Label ID="Label1" runat="server" Text="Label">asp:Label>

As you can see, I created a public property ShowValue in which the Text of the Label control, Label1, will be set to the value that's passed to it.

And the webform which hosts the user control:

1 <%@ Page Language="C#" %>

 2

 3 <%@ Register Src="PropertySetDeclaratively.ascx" TagName="PropertySetDeclaratively"

 4 TagPrefix="uc1" %>

 5

 6 DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"

 7 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

 8

 9 <script runat="server">

 10

 11 script>

 12

 13 <html xmlns="http://www.w3.org/1999/xhtml" >

 14 <head runat="server">

 15 <title>Untitled Pagetitle>

 16 head>

 17 <body>

 18 <form id="form1" runat="server">

 19 <div>

 20 <uc1:PropertySetDeclaratively ID="PropertySetDeclaratively1" runat="server" ShowValue="13" />

 21 div>

 22 form>

 23 body>

 24 html>

In the syntax on line 20 you see that the ShowValue, the public property on the user control, is set to 13. Once rendered the Label will be filled up with the passed content. Also be aware that the declaratively set property is filled up even before the OnInit event of the user control gets handled.

As a nice side effect we can also turn off ViewState for the Label control because it gets set automatically on each page call, be it either an initial request or a postback. You turn of Viewstate of a control by setting its EnableViewState property to false.

Grz, Kris.
