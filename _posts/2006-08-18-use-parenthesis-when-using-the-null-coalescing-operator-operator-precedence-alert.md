---
layout: post
title: "Use parenthesis when using the null coalescing operator, operator precedence alert..."
date: 2006-08-18T05:30:17.265125-07:00
tags: [".NET 2.0"]
author: "adminKris"
guid: "34110744-e49c-40f1-a971-c92ffaadbec2"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-08-18T05:41:24.343250-07:00
---

I've written already some articles in the past about the null coalescing operator (/images/1) but recently my colleague found some "strange" behavior when using this operator. First of all the guilty code:

1 using System;

 2 using System.Collections.Generic;

 3 using System.Text;

 4

 5 namespace ConsoleApplicationNullableTypes

 6 {

 7 public class NullCoalescingTestWithinObject

 8 {

 9 static void Main(/images/string[] args)

 10 {

 11 int multiplicator = 5;

 12 int workRegime = 6;

 13

 14 SomeObject so = new SomeObject();

 15 so.Test = 7;

 16

 17 decimal result = (/images/* multiplicator) / workRegime;

 18

 19 Console.WriteLine(/images/result.ToString("N"));

 20

 21 Console.ReadLine();

 22 }

 23 }

 24

 25 internal class SomeObject

 26 {

 27 private decimal? \_test;

 28

 29 public decimal? Test

 30 {

 31 get { return \_test; }

 32 set { \_test = value; }

 33 }

 34 }

 35 }

 The actual behavior for investigation is on line 17. The parenthesis are omitted around the statement *so.Test ?? 0*. This causes the following code to be produced (/images/I used [Lutz Roeder's .NET Reflector](/images/dotnet) tool for this):

private static [void](/images/Default.aspx?Object=1) **Main**(/images/Default.aspx?Object=2)[] args) 
{ 
 [int](/images/Default.aspx?Object=3) **num2** = 6; 
 [SomeObject](/images/Default.aspx?Object=4) **obj1** = new [SomeObject](/images/Default.aspx?Object=5)(); 
 obj1.[Test](/images/Default.aspx?Object=6) = new [Nullable](/images/Default.aspx?Object=7)<[decimal](/images/Default.aspx?Object=8)>(/images/Default.aspx?Object=9)(/images/7)); 
 [Nullable](/images/Default.aspx?Object=10)<[decimal](/images/Default.aspx?Object=11)> **nullable1** = obj1.[Test](/images/Default.aspx?Object=12); 
 [Console](/images/Default.aspx?Object=13).[WriteLine](/images/Default.aspx?Object=14)(/images/Default.aspx?Object=15) ? nullable1.[GetValueOrDefault](/images/Default.aspx?Object=16)() : new [decimal](/images/Default.aspx?Object=17)(/images/0)) / (/images/Default.aspx?Object=18)) num2)).[ToString](/images/Default.aspx?Object=19)("N")); 
 [Console](/images/Default.aspx?Object=20).[ReadLine](/images/Default.aspx?Object=21)(); 
}

The output is 1.17 and not really what one would expect.

Now with the parenthesis placed around the statement so.Test ?? 0 so line 17 becomes:

17 decimal result = (/images/(so.Test ?? 0) \* multiplicator) / workRegime;

The output becomes 5.83 and is what is expected. Now the following code is generated:

private static [void](/images/Default.aspx?Object=1) **Main**(/images/Default.aspx?Object=2)[] args) 
{ 
 [int](/images/Default.aspx?Object=3) **num1** = 5; 
 [int](/images/Default.aspx?Object=4) **num2** = 6; 
 [SomeObject](/images/Default.aspx?Object=5) **obj1** = new [SomeObject](/images/Default.aspx?Object=6)(); 
 obj1.[Test](/images/Default.aspx?Object=7) = new [Nullable](/images/Default.aspx?Object=8)<[decimal](/images/Default.aspx?Object=9)>(/images/Default.aspx?Object=10)(/images/7)); 
 [Nullable](/images/Default.aspx?Object=11)<[decimal](/images/Default.aspx?Object=12)> **nullable1** = obj1.[Test](/images/Default.aspx?Object=13); 
 [Console](/images/Default.aspx?Object=14).[WriteLine](/images/Default.aspx?Object=15)(/images/Default.aspx?Object=16) ? nullable1.[GetValueOrDefault](/images/Default.aspx?Object=17)() : new [decimal](/images/Default.aspx?Object=18)(/images/0)) \* (/images/Default.aspx?Object=19)) num1)) / (/images/Default.aspx?Object=20)) num2)).[ToString](/images/Default.aspx?Object=21)("N")); 
 [Console](/images/Default.aspx?Object=22).[ReadLine](/images/Default.aspx?Object=23)(); 
}

For developers whom are still new to this new operator you must be aware of the [operator precedence in C#](/images/6a71f45d.aspx)(/images/2). The \* operator is normally executed before the ?? operator. But in the generated code we can clearly see that the num1 variable, in our code multiplicator, is omitted which causes some strange side effects to your code to kick in.

Grz, Kris.

(/images/1): [Testing upon Nullable types in C# 2.0](/images/TestingUponNullableTypesInC20.aspx) and [Be sure to put in some default value when testing with Nullable types in .NET 2.0](/images/BeSureToPutInSomeDefaultValueWhenTestingWithNullableTypesInNET20.aspx). 
(/images/2): [operator precedence in C#](/images/6a71f45d.aspx)

[![kick it on DotNetKicks.com](/images/UseParenthesisWhenUsingTheNullCoalescingOperatorOperatorPrecedenceAlert.aspx)](/images/UseParenthesisWhenUsingTheNullCoalescingOperatorOperatorPrecedenceAlert.aspx)
