---
layout: post
title: "Attaching a .mdf file when you don't have the .ldf file available"
date: 2006-05-29T12:25:24.515000-07:00
tags: ["SQL Server"]
author: "adminKris"
guid: "34778781-d68e-49fe-8b64-52e2ae2f94ac"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-05-31T12:05:33.484375-07:00
---

Hi,

ASP.NET 2.0 is promoted quite heavily by Microsoft and other companies or dedicated sites. What most people seem to love are the starter kits which have several dedicated members that like to extend these starter kits and expose these on the internet. If you would be interested in extending some of the starter kits, or just have one deployed as your own personal website, you can [download them here](/images/default.aspx?tabid=62).

Most of these starter kits ship with a sample database which normally consists of a .mdf and a .ldf file. Not all people have SQL Server 2005 Express edition installed but rather only SQL Server 2005. It's quite easy to attach such an Express database to SQL Server 2005 when you have both files available but as I found out in the past sometimes only the .mdf file is provided which prohibits one to attach the database the normal way.

Luckely there's a special procedure available: [sp\_attach\_single\_file\_db](/images/ts_sp_ae-az_4wrm.asp).

An example on how to use it: 
EXEC sp\_attach\_single\_file\_db @dbname = 'pubs', @physname = 'c:\Program Files\Microsoft SQL Server\MSSQL\Data\pubs.mdf'

The @dbname = and the @physname can be omitted if you like.

Grz, Kris.
