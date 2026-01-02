---
layout: post
title: "Book review: ASP.NET 3.5 Content Management System Development"
date: 2009-12-01T12:32:06.069750-08:00
tags: ["Books", "Review"]
author: "adminKris"
guid: "d468bff2-4b6d-4431-b9f6-40171450fd32"
published: true
comments: true
show_on_front: true
last_modified_at: 2009-12-01T12:32:06.069750-08:00
---

Recently I got this book for a review. The book itself is [ASP.NET 3.5 Content Management System Development by Packt publishing](/images/book).

[![1847193617](/images/1847193617_3.jpg "1847193617")](/images/book)

The book’s right for the right kind of people: people who started with ASP.NET, played around with it and now want to learn more of some of the concepts of ASP.NET. This is definitely not a book for developers who’ve been doing some hardcore web development with ASP.NET themselves.

What I liked is the order in which the book’s written. All chapters follow nicely one after another and it shows in each chapter steps to either build on the former or how to refactor the previous code and for what reason.

Chapter 1: a quick and dirty file based CMS system with only one page gets created after how it’s shown how to set up and configuring IIS and ASP.NET.

Chapter 2 is a great refrehser, or introduction, of SQL statements and installing **SQL** Server Express 2005 as a database. What I really liked about this chapter’s something that mostly gets overseen: SQL injection. What its is and what .NET does to prevent it

Chapter 3 takes you through a basic **multilayered architecture** which will be implemented in the small, now database using, application. What I found a bit of a pity was the usage of typed datasets. In a world where one sees Microsoft moving more and more to Linq and Entity Framework this is a bit of a missed chance. On the other hand typed datasets is still used a lot in the industry. And as told before, this is a book for people having gone through beginner tutorials first. Also a good basis for further chapters is made with the new architecture which goes beyond a simple: here’s a page and some controls which connect directly to the database.

Chapter 4 introduces the reader to an important concept: **security**. How to configure sqlmembershipprovider, creating the database, making use of the aspnet\_regsqltool, roles and making use of the login controls.

The next chapter shows how to create an articles module. An introduction to **user controls**, and making use of roles.

Chapter 6 leads the reader into the world of themes, **master pages**, skins and menus. First it’s shown how to add items directly with a wizard to the menu and then a more common approach’s used with **sitemaps**.

Chapter 7 is all about the **fileupload** control, working with files (/images/image gallery) and creating **RSS** for your content management system.

The fore last chapter’s more about finishing touches and adding reporting to the application, nice little additions. Also a couple of tips about SEO are highlighted (/images/using the title and meta tags).

The last chapter goes into further possibilities: upgrading to a real full blown SQL Server edition, how to use base pages in the application and error handling.

What I liked about the book is the way the authors write, it’s technical content but with humor added on top. It’s a kind of book you’ll like to read when you want to get to know as an aspiring developer. The topic about SQL injection was a big plus for this book just to get people more aware about the problems that can arise with it.

Grz, Kris.
