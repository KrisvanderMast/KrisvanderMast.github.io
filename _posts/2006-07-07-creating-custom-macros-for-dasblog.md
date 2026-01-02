---
layout: post
title: "Creating custom macros for dasBlog"
date: 2006-07-07T11:42:12.400000-07:00
tags: ["dasBlog", "dasBlog|Macros", "Tutorial"]
author: "adminKris"
guid: "c004a971-c437-4234-8c9d-aeca21fdeddd"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-10-23T07:58:03.497625-07:00
---

dasBlog is a decent blogging engine originally created by Clemens Vasters. A nice thing that not many people seem to be aware of is that you can easily extend it by creating custom macros. Such a custom macro isn't anything else than just a class library that you can hook into your copy of dasBlog and use it later on in one of the available templates that make up the website.

I couldn't really find a lot of information about this, so I decided to create my own article about the subject that also puts in the solutions I found. 
Also I would like to show the code that I use in my current installment that's reusable directly for other dasBlog users.

Creation:

So, as I already mentioned, creating macros is just like creating a class library. So lets fire up vs.net, create a new project and in the templates choose Class library like in Figure 1. The name of the project is also important when we will be configuring dasBlog to let it know about the existence of our macros. I chose *MydasBlogMacros* but you can choose your own name of course.

[![](/images/dasBlogMacro_01_th.png)](/images/dasBlogMacro_01.png) 
**Figure 1**: Create a new project based upon the Class Library template.

If you haven't downloaded the code for dasBlog now's a good time to do so. You can download the bits from the official site(/images/1) or you can use the guideline to get the latest bits and pieces(/images/2) like I did.

Now we have to add 3 references in order to be able to create our custom macro. You do this by right clicking in the Solution Explorer of Visual Studio.NET on the References node. Take a look at Figure 2 to choose *System.Web*, and Figure 3 to choose 2 assemblies that are from dasBlog itself. These 2 are *newTelligence.DasBlog.Runtime* and *newTelligence.DasBlog.Web.Core*. The result is shown in Figure 4.

![](/images/dasBlogMacro_02_01.png) 
**Figure 2**: locate and choose System.Web

![](/images/dasBlogMacro_02_02.png) 
**Figure 3**: Navigate to the bin folder of the compiled bits of dasBlog and select the needed assemblies.

![](/images/dasBlogMacro_solexpl.png) 
**Figure 4**: After adding the needed references.

In Figure 4 you can also see that I deleted the default Class1.cs file and added a new class with the name *Macros.cs*. This is the only class we'll need for the moment. Here's the code for the Macros class:

1 using System;

 2 using System.Collections.Generic;

 3 using System.Text;

 4 using System.Web.UI;

 5 using newtelligence.DasBlog.Runtime;

 6 using newtelligence.DasBlog.Web.Core;

 7

 8 namespace MydasBlogMacros

 9 {

 10 public class MyMacros

 11 {

 12 protected SharedBasePage sharedBasePage;

 13 protected Entry currentEntry;

 14

 15 public MyMacros(/images/SharedBasePage page, Entry entry)

 16 {

 17 sharedBasePage = page;

 18 currentEntry = entry;

 19 }

 20

 21 public virtual Control EmailIt(/images/string linkText, string cssStyle)

 22 {

 23 if (/images/this.currentEntry != null)

 24 {

 25 string link = this.currentEntry.Link != null

 26 ? this.currentEntry.Link : Utils.GetPermaLinkUrl(/images/this.currentEntry);

 27

 28 return new LiteralControl(" [+ this.currentEntry.Title +](/images/"mailto:?subject="</SPAN)

 29 "&body=I found this to be a great read: " + link +

 30 ". Hope you like it too.\" class=\"" +

 31 cssStyle + "\">" + linkText + "");

 32 }

 33

 34 return new LiteralControl("");

 35 }

 36

 37 public virtual Control Delicious(/images/string linkText, string cssStyle)

 38 {

 39 if (/images/this.currentEntry != null)

 40 {

 41 string link = this.currentEntry.Link != null

 42 ? this.currentEntry.Link : Utils.GetPermaLinkUrl(/images/this.currentEntry);

 43

 44 return new LiteralControl(" [+ link](/images/"http://del.icio.us/post?url="</SPAN)

 45 + "&title=" + this.currentEntry.Title + "\" class=\"" + cssStyle + "\">"

 46 + linkText + "");

 47 }

 48

 49 return new LiteralControl("");

 50 }

 51

 52 public virtual Control Digg(/images/string linkText, string cssStyle)

 53 {

 54 string link = this.currentEntry.Link != null

 55 ? this.currentEntry.Link : Utils.GetPermaLinkUrl(/images/this.currentEntry);

 56

 57 return new LiteralControl(" [+ link +](/images/"http://www.digg.com/submit?url="</SPAN)

 58 "\" class=\"" + cssStyle + "\">"

 59 + linkText + "");

 60 }

 61

 62 public virtual Control Technorati(/images/string linkText, string cssStyle)

 63 {

 64 if (/images/this.currentEntry != null)

 65 {

 66 string link = this.currentEntry.Link != null

 67 ? this.currentEntry.Link : Utils.GetPermaLinkUrl(/images/this.currentEntry);

 68

 69 return new LiteralControl(" [+](/images/"http://www.technorati.com/search/"</SPAN)

 70 this.currentEntry.Title +

 71 "\" class=\"" + cssStyle + "\">"

 72 + linkText + "");

 73 }

 74

 75 return new LiteralControl("");

 76 }

 77 }

 78 }

