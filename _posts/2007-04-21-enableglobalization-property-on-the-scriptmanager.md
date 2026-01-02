---
layout: post
title: "EnableGlobalization property on the ScriptManager"
date: 2007-04-21T08:29:30.774000-07:00
tags: ["ASP.NET|ASP.NET AJAX"]
author: "adminKris"
guid: "d5cb0d97-2563-46f5-b976-7f2cb7f45905"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-04-30T15:32:57.977375-07:00
---

Last week I needed a calendar control to input dates into a textbox, in Belgian notation, so I decided to give the Calendar extender control in the ASP.NET AJAX Toolkit a go.

I put this line in my web.config: <globalization culture="nl-BE" uiCulture="nl-BE" />

I added a TextBox control and a Calendar extender but it always gave me US notation. So I went out looking for a solution. Searching on the ASP.NET forums quickly answered my question. The ScriptManagers EnableGlobalization property seems not to be set by default. After setting it to true my problem was solved immediately.

This was my little test code:

1 <%@ Page Language="C#" AutoEventWireup="true" CodeFile="culturewithoutsettingscriptmanager.aspx.cs" Inherits="culturewithoutsettingscriptmanager" %>

 2 <%@ Register Assembly="AjaxControlToolkit" Namespace="AjaxControlToolkit" TagPrefix="ajaxToolkit" %>

 3

 4 DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

 5

 6 <html xmlns="http://www.w3.org/1999/xhtml" >

 7 <head runat="server">

 8 <title>Untitled Pagetitle>

 9 head>

 10 <body>

 11 <form id="form1" runat="server">

 12 <div>

 13 <asp:ScriptManager ID="ScriptManager1" runat="server" **EnableScriptGlobalization****="true"**>

 14 asp:ScriptManager>

 15 <asp:TextBox runat="server" ID="TextBoxDate" Width="116px" />

 16 <asp:Button runat="server" ID="ButtonSave" OnClick="ButtonSave\_Click" Text="Save" />

 17 <br />

 18 <asp:Label ID="LabelDate" runat="server">asp:Label>

 19 <ajaxToolkit:CalendarExtender runat="server" ID="Calendar1"

 20 FirstDayOfWeek="Monday"

 21 TargetControlID="TextBoxDate" />

 22 div>

 23 form>

 24 body>

 25 html>

And the CodeFile:

1 using System;

 2 using System.Data;

 3 using System.Configuration;

 4 using System.Collections;

 5 using System.Web;

 6 using System.Web.Security;

 7 using System.Web.UI;

 8 using System.Web.UI.WebControls;

 9 using System.Web.UI.WebControls.WebParts;

 10 using System.Web.UI.HtmlControls;

 11

 12 public partial class culturewithoutsettingscriptmanager : System.Web.UI.Page

 13 {

 14 protected void Page\_Load(/images/object sender, EventArgs e)

 15 {

 16

 17 }

 18 protected void ButtonSave\_Click(/images/object sender, EventArgs e)

 19 {

 20 DateTime dt;

 21 DateTime.TryParse(/images/TextBoxDate.Text.Trim(), out dt);

 22

 23 LabelDate.Text = dt.ToShortDateString();

 24 }

 25 }

Testing it with my birthdate, 13/06/1975, I got the expected result in LabelDate.

Grz, Kris.

[![kick it on DotNetKicks.com](/images/EnableGlobalizationPropertyOnTheScriptManager.aspx)](/images/EnableGlobalizationPropertyOnTheScriptManager.aspx)
