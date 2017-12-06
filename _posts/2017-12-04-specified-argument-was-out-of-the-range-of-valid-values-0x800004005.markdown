---
layout: post
title: "Specified argument was out of the range of valid values 0x800004005"
date: 2017-12-04 14:45:03 +0100
comments: true
published: true
categories: ["post"]
tags: ["IIS Express", "Windows 10", "0x800004005"]
author: Kris van der Mast
---
A couple of weeks ago I was going through my preparations and demos about the Microsoft Bot Framework to [talk at SharePoint Saturday in Lisbon][1]. As I didn't use Visual Studio lately on this machine but mostly [Visual Studio Code][2] for some of [my recent talks][3] I was rather surprised to see the following error:  

![Specified argument was out of the range of valid values 0x800004005][4]  

Ouch! No fun to discover that several days before going to go to a conference. After some digging around it turned out to be I wasn't the only one. The culprit apparently was the recent Fall Creator update of Windows 10. The remedy? Uninstall IIS Express and install it again. After that it worked again for me. The steps I took to solve it were:  

1. Open the __Control Panel__ of Windows 10
2. Go to __Add and Remove Programs__
3. Search for __IIS Express__ and remove it
4. Start up the Visual Studio 2017 installer
5. Go to the __Individual Components__ tab
6. Check __IIS Express__ and click the __Modify__ button

The full exception I got:  

<pre>
Server Error in '/' Application.

Specified argument was out of the range of valid values.
Parameter name: site 
Description: An unhandled exception occurred during the execution of the current web request. Please review the stack trace for more information about the error and where it originated in the code. 

Exception Details: System.ArgumentOutOfRangeException: Specified argument was out of the range of valid values.
Parameter name: site

Source Error: 


An unhandled exception was generated during the execution of the current web request. Information regarding the origin and location of the exception can be identified using the exception stack trace below. 
Stack Trace: 



[ArgumentOutOfRangeException: Specified argument was out of the range of valid values.
Parameter name: site]
   System.Web.HttpRuntime.HostingInit(HostingEnvironmentFlags hostingFlags, PolicyLevel policyLevel, Exception appDomainCreationException) +280
[HttpException (0x80004005): Specified argument was out of the range of valid values.
Parameter name: site]
   System.Web.HttpRuntime.FirstRequestInit(HttpContext context) +10042604
   System.Web.HttpRuntime.EnsureFirstRequestInit(HttpContext context) +95
   System.Web.HttpRuntime.ProcessRequestNotificationPrivate(IIS7WorkerRequest wr, HttpContext context) +254

Version Information: Microsoft .NET Framework Version:4.0.30319; ASP.NET Version:4.7.2556.0 

</pre>

[1]:http://www.spsevents.org/city/Lisbon/Lisbon2017/schedule
[2]:https://code.visualstudio.com/
[3]:/talks-presentations.html
[4]:/images/0x800004005.PNG