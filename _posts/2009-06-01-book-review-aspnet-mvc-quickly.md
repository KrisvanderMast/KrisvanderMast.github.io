---
layout: post
title: "Book review: ASP.NET MVC Quickly"
date: 2009-06-01T13:06:19.129134-07:00
tags: ["Books", "Review"]
author: "adminKris"
guid: "bdf41143-546c-4c39-b96d-cd9d9b592052"
published: true
comments: true
show_on_front: true
last_modified_at: 2009-06-01T13:06:19.129134-07:00
---

I recently read the book ASP.NET MVC Quickly from Maarten Balliauw, published by PACKT Publishing. It’s been one of those few books that I read from cover to cover. Not only because the subject interested me but also because it shows in about 190+ pages an introduction to this new technology from Microsoft. It was clear that the person who wrote it knows quite a lot about the subject and that shows in the book. I really appreciated Appendix A and C where Maarten discusses a sample application he created: [CarTrackr](/images/ "CarTrackr ASP.NET MVC sample application on CodePlex").

[![aspnetmvcquickly](/images/aspnetmvcquickly_3.jpg "aspnetmvcquickly")](/images/book "ASP.NET MVC Quickly PACKT publishing")

Chapters 1 & 2 provide some quick introductions as to how the architecture looks like and why you would use it over normal ASP.NET webforms. Provided is a “litmus” test to see whether to go for MVC or Webforms and discusses the advantages of both. Chapter 2 explains what’s in the box when you create a new ASP.NET MVC application with Visual Studio. Also a first small application’s being built with ViewData and strong typed ViewData.

Chapter 3 introduces you to a simple application, shows how to deal with fileuploads in MVC, simple validation and the creation of a custom ModelBinder attribute.

Chapter 4 covers the ASP.NET MVC request life cycle. Yes there’s a life cycle but not similar to the [ASP.NET Page Life Cycle](/images/ASPNET20PageLifeCycle.aspx "ASP.NET Page Life Cycle") most people got to know during the last years. After that it proceeds with a more in depth look at the model and validation on such a model. After that an in depth look at controllers, actionresult types and how to handle unknown controller actions. Master pages and Partial views (/images/.ascx) are covered. Those last are only briefly touched and I found that a bit of a pity as these are important concepts. Especially the lack of nester master pages in this story was something I missed.

Chapter 5 is totally dedicated to routing. A very important concept in the whole ASP.NET MVC technology stack (/images/and ASP.NET Dynamic Data and also possible to use with normal webforms). Also a quick explanation on how to integrate both ASP.NET and ASP.NET MVC together in the same project routing wise.

Chapter 6 shows you an overview on how to customize the framework and to even build a small custom viewengine. Also the making of a custom ActionFilter gets discussed.

Chapter 7 shows how to use the standard membership, session state, … that we all know from webforms in ASP.NET MVC. After all, it’s built on top of normal ASP.NET so they can share a great deal of the standard technology. Also is shown how to integrate both technology stacks in the same project. This can be interesting food for thought when people want to gradually upgrade to MVC. Also a nice trick to build views at compile time. Slowing the process down but can safe time in finding out the hard way that you forgot a ) or something and the whole thing explodes in your face.

The next chapter tells us more about AJAX. I had hoped to see this chapter to be longer but it just gives a quick overview. The fact that both ASP.NET AJAX and jQuery (/images/even some of the ui components) are discussed is a plus. I’m a big fan of the latter myself.

Then chapter 9’s all about testing. Also mocking’s discussed. Since ASP.NET MVC is also considered to be way better than webforms to be tested (/images/TDD and such) this is an interesting chapter.

The last chapter is all about deployment; A lot of resources seem to be forgetting about this but I liked the fact that this book covers it. Also on older versions of IIS than 7.

As already stated above, I liked appendix A and C. They cover an application built with the technology which is downloadable on codeplex. Appendix C provides an overview of very interesting resources about the topic.

Conclusion: it’s a nice book that quickly gets a developer into the terms of ASP.NET MVC, covers quite a lot of ground and touches the interesting parts of the technology. Some parts I would’ve loved to see a bit deepened out, especially the parts about the master pages and partial views as well ajax. On the other hand I read it from cover to cover and that certainly means something.

Grz, Kris.
