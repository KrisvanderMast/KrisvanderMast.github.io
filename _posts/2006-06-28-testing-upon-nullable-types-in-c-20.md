---
layout: post
title: "Testing upon Nullable types in C# 2.0"
date: 2006-06-28T12:59:22.437000-07:00
tags: [".NET 2.0"]
author: "adminKris"
guid: "cd198e55-67a4-4e60-b8a9-91f72915197c"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-07-12T13:20:02.062500-07:00
---

Most people that use C# are quite familiar with the if() expression and the (/images/?:) conditional/ternary operator. In C# 2.0, the Visual C# team introduced another operator that's less known: the ?? or null coalescing operator. A quick demo explains how to use it. The result can be seen in Figure 1:

1 using System;

 2 using System.Collections.Generic;

 3 using System.Text;

 4

 5 namespace ConsoleApplicationNullableTypes

 6 {

 7 class Program

 8 {

 9 static void Main(/images/string[] args)

 10 {

 11 int? input = null;

 12

 13 IfStatements(/images/input);

 14

 15 // Now fill up the nullable input with some value.

 16 input = 99999;

 17

 18 IfStatements(/images/input);

 19

 20 Console.ReadLine();

 21 }

 22

 23 ///

 24 /// Show the 3 different ways to write the same if functionality in C# 2.0.

 25 ///

 26 ///

 27 private static void IfStatements(/images/int? input)

 28 {

 29 int result;

 30 // Scenario 1, normal if statement

 31 if (/images/input.HasValue)

 32 result = input.Value;

 33 else

 34 result = 200;

 35

 36 Console.WriteLine("Scenario 1, result: " + result.ToString());

 37

 38 // Scenario 2, using the conditional/ternary operator

 39 result = input.HasValue ? input.Value : 200;

 40

 41 Console.WriteLine("Scenario 2, result: " + result.ToString());

 42

 43 // Scenario 3, using the null coalescing operator new to C# 2.0.

 44 result = input ?? 200;

 45

 46 Console.WriteLine("Scenario 3, result: " + result.ToString());

 47 Console.WriteLine();

 48 }

 49 }

 50 }

The 3 different manners of writing the same test. Scenario 1, line number 31, is the normal if statement. Scenario 2 uses the conditional/ternary operator and just like in scenario 1 the new method HasValue is used to check if the nullable type has a value. If so then one could fetch the value by using the Value property on the nullable type. 
Scenario 3, line number 44, uses the new null coalescing operator which is [only available in C# 2.0](/images/2hxce09y.aspx).

Since I started developing with C# 2.0 in May 2005 I used to use the code like described in scenario 2 until I found out about the null coalescing operator. I find it easier to read and to use in my code. But because I found out that not too many people seem to be aware of this new gem in the C# 2.0 language I wanted to show it off in an article.

![](/images/nullcoalescing_conditional_.png) 
**Figure 1**: The result of the test.

I also blogged about using testing serious with nullable types in the past: [Be sure to put in some default value when testing with Nullable types in .NET 2.0](/images/BeSureToPutInSomeDefaultValueWhenTestingWithNullableTypesInNET20.aspx).

Grz, Kris.

[![kick it on DotNetKicks.com](/images/TestingUponNullableTypesInC20.aspx)](/images/TestingUponNullableTypesInC20.aspx)
