---
layout: post
title: "Creating a horizontal menu with some simple CSS, a Datalist control and a sitemap in ASP.NET"
date: 2010-11-20T15:20:25.511162-05:00
tags: ["ASP.NET", "CSS", "Datalist", "Sitemap"]
author: "adminKris"
guid: "f1fef1c4-830f-4416-a426-9757c6a9e378"
published: true
comments: true
show_on_front: true
last_modified_at: 2010-11-20T15:20:25.511162-05:00
---

ASP.NET provides developers with some very handy controls like a [Treeview](/images/system.web.ui.webcontrols.treeview.aspx "Treeview control") or a [Menu](/images/system.web.ui.webcontrols.menu.aspx "Menu control") control for displaying data coming from a sitemap file. Though a very common scenario sometimes these are simply too heavy weight to be used and on the ASP.NET forums I simply suggest an alternative by using a simple [DataList](/images/system.web.ui.webcontrols.datalist.aspx "DataList control") control. For future reference to point out on the forums I decided to write this little code snippet:

The sitemap file:

```
</fontxml version="1.0" encoding="utf-8" ?> 
<siteMap xmlns="http://schemas.microsoft.com/AspNet/SiteMap-File-1.0" > 
 <siteMapNode url="" title="" description=""> 
 <siteMapNode url="http://www.microsoft.com" title="Microsoft" description="" /> 
 <siteMapNode url="http://blog.krisvandermast.com" title="Kris' blog" description="" /> 
 siteMapNode> 
siteMap>
```

The markup of a simple ASP.NET webform:

```
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %> 
 
DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
 
<html xmlns="http://www.w3.org/1999/xhtml"> 
<head runat="server"> 
 <title>title> 
 <style type="text/css"> 
 
 li { 
 border-left:2px solid #000; 
 list-style:none; 
 margin-right:10px; 
 padding-left:10px; 
 float:left; 
 } 
 
 style> 
head> 
<body> 
 <form id="form1" runat="server"> 
 <div> 
 <asp:SiteMapDataSource runat="server" ID="smd" ShowStartingNode="false" /> 
 <asp:DataList runat="server" ID="menu" DataSourceID="smd" RepeatDirection="Horizontal" RepeatLayout="Flow"> 
 <HeaderTemplate> 
 <ul> 
 HeaderTemplate> 
 <ItemTemplate> 
 <li> 
 <asp:HyperLink ID="HyperLink1" runat="server" NavigateUrl='<%# Eval("Url") %>' 
 Text='<%# Eval("Title") %>'>asp:HyperLink> 
 li> 
 ItemTemplate> 
 <FooterTemplate> 
 ul> 
 FooterTemplate> 
 asp:DataList> 
 div> 
 form> 
body> 
html>
```

The output:

[![datalist_sitemap_menu](/images/datalist_sitemap_menu_thumb.png "datalist_sitemap_menu")](/images/datalist_sitemap_menu.png)

The benefits of using the DataList control is that it’s versatile, lightweight, easy to program but also that it supports item selection. That Could be quite an asset when a page wants to set the [SelectedIndex](/images/system.web.ui.webcontrols.datalist.selectedindex.aspx) from codebehind to have selection in the menu itself. Note the extra added SelectedItemTemplate and the added class=”selected” in the- element. This will, thanks to the css class, make the background color look red and as such a selected menu item.

```
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %> 
 
<%@ Register Assembly="WebApplication1" Namespace="WebApplication1" TagPrefix="cc1" %> 
DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml"> 
<head runat="server"> 
 <title>title> 
 <style type="text/css"> 
 li { 
 border-left: 2px solid #000; 
 list-style: none; 
 padding-right: 10px; 
 padding-left: 10px; 
 float: left; 
 } 
 
 .selected { 
 background-color:Red; 
 } 
 style> 
head> 
<body> 
 <form id="form1" runat="server"> 
 <div> 
 <asp:SiteMapDataSource runat="server" ID="smd" ShowStartingNode="false" /> 
 <asp:DataList runat="server" ID="menu" DataSourceID="smd" RepeatDirection="Horizontal" 
 RepeatLayout="Flow"> 
 <HeaderTemplate> 
 <ul> 
 HeaderTemplate> 
 <ItemTemplate> 
 <li> 
 <asp:HyperLink ID="HyperLink1" runat="server" NavigateUrl='<%# Eval("Url") %>' 
 Text='<%# Eval("Title") %>'>asp:HyperLink> 
 li> 
 ItemTemplate> 
 <SelectedItemTemplate> 
 <li class="selected"> 
 <asp:HyperLink ID="HyperLink1" runat="server" NavigateUrl='<%# Eval("Url") %>' 
 Text='<%# Eval("Title") %>'>asp:HyperLink> 
 li> 
 SelectedItemTemplate> 
 <FooterTemplate> 
 ul> 
 FooterTemplate> 
 asp:DataList> 
 div> 
 form> 
body> 
html>
```

And in the Page\_Load event:

```
protected void Page_Load(/images/object sender, EventArgs e) 
{ 
 menu.SelectedIndex = 1; 
}
```

This outputs the following:

[![datalist_sitemap_menu2](/images/datalist_sitemap_menu2_thumb.png "datalist_sitemap_menu2")](/images/datalist_sitemap_menu2.png)

Another option, which generates less span elements would be to use a [Repeater](/images/system.web.ui.webcontrols.repeater.aspx "Repeater control") control instead:

```
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %> 
 
<%@ Register assembly="WebApplication1" namespace="WebApplication1" tagprefix="cc1" %> 
 
DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
 
<html xmlns="http://www.w3.org/1999/xhtml"> 
<head runat="server"> 
 <title>title> 
 <style type="text/css"> 
 
 li { 
 border-left:2px solid #000; 
 list-style:none; 
 margin-right:10px; 
 padding-left:10px; 
 float:left; 
 } 
 
 style> 
head> 
<body> 
 <form id="form1" runat="server"> 
 <div> 
 <asp:SiteMapDataSource runat="server" ID="smd" ShowStartingNode="false" /> 
 <div id="menu"> 
 <asp:Repeater runat="server" ID="rpt" DataSourceID="smd"> 
 <HeaderTemplate> 
 <ul> 
 HeaderTemplate> 
 <ItemTemplate> 
 <li> 
 <asp:HyperLink ID="HyperLink1" runat="server" NavigateUrl='<%# Eval("Url") %>' 
 Text='<%# Eval("Title") %>'>asp:HyperLink> 
 li> 
 ItemTemplate> 
 <FooterTemplate> 
 ul> 
 FooterTemplate> 
 asp:Repeater> 
 div> 
 div> 
 form> 
body> 
html>
```

Grz, Kris.
