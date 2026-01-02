---
layout: post
title: "Selection in a GridView Control in a different way"
date: 2007-05-28T07:46:12.336750-07:00
tags: ["ASP.NET", "ASP.NET|Grid controls"]
author: "adminKris"
guid: "7966b492-01d7-47eb-90e2-3f784b134601"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-05-28T07:46:12.336750-07:00
---

Normally you have the possibility to choose Enable Selection in the Smart tag of a GridView control. This results in an extra column in front of the GridView with the text Select. But what if you don't want it like that but want to be able to use an image for example to select that row?

Well, a neat solution's to add a TemplateField and in the ItemTemplate place an ImageButton control. Why this one? Because it has a CommandName property available you can use. All you have to do is to set it to the predefined word **Select**.

Here's a small example to show what I mean:

```
<%@ Page Language="C#" %>

DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<script runat="server">

script>

<html xmlns="http://www.w3.org/1999/xhtml" >
<head runat="server">
 <title>Untitled Pagetitle>
head>
<body>
 <form id="form1" runat="server">
 <div>
 <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False" 
 DataSourceID="SqlDataSource1">
 <Columns>
 <asp:CommandField ShowSelectButton="True" />
 <asp:BoundField DataField="LastName" HeaderText="LastName" SortExpression="LastName" />
 <asp:BoundField DataField="FirstName" HeaderText="FirstName" SortExpression="FirstName" />
 <asp:BoundField DataField="Title" HeaderText="Title" SortExpression="Title" />
 <asp:TemplateField>
 <ItemTemplate>
 <asp:ImageButton ID="ImageButton1" CommandName="Select" runat="server" 
 ImageUrl="../App_Themes/Black/Images/bullet-1.gif" />
 ItemTemplate>
 asp:TemplateField>
 Columns>
 <SelectedRowStyle BackColor="Red" />
 asp:GridView>
 <asp:SqlDataSource ID="SqlDataSource1" runat="server" 
 ConnectionString="<%$ ConnectionStrings:NorthwindConnectionString %>"
 SelectCommand="SELECT [LastName], [FirstName], [Title] FROM [Employees]">asp:SqlDataSource>
 div>
 form>
body>
html>
```

Grz, Kris.
