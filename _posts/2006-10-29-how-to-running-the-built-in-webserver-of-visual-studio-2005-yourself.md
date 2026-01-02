---
layout: post
title: "How To: Running the built in webserver of Visual Studio 2005 yourself"
date: 2006-10-29T06:05:19.664000-07:00
tags: ["ASP.NET", "Tools", "Cassini", "Webserver"]
author: "adminKris"
guid: "e931a45c-30ab-4d5e-b435-6902f017fc76"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-05-27T08:47:38.977375-07:00
---

The freely available tool WebMatrix, which I used on my old pc to develop ASP.NET pages several years ago, came with a built in webserver, code named Cassini, so a developer could test his/her pages on the localhost.

With the .NET 2.0 framework this localhost only webserver's shipped and if you don't have Visual Studio 2005, or the free [Visual Web Developer Express Edition tool](/images/ "Visual Web Developer Express") (/images/which is the follow up of WebMatrix), you can still execute your pages and view the outcome in a browser.

Here's a little guide on how to proceed:

Create a folder on your hard drive. In this example I created c:\MyASPNETPages\ where my testpage will reside. The testpage itself contains this code:

1 <%@ Page Language="C#" %>

 2

 3 <script runat="server">

 4

 5 protected void Page\_Load(/images/object sender, EventArgs e)

 6 {

 7 Label1.Text = DateTime.Now.ToShortDateString();

 8 }

 9

 10 script>

 11

 12 <html>

 13 <head runat="server">

 14 <title>Test Pagetitle>

 15 head>

 16 <body>

 17 <form id="form1" runat="server">

 18 <div>

 19 <asp:Label ID="Label1" runat="server" Text="Label">asp:Label>

 20 div>

 21 form>

 22 body>

 23 html>

Now start up a DOS box (/images/Start | Run, type in **cmd** followed by enter). Navigate to the folder **C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727**

If you don't know how to do this you can type in the following in the opened DOS box: 
**cd \windows\microsoft.net\framework\v2.0.50727**

After that you can type in the text in bold:

C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727>**webdev.webserver /port:8088 /path: 
"c:\MyASPNETPages" /vpath:"/Test"**

Ok what does this mean?

webdev.webserver is the executable itself with the following arguments: port, path and vpath. Port and vpath are optional parameters. After typing the previous lines in bold in and pressing enter a webserver starts up (/images/Figure 1):

[![](/images/webdev_webserver_thumb.png)](/images/webdev_webserver2.png) 
**Figure 1**: Started up webserver

From Figure 1 we can also see what our url will look like (/images/Test>). 
This demonstrates the purpose of the port and vpath arguments. Port is the port number on which the server will listen. The default is 80 but if you have IIS running, like me, it's better to use another number or they will conflict.

After starting the webserver I can easily navigate to my webpage by typing in the url in the address bar of my browser: <http://localhost:8088/Test/>

[![](/images/webdev_webserver2_thumb.png)](/images/webdev_webserver22.png)

As you would've expected I get to see the current date displayed in my page.

If I ommit the vpath argument it would default to "/", meaning that I can navigate to my pages by just typing in this in the address bar: [http://localhost:8088/test.aspx](/images/test.aspx "http://localhost:8088/test.aspx")

Grz, Kris.
