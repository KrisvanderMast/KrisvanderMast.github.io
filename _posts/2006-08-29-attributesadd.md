---
layout: post
title: "Attributes.Add()"
date: 2006-08-29T11:21:02.936000-07:00
tags: ["ASP.NET", "Javascript", "Tutorial"]
author: "adminKris"
guid: "eb46715d-a7a9-467e-8189-85d71ad06ddb"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-10-23T07:49:40.435125-07:00
---

People that use ASP.NET know that it's very easy to use the Properties pane in visual studio to quickly set some properties on a server control. By default already a lot of such properties are made available but sometimes you just want something that just doesn't come out of the box. Luckely the WebControl class also provides the [Attributes property](/images/frlrfsystemwebuiwebcontrolswebcontrolclassattributestopic.asp) which is of type [AttributeCollection](/images/frlrfsystemwebuiattributecollectionclasstopic.asp). You can use the [Add method](/images/frlrfsystemwebuiattributecollectionclasstopic.asp) to add new attributes to your control.

To make it more clear I created a small demo page that I used to answer a question on the [ASP.NET forums](/images/forums.asp.net).

1 <%@ Page Language="C#" %>

 2

 3 DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

 4

 5 <script runat="server">

 6

 7 protected void Page\_Load(/images/object sender, EventArgs e)

 8 {

 9 ListBox1.Attributes.Add("ondblclick", "GetValue();");

 10 }

 11 script>

 12

 13 <html xmlns="http://www.w3.org/1999/xhtml" >

 14 <head runat="server">

 15 <title>Untitled Pagetitle>

 16 <script type="text/ecmascript">

 17 function GetValue()

 18 {

 19 box = document.getElementById('ListBox1');

 20 x = box.options[box.selectedIndex].value;

 21

 22 if(/images/document.all)

 23 document.getElementById('Label1').innerText = x;

 24 else // FireFox doesn't implement the innerText property.

 25 document.getElementById('Label1').textContent = x;

 26 }

 27 script>

 28 head>

 29 <body>

 30 <form id="form1" runat="server">

 31 <div>

 32 <asp:ListBox ID="ListBox1" runat="server">

 33 <asp:ListItem>Oneasp:ListItem>

 34 <asp:ListItem>Twoasp:ListItem>

 35 <asp:ListItem>Threeasp:ListItem>

 36 asp:ListBox>div>

 37 <asp:Label runat="server" ID="Label1" />

 38 form>

 39 body>

 40 html>

On line 9 you can see that I add an attribute. In this case the ondblClick javascript event. This results, once rendered in a browser to have the ability to double click on an item and have the selected value set as being the text of the label control. The javascript function that accomplishes this task is on line 19 - 25.
