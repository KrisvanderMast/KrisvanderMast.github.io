---
layout: post
title: "How to setup Orchard CMS on Windows Azure Web Sites with a Windows Azure SQL Database"
date: 2012-07-05T07:35:15.320292-04:00
tags: ["Orchard", "WindowsAzure", "WindowsAzureSQLDatabase", "WindowsAzureWebSites"]
author: "adminKris"
guid: "aaee7d20-cf9e-48cb-967a-7326c198f247"
published: true
comments: true
show_on_front: true
last_modified_at: 2012-07-05T07:40:36.820692-04:00
---

I noticed on Twitter several people asking for this. However if you know the steps it’s pretty easy. So simply follow along and get the Orchard party started.

### Preparation step – Set up a database

Normally one would simply deploy Orchard, make use of the built in SQL CE database and get going. However if you want to scale out, which is very easy in [Windows Azure Web Sites](/images/ "Windows Azure Web Sites"), then it’s nothing more but logical to make use of a dedicated database for all deployed instances to keep your data in sync.

To accomplish this simply navigate to the portal and select from the left side menu the option **SQL DATABASES**. Click on the **CREATE A SQL DATABASE**.

Give it a meaningful name:

[![orchardonazure02](/images/orchardonazure02_thumb.png "orchardonazure02")](/images/orchardonazure02_2.png)

Then provide a login name and a password (/images/make sure to make up a good one):

[![orchardonazure03](/images/orchardonazure03_thumb.png "orchardonazure03")](/images/orchardonazure03_2.png)

After the creation you can take a look at the details of the database and either stay on the first page or go to the **DASHBOARD**. Here you can see the connectionstring which is needed later on so be sure to copy that down or know where you can find it in the portal once you need it:

[![orchardonazure04](/images/orchardonazure04_thumb.png "orchardonazure04")](/images/orchardonazure04_2.png)

Ok, that concludes for the first part, let’s move on to the next one.

### Preparation step – Create the new Web Site

Either make use of the big + sign in the lower left of the portal or click on **CREATE A WEB SITE** from the **WEB SITES** menu item in the portal. Select the **FROM GALLERY** and in there select Orchard CMS:

[![orchardonazure05](/images/orchardonazure05_thumb.png "orchardonazure05")](/images/orchardonazure05_2.png)

[![orchardonazure06](/images/orchardonazure06_thumb.png "orchardonazure06")](/images/orchardonazure06_2.png)

Configure the application you’re about to set up. Give it a unique name and select a region:

[![orchardonazure07](/images/orchardonazure07_thumb.png "orchardonazure07")](/images/orchardonazure07_2.png)

Let it spin and after a while you’ll notice the message that your site has been created. You can look up the web site in the portal:

[![orchardonazure08](/images/orchardonazure08_thumb.png "orchardonazure08")](/images/orchardonazure08_2.png)

### Preparation step – Link the database with the Web Site

Ok, now while in that last screen select **LINKED RESOURCES**. From there on create a new one by clicking on **LINK A RESOURCE**:

[![orchardonazure09](/images/orchardonazure09_thumb.png "orchardonazure09")](/images/orchardonazure09_2.png)

Select for the option **Link an existing resource** and select there for the **SQL Database** option:

[![orchardonazure10](/images/orchardonazure10_thumb.png "orchardonazure10")](/images/orchardonazure10_2.png)

In the next screen select the database which was created in the first preparation step:

[![orchardonazure11](/images/orchardonazure11_thumb.png "orchardonazure11")](/images/orchardonazure11_2.png)

Provide the LOGIN NAME and LOGIN PASSWORD and finish.

### Final step – Run the Web Site

Ok, we made it this far already which is great. Now select in the left hand menu the item **WEB SITES**. In the last column of the overview of your web sites select the url and let a new browser window open:

[![orchardonazure12](/images/orchardonazure12_thumb.png "orchardonazure12")](/images/orchardonazure12_2.png)

This is the oh-so-familiar startup screen of Orchard CMS itself. Fill in the required fields but instead of opting for the standard selected SQL Server Compact, select **Use an existing SQL Server (/images/or SQL Express) database**.

Remember I told you to copy the connection string earlier on? Well, here’s where it’s needed. Fill in the connectionstring and make sure you fill in the right password as well. I chose for the default recipe for Orchard in my case and then clicked the **Finish Setup** button. Let the recipe cook up the Orchard CMS website and you’re in business:

[![orchardonazure13](/images/orchardonazure13_thumb.png "orchardonazure13")](/images/orchardonazure13_2.png)

As you can see, it’s pretty easy to do if you know the steps.

### Checking the database

If you want you can connect to your database server and open the MyOrchardDB database. Be sure however to add the IP address you’re using at this moment in the firewall rules or else you won’t be able to connect to it. The portal will provide a warning and an option to directly add your current IP address to the allowed list which is a nice feature.

As you can see all the needed tables where created when cooking the recipe to be able to run Orchard CMS:

[![orchardonazure14](/images/orchardonazure14_thumb_1.png "orchardonazure14")](/images/orchardonazure14_4.png)

Grz, Kris.
