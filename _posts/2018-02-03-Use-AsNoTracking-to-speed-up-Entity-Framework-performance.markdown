---
layout: post
title: "Use AsNoTracking to speed up Entity Framework performance"
date: 2018-02-03 16:59:00 +0100
comments: true
published: true
categories: ["post"]
tags: ["Performance", "Entity Framework", "Tips and tricks"]
author: Kris van der Mast
---
I'm curently busy at a large project in the insurance sector. The original architecture implemented the onion architecture and took from the database a lot of data and the mangling it through a bunch of `foreach` loops in C#.  

As testers were complaining about performance I was put on the task to optimize things around during the Christmas period (I wasn't taking any vacation either way).  

Basically `select * from tasks` is usually not a good idea when you have a lot of records and a lot of columns in the __Tasks__ table. As such I narrowed that down already to only the fields I needed. That already helped a lot on the performance side but still memory usage was higher than I expected. The reason for this: Entity Framework (6, which we use in this particular project) uses a feature called __tracking__ and guess what, it's on by default.  

So what does this tracking mean for you as a developer? It means that you can more easily update entities later on as Entity Framework will keep information about the tracked entity instance in its __change tracker__. Turning this feature off gives you a bit more work as a developer when updating an entity, basically it's up to you to find out which entity needs an update and set the modified state. But as a bonus you make Entity Framework consume less memory and work (a bit) more performant as it doesn't have to keep track of all the changed stuff itself.  

Sounds great no but how would you turn on this default behaviour? Well that's pretty simple, by making use of the __AsNoTracking()__ method. For example:

```csharp
using(var context = new TaskDBContext()) 
{
    var tasks = context.Tasks.AsNoTracking().ToList();
}
```

It's important to put it directly there after the DBSet property before putting `where`, `select` or other clauses in order to have effect.

In Entity Framework Core you can also make use of this and even turn it off on a context instance level, unlike Entity Framework 6 where you have to make use of `AsNoTracking()` each time. The way to do it 

```csharp
using(var context = new TaskDBContext()) 
{
    context.ChangeTracker.QueryTrackingBehavior = QueryTrackingBehavior.NoTracking;
    var tasks = context.Tasks.ToList();
}
```

I did some other big changess and effort to get the performance way better but this for sure already helped out a lot. As a sidenote the following numbers I got from the support team (which were in a slight panic apparently before my changes went live). Mind that this is on a virtualized server with about 20-30 applications running but the new application toulk quite a heavy load on it:

|        | Before | After |
|-------:|:------:|:-----:|
| Memory |   3Gb  | 700Mb |
| CPU    |  100%  | 0-10% | 

Not bad results, especially the CPU usage went down dramatically and the people that need to keep the servers in good shape were very much relieved.

Kris.