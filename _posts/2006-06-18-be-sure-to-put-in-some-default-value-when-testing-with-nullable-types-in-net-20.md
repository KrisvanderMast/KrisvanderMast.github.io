---
layout: post
title: "Be sure to put in some default value when testing with Nullable types in .NET 2.0"
date: 2006-06-18T05:01:24.817000-07:00
tags: [".NET 2.0"]
author: "adminKris"
guid: "4bb89885-d3bb-4a00-94c6-be3b1a343078"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-07-12T13:23:12.687500-07:00
---

Nullable types in .NET 2.0 are a great asset for many developers. I use them all the time in my current project. However there are some things that you should be aware of. Because they can be filled in or can be null you should perform some extra checks in order to get your code to behave like you would expect it.

I've written some sample code that uses a nullable DateTime *endDate.* In applications this can be used to denote a period, startDate - endDate with the endDate being as such that it will never expire. In .NET 1.x we would've just filled it up with new DateTime(/images/9999, 12, 31);. With nullable types you can just let it be null and check appropriately.

1 <%@ Page Language="C#"%>

 2

 3 DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

 4

 5 <script runat="server">

 6

 7 protected void Page\_Load(/images/object sender, EventArgs e)

 8 {

 9 DateTime startDate = newDateTime(/images/2004, 5, 23);

 10

 11 // Using a nullable DateTime can represent an occurance that doesn't expire.

 12 // In a database, like SQL Server, you can have this field set to NULL.

 13 DateTime? endDate = null;

 14 DateTime toCheck = newDateTime(/images/2006, 6, 13);

 15

 16 // First example: this test will fail because we check

 17 // a normal DateTime against a nullable DateTime without

 18 // replacing it with something to check against when it's null.

 19 // Note however that this code compiles! It's only not working out

 20 // in a functional logic way because it doesn't do what we would expect.

 21 if (/images/startDate <= toCheck && toCheck < endDate)

 22 LabelEndDateNull.Text = true.ToString();

 23 else

 24 LabelEndDateNull.Text = false.ToString();

 25

 26

 27 // Second example: now we're checking, and replacing it with an appropriate

 28 // value in case it's null, so the test will pass as expected.

 29 // The trick here is to use the GetValueOrDefault() method on a Nullable type

 30 // to replace it with a default value in case it's null.

 31 if (/images/startDate <= toCheck && toCheck < endDate.GetValueOrDefault(DateTime.MaxValue))

 32 LabelEndDateNullButWithGetValueOrDefaultUsage.Text = true.ToString();

 33 else

 34 LabelEndDateNullButWithGetValueOrDefaultUsage.Text = false.ToString();

 35

 36 // Third example: this one's exactly the same as the previous, second, example.

 37 // Only here I'm applying the great ?? operator available in C# 2.0.

 38 if (/images/startDate <= toCheck && toCheck < (endDate ?? DateTime.MaxValue))

 39 LabelEndDateNullButWithCheck.Text = true.ToString();

 40 else

 41 LabelEndDateNullButWithCheck.Text = false.ToString();

 42

 43

 44 // Fourth example: fill up the nullable DateTime with some actual value:

 45 endDate = newDateTime(/images/2007, 1, 1);

 46

 47 // We can see, this is easier when done debugging the code, that the enddate

 48 // now has some actual value and the test will pass.

 49 if (/images/startDate <= toCheck && toCheck < (endDate ?? DateTime.MaxValue))

 50 LabelEndDateNotNull.Text = true.ToString();

 51 else

 52 LabelEndDateNotNull.Text = false.ToString();

 53 }

 54

 55 script>

 56

 57 <html xmlns="http://www.w3.org/1999/xhtml">

 58 <head runat="server">

 59 <title>Untitled Pagetitle>

 60 head>

 61 <body>

 62 <form id="form1" runat="server">

 63 <div>

 64 Enddate = null:

 65 <asp:Label ID="LabelEndDateNull" runat="server">asp:Label>

 66 <br/>

 67 <br/>

 68 Enddate = null but with GetValueOrDefault method:

 69 <asp:Label ID="LabelEndDateNullButWithGetValueOrDefaultUsage" runat="server">asp:Label>

 70 <br/>

 71 <br/>

 72 Enddate = null but with ?? check:

 73 <asp:Label ID="LabelEndDateNullButWithCheck" runat="server">asp:Label><br/>

 74 <br/>

 75 EndDate != null:

 76 <asp:Label ID="LabelEndDateNotNull" runat="server">asp:Label>div>

 77 form>

 78 body>

 79 html>

The output of this little code sample is:

Enddate = null: False 
 
Enddate = null but with GetValueOrDefault method: True 
 
Enddate = null but with ?? check: True 
 
EndDate != null: True

Take a look at the comment in the code, or better yet: debug it on your own dev machine, to see the subtle difference between the first and second example. The third example's just the same as the second but uses the ?? operator, the one that I prefer in my code because its shorter. [The ?? operator, or null coalescing operator, is only available in C# 2.0](/images/2hxce09y.aspx "Operators Compared in Different Languages").

Grz, Kris.

[![kick it on DotNetKicks.com](/images/BeSureToPutInSomeDefaultValueWhenTestingWithNullableTypesInNET20.aspx)](/images/BeSureToPutInSomeDefaultValueWhenTestingWithNullableTypesInNET20.aspx)
