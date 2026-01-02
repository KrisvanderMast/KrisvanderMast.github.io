---
layout: post
title: "Using Access instead of SQL server for your ASP.NET Application Services"
date: 2007-09-09T13:25:12.528000-07:00
tags: ["ASP.NET", "Provider", "Tutorial"]
author: "adminKris"
guid: "2afd591c-7c04-44a9-b86c-86a624ef9ebb"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-10-13T12:57:06.372440-07:00
---

Standard out of the box ASP.NET 2.0 uses SQL Server Express for the Application Services (/images/Membership, Roles, ...). However sometimes you don't want it to be like that because you don't want to pay extra for SQL Server to your hosting company. In the past you practically had to rewrite your application or at least the Data Access Layer to be able to use an alternative database. Thanks to the [Provider model](/images/Aa336558.aspx) that's being used by ASP.NET 2.0 it's possible to develop an application while another team could create an alternative provider and afterwards use some configuration to let your application make use of this new provider.

So, when you're reading this, it means you're interested in changing your default SQL Server based applications services to Access. First of all make sure that you download the [Sample Access Providers](/images/sampleaccessproviders.vsi) provided by Microsoft. 
This is a .vsi file and you could run it to get installed. But rather then doing that, you simply rename the extension from vsi to zip. That's right, you simply rename it and use a zip utitlity, like the built in zip functionality of Windows to extract the files.

[![accessproviders01](/images/accessproviders01_thumb.png)](/images/accessproviders01.png) 
**Figure 1**: the unpacked Sample Access Providers

These are the files I got after extracting the .zip file. You see there's already a full blown ASPNetDB.mdb file in it that has the needed tables and queries to be able to support the Application Services. Figure 2 shows what's already available. As you can see

[![accessproviders03](/images/accessproviders03_thumb.png)](/images/accessproviders03.png) 
**Figure 2**: Overview of the available tables and queries in the accompanied Access database file.

After extracting the files we still need to compile the source code in order to be able to integrate the providers into our web application. If you have Visual Studio or [Visual C# Express](/images/visualcsharp) installed you open your IDE of choice. You navigate to the menu and click File, Open, Project/Solution. Once the dialog opens you navigate to where you extracted the contents of the zip file. Select the **Access.csproj**, see Figure 1, and click the Open button.

Once opened you can see the following in the solution (/images/Figure 3). Now you just have to build the solution, preferably in Release mode.

[![accessproviders04](/images/accessproviders04_thumb.png)](/images/accessproviders04.png) 
**Figure 3**: solution

Ok, the output of building the solution provides us with an assembly named SampleAccessProviders.dll. To find it back you just need to open a windows explorer and navigate to the place where you extracted the zip file to. There you should see a newly created subfolder called bin and in that one that's called Release. In the Release folder you'll find the built assembly.

Now that we have created the assembly it's time to actually use it. Open your Visual Studio or Visual Web Developer Express and create a new website. In the project you create a new subfolder called **bin**. After creation right click on it and choose *Add existing item...* from the context menu that appears. Navigate to the place where the built assembly is. Add it to the bin folder of the website project. After that repeat the same thing with the access database (/images/ASPNetDB.mdb) file but this time put it in the dedicated folder App\_Data which is one of the predefined ASP.NET 2.0 subfolders.

Open the web.config file of the website project. You'll need to make some adjustments here in order to be able to use it Access provider. When you take a look at figure 1 you'll see that the extracted zip file also contains a web.config. It already contains the needed parts so the only thing required is just to copy paste the needed configuration parts. 
First of all the connectionstring to the access database:

```
 <connectionStrings>
 <add name="AccessFileName" connectionString="~/App_Data/ASPNetDB.mdb" providerName="System.Data.OleDb"/>
 connectionStrings>
```

 Also be sure to change the authentication mode which defaults to Windows. Make it use Forms instead like this:

```
<authentication mode="Forms">
 <forms loginUrl="mylogin.aspx" defaultUrl="Login.aspx"/>
authentication>
```

After that you can simply copy in the providers that you need. In this tutorial I'll only copy in the Membership provider part:

```
<membership defaultProvider="AccessMembershipProvider">
 <providers>
 <clear/>
 <add name="AccessMembershipProvider" 
 type="Samples.AccessProviders.AccessMembershipProvider, SampleAccessProviders" 
 connectionStringName="AccessFileName" 
 enablePasswordRetrieval="false" 
 enablePasswordReset="false" 
 requiresUniqueEmail="false" 
 requiresQuestionAndAnswer="false" 
 minRequiredPasswordLength="1" 
 minRequiredNonalphanumericCharacters="0" 
 applicationName="SampleSite" 
 hashAlgorithmType="SHA1" 
 passwordFormat="Hashed"/>
 providers>
membership>
```

Other provider parts, like the Roles and Profile, are just as easily copied.

Just to see if things are working is quite easy. Just open the ASP.NET Configuration Tool. You do that by navigating to the menu and click Website, ASP.NET Configuration. A browser opens with the tool in place. Click the fourth tab (/images/Provider). Select the second link ("Select a different provider for each feature (/images/advanced)). There you'll see that the access provider is selected (/images/figure 4)

[![accessproviders05](/images/accessproviders05_thumb.png)](/images/accessproviders05.png) 
**Figure 4**: Provider tab in the ASP.NET Configuration Tool

In the membership configuration you notice the tag. This clears all previous settings from a hierarchical higher configuration. If you remove that particlar line you'll see that you get another radiobutton option that lists the default AspNetSqlMembershipProvider. If you would select that option SQL Server's used again.

Grz, Kris.
