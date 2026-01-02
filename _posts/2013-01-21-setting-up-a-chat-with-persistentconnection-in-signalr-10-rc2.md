---
layout: post
title: "Setting up a chat with PersistentConnection in SignalR 1.0 rc2"
date: 2013-01-21T16:20:37.610242-05:00
tags: ["SignalR"]
author: "adminKris"
guid: "5cf58903-3ca2-4bb3-832e-c294d8883410"
published: true
comments: true
show_on_front: true
last_modified_at: 2013-01-22T01:28:11.498628-05:00
---

Today I was going through a [video from BUILD 2012 where Damian Edwards and David Fowler are talking about SignalR](/images/3-034 "Building Real-time Web Apps with ASP.NET SignalR"). Normally people tend to make use of the Hub abstraction as it’s pretty easy to set up. In the video the technique of making use of a PersistentConnection class approach is shown and as I wanted to try that one out I found out that the the rc2 version got some [breaking changes](/images/ReleaseNotes.md "SignalR changes") and I had to find a way around it.

If you want to follow along then here are the steps I took:

Create a new web application. I used an empty MVC 4 one. Open the package manager console and get the prerelease version of [SignalR](/images/ "SignalR").

PM> **Install-Package Microsoft.AspNet.SignalR –Pre**

After you let it install everything create a new class and let it inherit from **PersistentConnection**. Override the OnReceived method. That’s right, the async suffix was dropped.

```
1 using System.Threading.Tasks;
 2 using Microsoft.AspNet.SignalR;
 3 
 4 namespace SignalR1rc2PersistentConnectionTest
 5 {
 6 public class ChatConnection : PersistentConnection
 7 {
 8 protected override Task OnReceived(/images/IRequest request, string connectionId, string data)
 9 {
10 return Connection.Broadcast(/images/data);
11 }
12 }
13 }
```

In the global.asax simply write the following line in the global.asax’ Application\_Start method. Be sure that the setting up of the route needs to be done before setting up other routes:

```
1 public class MvcApplication : HttpApplication
 2 {
 3 protected void Application_Start()
 4 {
 5 RouteTable.Routes.MapConnection<ChatConnection>("chat", "/chat");
 6 
 7 AreaRegistration.RegisterAllAreas();
 8 
 9 WebApiConfig.Register(/images/GlobalConfiguration.Configuration);
10 FilterConfig.RegisterGlobalFilters(/images/GlobalFilters.Filters);
11 RouteConfig.RegisterRoutes(/images/RouteTable.Routes);
12 }
13 }
```

If you’re used to passing in something like “chat/{\*operation}” as second parameter for MapConnection as I tried first as well then you’ll see in this rc2 a fat 404 returning. Simply passing in “/chat” works. Funny enough while I was fiddling around with the code it turned out that passing in null, “” or simply “chat” also worked out for me. I like to keep things in sync with client code so I opted in this sample for “/chat” to keep things simple.

Now create a new html file:

```
1 DOCTYPE html>
 2 <html xmlns="http://www.w3.org/1999/xhtml">
 3 <head>
 4 <title>title>
 5 head>
 6 <body>
 7 <input type="text" value="" id="msg" />
 8 <input type="button" value="Send" id="send" />
 9 
10 <ul id="messages">
11 ul>
12 
13 <script src="/images/jquery-1.9.0.js">script>
14 <script src="/images/jquery.signalR-1.0.0-rc2.js">script>
15 <script>
16 
17 $(/images/function () {
18 
19 var conn = $.connection('/chat');
20 
21 conn.received(/images/function (data) {
22 $('#messages').append('
' + data + '');
23 });
24 
25 conn.start().done(/images/function () {
26 $('#send').on('click', function () {
27 var msg = $('#msg').val();
28 conn.send(/images/msg);
29 });
30 });
31 
32 });
33 
34 script>
35 body>
36 html>
```

Besides adding references to both jQuery and the SignalR scripts the interesting part is in the custom script where the connection is set up, received data from the server gets captured and appended to the ul element. After starting the promise in the form of the done function makes sure that there’s no race condition with the click event of the send button.

A screen capture of the websockets going back and forth in the browser says more than enough. I used IIS Express 8 and Chrome 24 and the built in dev tools for this:

[![SignalR captured websockets with Chrome dev tools](/images/SignalR_websockets_captured_thumb.png "SignalR captured websockets with Chrome dev tools")](/images/SignalR_websockets_captured_2.png)

As I spent some time figuring out the differences between former versions and the new rc2 I hope this may be of convenience for future readers.

Grz, Kris.
