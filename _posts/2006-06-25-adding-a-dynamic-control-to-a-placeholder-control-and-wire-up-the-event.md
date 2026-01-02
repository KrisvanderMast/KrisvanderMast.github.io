---
layout: post
title: "Adding a dynamic control to a placeholder control and wire up the event."
date: 2006-06-25T06:13:21.575250-07:00
tags: ["ASP.NET", "VB.NET"]
author: "adminKris"
guid: "3a2c3a5f-933a-4d03-8ed6-44ca25f3afa5"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-06-25T06:13:21.575250-07:00
---

Most controls are just drag & dropped on a webform or handcoded by a developer in the source view of the document. Although these controls can display dynamic data, for example coming from a database, the controls on the webform themselves remain static. In some scenario's however you want dynamically added controls. For example if a certain authenticated user views the page you want to show more information, or depending on a certain choice you want to load a Repeater control with data or a DateTime control. In this article I instantiate a RadioButtonList control, add it to a PlaceHolder control and wire up the SelectedIndexChanged event of the RadioButtonList instance. Listing 1 shows the C# version and Listing 2 the VB.NET version. Either version is equivalent and it's quite easy to compare both of the code snippets since both have the same equivalent code on the same line.

Listing 1: C# version:

1 <%@ Page Language="C#" %>

 2

 3 DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

 4

 5 <script runat="server">

 6 protected override void OnInit(/images/EventArgs e)

 7 {

 8 base.OnInit(/images/e);

 9

 10 // Instantiate a RadioButtonList control

 11 RadioButtonList rbl = new RadioButtonList();

 12

 13 rbl.AutoPostBack = true;

 14 rbl.ID = "rblID";

 15

 16 // Wire up the eventhandler

 17 rbl.SelectedIndexChanged += new EventHandler(/images/_SelectedIndexChanged);

 18

 19 // Add the items

 20 rbl.Items.Add(/images/new ListItem("One", "1"));

 21 rbl.Items.Add(/images/new ListItem("Two", "2"));

 22 rbl.Items.Add(/images/new ListItem("Three", "3"));

 23

 24 rbl.DataBind();

 25

 26 PlaceHolder1.Controls.Add(/images/rbl);

 27 }

 28

 29 void rbl\_SelectedIndexChanged(/images/object sender, EventArgs e)

 30 {

 31 // Get the control and cast it to the

 32 // appropriate type. In our case a RadioButtonList.

 33 RadioButtonList c = (/images/RadioButtonList)FindControl("rblID");

 34 Label1.Text = c.SelectedItem.Text;

 35 }

 36 script>

 37

 38 <html xmlns="http://www.w3.org/1999/xhtml" >

 39 <head runat="server">

 40 <title>Untitled Pagetitle>

 41 head>

 42 <body>

 43 <form id="form1" runat="server">

 44 <div>

 45 <asp:PlaceHolder ID="PlaceHolder1" runat="server" /><br />

 46 <asp:Label runat="server" ID="Label1" />

 47 div>

 48 form>

 49 body>

 50 html>

Listing 2: VB.NET version:

1 <%@ Page Language="VB" %>

 2

 3 DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

 4

 5 <script runat="server">

 6

 7 Protected Sub Page\_Init(/images/ByVal sender As Object, ByVal e As System.EventArgs)

 8

 9

 10 ' Instantiate a RadioButtonList control

 11 Dim rbl As New RadioButtonList

 12

 13 rbl.AutoPostBack = True

 14 rbl.ID = "rblID"

 15

 16 ' Wire up the event handler

 17 AddHandler rbl.SelectedIndexChanged, AddressOf rbl\_SelectedIndexChanged

 18

 19 ' Add the items

 20 rbl.Items.Add(/images/New ListItem("One", "1"))

 21 rbl.Items.Add(/images/New ListItem("Two", "2"))

 22 rbl.Items.Add(/images/New ListItem("Three", "3"))

 23

 24 rbl.DataBind()

 25

 26 PlaceHolder1.Controls.Add(/images/rbl)

 27

 28 End Sub

 29

 30 Protected Sub rbl\_SelectedIndexChanged(/images/ByVal sender As Object, ByVal e As EventArgs)

 31

 32 ' Get the control and cast it to the

 33 ' appropriate type. In our case a RadioButtonList.

 34 Dim c As RadioButtonList = DirectCast(/images/FindControl("rblID"), RadioButtonList)

 35 Label1.Text = c.SelectedItem.Text

 36

 37 End Sub

 38

 39 script>

 40

 41 <html xmlns="http://www.w3.org/1999/xhtml">

 42 <head runat="server">

 43 <title>Untitled Pagetitle>

 44 head>

 45 <body>

 46 <form id="form1" runat="server">

 47 <div>

 48 <asp:PlaceHolder ID="PlaceHolder1" runat="server" /><br />

 49 <asp:Label runat="server" ID="Label1" />

 50 div>

 51 form>

 52 body>

 53 html>

On line 11 the RadioButtonList is instantiated. After that it's given an ID and the AutoPostBack property is set to true (/images/line numbers 13 & 14). 
Then we wire up the event that'll be handled when a certain selection is made, remember we set the AutoPostBack property to true so once another choice than the current is made an automatic postback to the server will occur. Note the different syntax for C# and VB.NET to wire event handlers on line 17.

At this moment we already have a RadioButtonList instance, wired up the SelectedIndexChanged event, added 3 items to it and databound these items (/images/Lines 20 to 24) but at this moment it's still not visible to the enduser since it was not already put on the page. ASP.NET provides a dedicated control for this: the PlaceHolder control. You can place this control somewhere on your webform and later on use it to hang dynamic controls to. Another convenient control for this is the Panel control. Adding our RadioButtonList to the PlaceHolder control is done on line 26.

We can now render our webform in a browser and upon checking a radiobutton in the list an automatic postback occurs, goes through the code of adding the RadioButtonList again to the page in the Page\_Init/OnInit event again, which is necessary because the page has completely forgotten about the existance of it after the previous rendering. After that the rbl\_SelectedIndexChanged event gets handled. 
In this event we first need to obtain the correct control based upon its ID property with the FindControl method. This method returns an instance of a Control class, which is the base class of all controls in ASP.NET. Once obtained we need to cast it back to the proper class, which is in this case a RadioButtonList. Once cast the Text property of the SelectedItem is used to fill up the Text property of the Label control.

Grz, Kris.
