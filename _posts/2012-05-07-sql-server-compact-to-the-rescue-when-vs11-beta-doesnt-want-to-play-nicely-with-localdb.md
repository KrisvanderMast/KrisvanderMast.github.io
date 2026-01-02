---
layout: post
title: "SQL Server Compact to the rescue when VS11 Beta doesn’t want to play nicely with LocalDB"
date: 2012-05-07T15:12:44.444642-04:00
tags: ["Entity Framework", "Nuget", "SQL Server", "SQL Server Compact"]
author: "adminKris"
guid: "0455bebe-c160-4493-b109-5b757e40582c"
published: true
comments: true
show_on_front: true
last_modified_at: 2012-05-07T15:12:44.444642-04:00
---

Today I was trying to run a sample application for VS11 Beta that I found online: [Download Hands-on Lab Source Files](/images/Source.zip "Download Hands-on Lab Source Files"). However when trying to run the pages I encountered the following error:

[![A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible. Verify that the instance name is correct and that SQL Server is configured to allow remote connections. (/images/Instance Specified)](/images/ProviderIncompatibleException_thumb.png "ProviderIncompatibleException")](/images/ProviderIncompatibleException_2.png)

Looking into the inner exception:

[![ANetworkRelatedErrorOccured](/images/ANetworkRelatedErrorOccured_thumb_1.png "ANetworkRelatedErrorOccured")](/images/ANetworkRelatedErrorOccured_4.png)

gave me the following:

**A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible. Verify that the instance name is correct and that SQL Server is configured to allow remote connections. (/images/Instance Specified)**.

Ouch!

Well, what I could’ve done is trying to fiddle around with settings of SQL Server, trying to get it right and working. However I noticed that [Entity Framework](/images/bb399567.aspx "Entity Framework") was being used and in the code I found this little piece:

```
public class ProductsContext : DbContext
{
 public ProductsContext() : base("WebFormsLab-Products")
 {
 }

 public DbSet Categories { get; set; }
 
 public DbSet Products { get; set; }
 
 public DbSet Customers { get; set; }
}
```

Inherits from DbContext? Aha, that’s interesting. Now, let me see if we can get SQL Server Compact into play. Well, we can. There’s a nice [Nuget package](/images/ "Nuget") available:

`PM> Install-Package EntityFramework.SqlServerCompact`

This will update the web.config as well as besides downloading the package. Now running the same page again it shows the information nicely instead of giving that nasty error. Also it generated a new database file in the App\_Data subfolder:

[![sdfcreated](/images/sdfcreated_thumb.png "sdfcreated")](/images/sdfcreated_2.png)

Super!

Conclusion: SQL Server Compact to the rescue together with Entity Framework Code First. It’s easy to integrate via Nuget and it simply works (/images/disclaimer: on this machine).

Grz, Kris.
