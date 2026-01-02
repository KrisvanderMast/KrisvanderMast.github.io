---
layout: post
title: "Problems with aspnet_regsql (ASP.NET SQL Server Setup Wizard)"
date: 2007-12-02T06:39:06.153250-08:00
tags: ["Installation", "SQL Server"]
author: "adminKris"
guid: "fc1dfca4-690a-4de7-9e0d-ef68a72112a8"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-12-02T06:39:06.153250-08:00
---

Setting up a new environment sometimes gets you into troubles. On my new laptop I didn't want to install SQL Server Express but only the developer edition of SQL Server 2005. Since I know there's a tool that ships with the .NET framework called aspnet\_regsql, with which you can install the needed database for membership etc, I wanted to create such a database. Running the tool however I got this error message:

*System.Web.HttpException: Unable to connect to SQL Server database. ---> System.Data.SqlClient.SqlException: An error has occurred while establishing a connection to the server. When connecting to SQL Server 2005, this failure may be caused by the fact that under the default settings SQL Server does not allow remote connections. (/images/provider: Named Pipes Provider, error: 40 - Could not open a connection to SQL Server)*

So ok, I set on remote connections for TCP/IP only but still got the same error. Strange, but true. So I searched for the error and [found more information about it](/images/980214.aspx). Apparently the instance name of my database didn't get filled in automatically when using the wizard. Quickly inserting the correct instance name and all worked out like a charm.

[![ASP.NET SQL Server Setup Wizard](/images/ASP.NET%20SQL%20Server%20Setup%20Wizard_thumb.png)](/images/ASP.NET%20SQL%20Server%20Setup%20Wizard_2.png)

Grz, Kris.
