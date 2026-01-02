---
layout: post
title: "Getting the name of the table in which a column with specified name appears"
date: 2009-11-24T01:07:02.615750-08:00
tags: ["T-SQL"]
author: "adminKris"
guid: "5daae18e-6612-4623-8a02-dafb553d2d5e"
published: true
comments: true
show_on_front: true
last_modified_at: 2009-11-24T01:07:02.615750-08:00
---

Sometimes you need to find out in which tables a certain column name exists. For example when you want to find out where it’s being used as a foreign key. Here’s a handy script to use in T-SQL.

```
SELECT OBJECT_NAME(/images/object_id), * FROM sys.columns WHERE name = 'columnname'
```

This makes use of the [OBJECT\_NAME](/images/ms186301.aspx "OBJECT_NAME function in T-SQL") function in T-SQL which according to the documentation: *Returns the database object name for schema-scoped objects*.

Grz, Kris.
