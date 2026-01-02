---
layout: post
title: "SQL Azure and Reporting updates and as a bonus databases can be 150 Gb instead of 50"
date: 2011-10-13T16:39:32.104088-04:00
tags: ["Reporting Services", "SQL Azure", "SQL Azure Data Sync"]
author: "adminKris"
guid: "f9989145-65bb-4fc8-8da7-f67a4c88e9a5"
published: true
comments: true
show_on_front: true
last_modified_at: 2011-10-13T16:39:32.104088-04:00
---

Great to see that Azure gets better each time. Today I noticed [an interesting blog post](/images/sql-azure-databases-will-be-expanded-3x-from-50-gb-to-150-gb-and-sql-azure-reporting-amp-sql-azure-data-sync-ctp.aspx?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+AvkashChauhansBlog+%28Avkash+Chauhan%27s+Blog%29) which stated that SQL Azure databases can become 150Gb in size instead of the limitation of 50Gb nowadays.

What I did find cool to find out is the new item in the portal quick navigation links:

[![DataSyncInPortal](/images/DataSyncInPortal_thumb.png "DataSyncInPortal")](/images/DataSyncInPortal.png)

New functionality is always great and I see this one coming in handy to sync between data centers and local SQL Server installations. According to the aforementioned blog post the following will be available for the end of 2011:

* Greater ease of use with new Management Portal:
* The new Management Portal provides a rich graphical interpretation of the databases being synchronized and is used to configure, manage and monitor your sync topology.
* Greater flexibility with enhanced filtering and sync group configuration:
* Filtering: Specify a subset of table columns or specific rows.
* Sync group configuration: Specify conflict resolution as well as sync direction per group member.
* Great access for all users:
* The new CTP is available to all SQL Azure users for trial and does not require a separate registration process.

To see more information about SQL Azure Data Sync:

* [http://social.technet.microsoft.com/wiki/contents/articles/sql-azure-data-sync-overview.aspx](/images/sql-azure-data-sync-overview.aspx "http://social.technet.microsoft.com/wiki/contents/articles/sql-azure-data-sync-overview.aspx")
* [http://social.technet.microsoft.com/wiki/contents/articles/sql-azure-data-sync-faq.aspx](/images/sql-azure-data-sync-faq.aspx "http://social.technet.microsoft.com/wiki/contents/articles/sql-azure-data-sync-faq.aspx")

The management portal of SQL Azure also changed as you can see from the following picture. It’s becoming more and more professional:

[![ManagementOfSqlAzure](/images/ManagementOfSqlAzure_thumb.png "ManagementOfSqlAzure")](/images/ManagementOfSqlAzure.png)

Besides that all there’s some more good news coming: The new SQL Azure Reporting Services CTP. One of my colleagues did an evening session at the company about it before summer. BI is an important thing and having it available in the cloud is just a natural flow.

The new CTP states these nice features:

* Improved availability and performance statistics.
* Ability to self-provision a SQL Azure Reporting server.
* Windows Azure Management Portal updates to easily manage users and reports deployed to SQL Azure Reporting.
* Availability of the service in all Microsoft Windows Azure datacenters around the world.
* Official Microsoft support in this new CTP release.
* Greater access for customers with no separate registration process required to use the new CTP.

To get to know more about SQL Azure Reporting Services be sure to take a look at:

* [http://blogs.msdn.com/b/windowsazure/archive/2011/10/13/announcing-sql-azure-reporting-preview-release.aspx](/images/announcing-sql-azure-reporting-preview-release.aspx "http://blogs.msdn.com/b/windowsazure/archive/2011/10/13/announcing-sql-azure-reporting-preview-release.aspx")
* [http://social.technet.microsoft.com/wiki/contents/articles/sql-azure-reporting-overview.aspx](/images/sql-azure-reporting-overview.aspx "http://social.technet.microsoft.com/wiki/contents/articles/sql-azure-reporting-overview.aspx")

Grz, Kris.
