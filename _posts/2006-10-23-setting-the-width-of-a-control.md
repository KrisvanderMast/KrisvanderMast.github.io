---
layout: post
title: "Setting the Width of a Control"
date: 2006-10-23T03:05:53.560000-07:00
tags: ["ASP.NET", "ASP.NET|Controls", "Tutorial"]
author: "adminKris"
guid: "835b0dfe-7ea2-4228-a4ce-baeeb9cc45c3"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-10-23T03:07:29.997625-07:00
---

Setting the Width property of a control in ASP.NET is mostly done in the properties pane or by declaratively setting it in the markup. However sometimes you want to set it in code. This can be done by using the [Unit structure](/images/system.web.ui.webcontrols.unit.aspx "Unit structure").

I crafted some small example that you can run to play around with the different UnitType enumerations. Possible choises are:

**Cm** Measurement is in centimeters. 
**Em** Measurement is relative to the height of the parent element's font. 
**Ex** Measurement is relative to the height of the lowercase letter x of the parent element's font. 
**Inch** Measurement is in inches. 
**Mm** Measurement is in millimeters. 
**Percentage** Measurement is a percentage relative to the parent element. 
**Pica** Measurement is in picas. A pica represents 12 points. 
**Pixel** Measurement is in pixels. 
**Point** Measurement is in points. A point represents 1/72 of an inch.

The sample provided here loops over the possible unit types and fills up the dropdownlist. The second textbox is used to fill in an amount to set the Width of the first textbox control to. If you don't fill in an amount it automatically defaults to 30.

1 <%@ Page Language="C#" %>

 2

 3 DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

 4

 5 <script runat="server">

 6

 7 protected void Page\_Load(/images/object sender, EventArgs e)

 8 {

 9 if (/images/!Page.IsPostBack)

 10 {

 11 // Set the original width to 300 pixels

 12 TextBox1.Width = new Unit(/images/300);

 13

 14 // Loop over the possible unit types

 15 foreach (/images/string s in Enum.GetNames(typeof(UnitType)))

 16 DropDownListSelectUnitType.Items.Add(/images/Enum.Format(typeof(UnitType), Enum.Parse(/images/typeof(UnitType), s), "G"));

 17 }

 18 }

 19

 20 protected void Button1\_Click(/images/object sender, EventArgs e)

 21 {

 22 // Obtain the chosen width, if it's not filled it default to 30

 23 int width = !String.IsNullOrEmpty(/images/TextBoxSetWidth.Text) ? Convert.ToInt32(/images/TextBoxSetWidth.Text) : 30;

 24

 25 // Obtain the chosen unit type

 26 UnitType type = (/images/UnitType)Enum.Parse(/images/typeof(UnitType), DropDownListSelectUnitType.SelectedItem.Text, true);

 27

 28 // Use the Unit structure to set the width of the textbox

 29 TextBox1.Width = new Unit(/images/width, type);

 30 }

 31 script>

 32

 33 <html xmlns="http://www.w3.org/1999/xhtml" >

 34 <head runat="server">

 35 <title>Untitled Pagetitle>

 36 head>

 37 <body>

 38 <form id="form1" runat="server">

 39 <div>

 40 <asp:TextBox ID="TextBox1" runat="server">asp:TextBox><br />

 41 <br />

 42 <br />

 43 Width: <asp:TextBox ID="TextBoxSetWidth" runat="server" Width="40px">asp:TextBox><br />

 44 Type: <asp:DropDownList ID="DropDownListSelectUnitType" runat="server">

 45 asp:DropDownList><br />

 46 <asp:Button ID="Button1" runat="server" Text="Set Textboxes width" OnClick="Button1\_Click" />

 47 div>

 48 form>

 49 body>

 50 html>

Grz, Kris.
