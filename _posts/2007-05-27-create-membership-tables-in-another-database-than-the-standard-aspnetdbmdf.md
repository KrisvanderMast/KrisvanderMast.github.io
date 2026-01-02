---
layout: post
title: "Create Membership tables in another database than the standard aspnetdb.mdf"
date: 2007-05-27T01:46:38.368000-07:00
tags: ["ASP.NET", "SQL Server"]
author: "adminKris"
guid: "4839905e-e475-4204-9fb4-b5eebe30335f"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-05-27T02:01:36.633625-07:00
---

When you start creating a new ASP.NET 2.0 site with Visual Studio 2005 or Visual Web Developer Express (/images/VWD) and want to start using it you'll notice that a new file in the App\_Data folder gets created besides your own database, namely the aspnetdb.mdf file. This extra database holds all the tables and stored procedures to let Membership, Roles, Profile etc run smoothly.

However a problem arises when you don't want to use that dedicated new database when you want to deploy to your live webserver, certainly not when you use a host that only offers one database and charges you extra for another database. Luckely you can control things more when using the dedicated [aspnet\_regsql tool](/images/ms229862(vs.80).aspx) that ships with the .NET 2.0 framework.

What I'm about to describe in this article is how to use that tool to generate a SQL script that you can use to run on your other database with a tool like SQL Server Management Studio (/images/SSMS). In this example I'll be using the installed *Northwind* database on my *localhost* developer machine.

Just start up a new DOS box by going to **Start | Run** and type in **cmd** followed by enter. In Windows Vista you push the blue windows logo button and in the field with the text *Start Search* you type in cmd followed by ctrl + shift + enter. The reason for that combination is that you must run it under Admin privileges or else the to be generated file doesn't get writed to disk. 
A new DOS box will appear and you just navigate to the following directory/folder:

**Windows\Microsoft.NET\Framework\v2.0.50727\**

If you're not used to using DOS you can navigate to it by typing this in the DOS box: **cd \windows\Microsoft.net\framework\v2.0.50727** followed by enter.

Then you type in this line: **aspnet\_regsql.exe -E -S localhost -d Northwind -A all -sqlexportonly c:\membership.sql** again followed by enter. At the location c:\ a new file gets generated: membership.sql.

[![](/images/aspnet_regsql_admindosbox_thumb%5B7%5D.png)](/images/aspnet_regsql_admindosbox%5B9%5D.png)

The Northwind name in the parameter list is later on used to set the db name in the generated sql file: SET @dbname = N'Northwind'

Once generated you can use/tweak this file to be used in SSMS to get executed and to install everything needed in the database.

Ok, up untill now we focussed on getting everything ready on the database side but we also have to let our ASP.NET 2.0 application know that we're pointing out to another database than the default one. The solution for this is to override the default settings for the LocalSqlServer connectionstring which can be found in the machine.config file.

<add name="LocalSqlServer" 
connectionString="data source=.\SQLEXPRESS;Integrated Security=SSPI; 
AttachDBFilename=|DataDirectory|aspnetdb.mdf;User Instance=true" 
providerName="System.Data.SqlClient" />

To override that you open the web.config file in your application which can be normally found in the root of the application. Go to the element.

<connectionStrings> 
 <remove name="LocalSqlServer"/> 
 <add name="LocalSqlServer" connectionString="The connection string to your 
 (/images/new) database" providerName="System.Data.SqlClient" /> 
connectionStrings>

Notice the second line where you call the **remove statement**. This is needed in order to be able to override the LocalSqlServer connection string!

If you're in need of a little help to get your connection string right there's a dedicated site: <http://www.connectionstrings.com/>.

If you're interested in creating one dedicated database for multiple applications you can also check out Scott Guthrie's post: [Configuring ASP.NET 2.0 Application Services to use SQL Server 2000 or SQL Server 2005](/images/423703.aspx).

Grz, Kris.

Technorati tags: [asp.NET](/images/asp.NET), [aspnetdb.mdf](/images/aspnetdb.mdf), [SQL Server](/images/SQL%20Server), [configuration](/images/configuration), [web.config](/images/web.config)
