---
layout: post
title: "Using VB.NET and C# in the same ASP.NET 2.0 project"
date: 2006-06-24T10:49:25.809625-07:00
tags: ["ASP.NET"]
author: "adminKris"
guid: "ac112d42-b984-4692-9d74-dd7166838737"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-06-24T10:49:25.809625-07:00
---

You know that your collegue has created a class with interesting method that you like to reuse in your ASP.NET 2.0 web project but your project is in C#. Instead of waisting time to rewriting the whole chunk of code that your collegue wrote you can simply reuse the code. The only need is to create a couple of subfolders, putting your classes, C# and VB.NET, in these separate subfolders and put some extra configuration in the web.config file.

So for example you add these subfolders to the App\_Code folder: CSharp and VB.

In the web.config you put these lines in the element:

<system.web>

 <compilation debug="true">

 <codeSubDirectories>

 <add directoryName="CSharp"/>

 <add directoryName="VB"/>

 codeSubDirectories>

 compilation>

 system.web>

Another nice thing about this is that you could also use it to organise your classes somewhat better. For example you can create several subdirectories which hold business classes that belong together and make them known in the element.

Grz, Kris.
