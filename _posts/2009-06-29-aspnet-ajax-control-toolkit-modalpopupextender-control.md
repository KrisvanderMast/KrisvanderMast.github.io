---
layout: post
title: "ASP.NET AJAX Control toolkit Modalpopupextender control"
date: 2009-06-29T14:39:40.381298-07:00
tags: ["AJAX Control Toolkit", "ASP.NET|ASP.NET AJAX", "jQuery", "ModalPopupExtender"]
author: "adminKris"
guid: "0c6d9ebc-a8ab-474a-ac2e-2877afbd1f8e"
published: true
comments: true
show_on_front: true
last_modified_at: 2009-06-29T14:39:40.381298-07:00
---

I’ve seen questions about this control over and over again on the forums and decided to write something about it. The most common questions seem to be these:

**1) How to show the modalpopup from codebehind?**

Quite an easy one. The control itself exposes a Show method. This can be called during a postback for example to show some informative message or to provide a fill in form for an enduser. The following code snippet show how to do it:

```
e Language="C#" AutoEventWireup="true" CodeBehind="ModalpopupShowFromCodeBehind.aspx.cs" Inherits="WebApplication35Tech.ModalPopupTesting.ModalpopupShowFromCodeBehind" %>
<%@ Register TagPrefix="act" Assembly="AjaxControlToolkit" Namespace="AjaxControlToolkit" %>





 Show a modalpopupextender from codebehind
 


 

Some informative message: Hello world!
```

And the codebehind:

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication35Tech.ModalPopupTesting
{
 public partial class ModalpopupShowFromCodeBehind : System.Web.UI.Page
 {
 protected void Page_Load(/images/object sender, EventArgs e)
 {
 
 }

 protected void Button1_Click(/images/object sender, EventArgs e)
 {
 mpe.Show();
 }
 }
}
```

This little sample, once the button is clicked and a postback has occured, will lay a so called overlay over the content of the page and in the middle of the screen will show what’s inside pnlOverlay.
 
Notice that I put the style=”display:none;” in the panel markup. This was done to initially hide the content. Otherwise you get the behavior that the content of the overlay will show on rendering in the browser in the top left corner and then suddenly flashes to the center of the screen which is rather unwanted behavior.

**2) How to show the modalpopup from script?**

This seems to be a bit more tricky. The modalpopup extender control has an ID and most people seem to the think that this should be used in client script to show it. As many have found out this is incorrect. Besides the ID of an extender it also provides a BehaviorID. This is the one that can be used to for example show our modal popup or to set the value of a slider extender (/images/also a part of the ASP.NET Ajax control toolkit).

```
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ModalpopupShowFromClientScriptWithjQuery.aspx.cs" Inherits="WebApplication35Tech.ModalPopupTesting.ModalpopupShowFromClientScriptWithjQuery" %>
<%@ Register TagPrefix="act" Assembly="AjaxControlToolkit" Namespace="AjaxControlToolkit" %>





 Show a modalpopupextender from client script
 


 

Some informative message: Hello world!
```

For this sample I made use of the unobtrusive way of capturing a click event of a button. Here I use ASP.NET Ajax to wire up the click event of the button in the onload event of the page. but I could’ve also written the same with [jQuery](/images/www.jquery.com). Note that I’m then mixing 2 different javascript frameworks/libraries together! That little piece of script looks like this:

```
$(/images/document).ready(/images/function() {
 $('#MyButton').click(/images/function() {
 var bid = $find('mpeBehaviorID');
 bid.show();
 });
});
```

Once the button is clicked the overlay will show itself.

**3) How to reposition the modalpopup?**

As we saw in the previous 2 samples the modalpopup shows itself in the center of the screen. Nice but sometimes you want to place it somewhere different. This can be done by using the setLocation function from ASP.NET Ajax. A sample will make it more clear:

```
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ModalpopupChangeScreenPosition.aspx.cs" Inherits="WebApplication35Tech.ModalPopupTesting.ModalpopupChangeScreenPosition" %>
<%@ Register TagPrefix="act" Assembly="AjaxControlToolkit" Namespace="AjaxControlToolkit" %>





 Reposition a modalpopup
 
 


 

test...
```

Once rendered there’s a link at the top and a button on the bottom of the page. Either one can be clicked and because we wired up the event handlers (/images/with the $addHandler shortcut provided by ASP.NET Ajax) the function showModalPopupViaClient gets called. This once again grabs the BehaviorID, mind the sample in point number 2. Once done it grabs several coordinates with the Sys.UI.DomElement.getLocation function call. Then it uses the x position of the panel that acts as the modalpopup and the y position of the button.

However we notice something strange here. When we click the button on the bottom we expect that the overlay is set to the bottom as well due to the x/y positioning. But when we click the link in the left top corner we would expect that it would center as we didn’t add a handler for that click right? This isn’t the case. The modalpopup becomes visible near the top. How is this done? Well, notice in the markup of the modalpopupextender the attribute Y=”80”. This is what makes it all happen. It’s our default position to show the modalpopup.

Once the popup has appeared we can simply click the button Reposition. The function reposition will get called and the modalpopup will reposition itself to the y position of the paragraph with id=testLocation.

Grz, Kris.
