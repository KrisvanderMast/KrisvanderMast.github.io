---
layout: post
title: "Using jQuery ajax to load a partial view in ASP.NET MVC 2 and then retrieve the input on the server again"
date: 2010-04-19T15:24:15.481924-04:00
tags: ["Ajax", "jQuery", "MVC", "PartialView"]
author: "adminKris"
guid: "b1a264ac-c48f-463e-9f55-db24e2a9b635"
published: true
comments: true
show_on_front: true
last_modified_at: 2010-04-19T16:02:19.449666-04:00
---

jQuery is a powerful javascript library which ships by default when you create an application based on the template of [ASP.NET MVC 2](/images/ "ASP.NET MVC").

[![MVC2LoadPartialViewThroughAjax](/images/MVC2LoadPartialViewThroughAjax_thumb.png "MVC2LoadPartialViewThroughAjax")](/images/MVC2LoadPartialViewThroughAjax_2.png)

Normally one creates a partial view and adds that to a view and renders the whole thing at once. As I was experimenting with some dynamic behavior and jQuery ajax I wanted to try out if I could load a partial view into the already rendered html as another piece of html and then be able to post the whole thing back to the server and capture the the input.

First I created a Model class which looks like this:

```
public class Product
{
 public String Name { get; set; }

 public Decimal Price { get; set; }

 public String Category { get; set; }

 public override string ToString()
 {
 return String.Format("Name: {0}; Price: {1}; Category: {2}", Name, Price, Category);
 }
}
```

Then the controller:

```
public class ProductController : Controller
{
 //
 // GET: /Product/

 public ActionResult Index()
 {
 return View();
 }

 public ActionResult Edit()
 {
 Product product = new Product()
 {
 Name = "Crispy crazy",
 Price = 3.17m,
 Category = "Sushi"
 };

 // Bad practice but just to show the animation in the right upper corner...
 Thread.Sleep(/images/3000);

 return PartialView(/images/product);
 }

 [HttpPost]
 public ContentResult Edit(/images/Product product)
 {
 Product p = product;

 return Content(/images/String.Format("Adjusted product: {0}", p.ToString()));
 }
}
```

Note the first Edit actionresult which fills up a dummy Product instance, halts for 3 seconds and then returns a PartialView which is found in the following code snippet:

```
<%@ Control Language="C#" Inherits="System.Web.Mvc.ViewUserControl" %>

 <% using (/images/Html.BeginForm()) {%>
 <%: Html.ValidationSummary(/images/true) %>
 
 
 Fields

<%: Html.LabelFor(/images/model => model.Name) %>



<%: Html.TextBoxFor(/images/model => model.Name) %>
 <%: Html.ValidationMessageFor(/images/model => model.Name) %>



<%: Html.LabelFor(/images/model => model.Price) %>



<%: Html.TextBoxFor(/images/model => model.Price, String.Format("{0:F}", Model.Price)) %>
 <%: Html.ValidationMessageFor(/images/model => model.Price) %>



<%: Html.LabelFor(/images/model => model.Category) %>



<%: Html.TextBoxFor(/images/model => model.Category) %>
 <%: Html.ValidationMessageFor(/images/model => model.Category) %>



 <% } %>
```

The interesting part however is in the Index view where the needed jQuery script is placed which loads the partial view by calling the first Edit actionresult, shows an animation while it has to wait and then puts the rendered html of that partial view inside a div element where originally the button was.

```
<%@ Page Language="C#" Inherits="System.Web.Mvc.ViewPage" %>





 Index
 
 
 



Please wait ![](/images/ajax-loader.gif)
```

The following part shows the div element with id=”wait” while the ajax action is performing.

```
$('#wait')
 .ajaxStart(/images/function () { $(/images/this).show(); })
 .ajaxStop(/images/function () { $(/images/this).hide(); });
```

By default this element is hidden thanks to the following piece of CSS:

```
#wait {
 position:absolute;
 top:0px;
 right:10px;
 width:200px;
 z-index:1000;
 vertical-align:middle;
 text-align:center;
 background: #febf00;
 display:none;
}
```

The loading part is:

```
$.get("/Product/Edit", {},
 function (/images/data) {
 $('#product').html(/images/data);
 },
 "html");
```

This is just a regular jQuery ajax get function call where in the anonymous function the result on success is passed with the name data. The next line uses a selector to find the div element with id product and then uses the html function to inject the retrieved html, from the Edit actionresult method which returns html, into the selected div element.

Here is a small video which shows the working of this code snippet:

Download of this article: [MVC2LoadPartialViewThroughAjax.zip](/images/MVC2LoadPartialViewThroughAjax.zip "Download sample code").

Grz, Kris.