Note that the signature in the constructor is required in order to let the macros work! 
Besides the constructor I created 4 methods, which will be the macros eventually, the first one EmailIt is for creating a link with the url of the current item in the body so someone can easily mail it to someone whom (/images/s)he thinks will also be interested in the article. The other 3 are for well known web 2.0 services: del.icio.us, digg and technorati.

The methods/macros take all 2 input parameters: the string to appear in the link and the css style that will go in the class attribute of the rendered tag. Separating content and layout has several benefits: it's easy to update in a single place and an external .css file can be cached on the client.

After compiling the source code, preferably in Release mode, and after that open windows explorer and navigate to where the .dll file is created. By default this will be the place where you created your project and in there the subfolders /bin/Release. Now copy the .dll file to the /bin subfolder of the dasBlog solution (/images/this is the same folder where you got your references from).

Configure dasBlog:

We created our macros assembly, dropped it in the /bin folder of the dasBlog folder, but we still need to configure dasBlog in such a way that it knows of the existance of our macros. This is entirely done in the web.config file that can be found in the root folder of dasBlog. Open it with your favorite IDE and uncomment the following line at the top of the web.config:

<section name="newtelligence.DasBlog.Macros" type="newtelligence.DasBlog.Web.Core.MacroSectionHandler, newtelligence.DasBlog.Web.Core" />

Now navigate to the tag <newtelligence.DasBlog.Macros>, uncomment it and add this line:

<add macro="mymacros" type="MydasBlogMacros.MyMacros, MydasBlogMacros"/>

Remember I told in the previous part that you could name your solution somewhat else, well here that name comes into play. If you take a look at the previous line you can see this combination: type="TypeName, Name of the assembly". TypeName in this case is NameSpace.ClassName. The name in the macro attribute, in this example mymacros will be used when we want to use a specific macro.

Use the macro in your template:

So at this point we created our macros, configured dasBlog that they exist. Now comes the part where we embed, or better use, our macros so they become visible in the what a visitor can see by altering the templates in the themes. dasBlog ships with several themes out of the box and people can switch between them. You can however push visitors to only have one theme available by deleting the rest of the themes. If you don't this you'll need to do the next steps for every theme if you want those themes to also have your macros available.

Navigate to the theme folder of choice. There you'll see several .css files and 3 files that have the extension .blogtemplate. Because the macros will be used for every item, they contain specific information for a specific item, open the itemTemplate.blogtemplate file. Here you can call a macro with the following syntax:

**<%EmailIt("Email it!", "mailLinkStyle")|mymacros%>**.

The call can be easily identified, it's the first macro in our example EmailIt. The method takes 2 parameters. After the method call you see the | followed by the name we provided in the macro attribute when we configured the web.config. I also created a new external .css file where I put the specific styles. After that I imported the newly created file into the base.css file with this statement: @import url("mymacros.css");

Resources:

- (/images/1): [dasBlog download](/images/showfiles.php?group_id=127624). 
- (/images/2): [Compiling the dasBlog source code](/images/RePost+Of+Compiling+The+DasBlog+Source+Code+From+DasBloginfo.aspx). 
- The class FooMacros in the dasBlog total solution. 
- [Creating dasBlog macros](/images/CreatingMacrosForDasBlog.aspx).

Well that's it for this article. I hope you found it interesting and if you create new macros yourself or have questions feel free to use the Comments field to let me know.

Grz, Kris.

[![kick it on DotNetKicks.com](/images/CreatingCustomMacrosForDasBlog.aspx)](/images/CreatingCustomMacrosForDasBlog.aspx)
