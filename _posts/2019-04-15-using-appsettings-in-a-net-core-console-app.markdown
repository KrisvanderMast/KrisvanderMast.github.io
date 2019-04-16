---
layout: post
title: "Using appsettings.json in a .NET Core console application"
date: 2019-04-15 17:49:00 +0200
comments: true
published: true
categories: ["post"]
tags: [".NET Core"]
author: Kris van der Mast
---
Most samples one sees about using settings in .NET Core is about setting up an ASP.NET Core application. Very handy but sometimes I simply want to make use of a console application and have that run on some server.  

You can add the following code in the `Main` method of the console application:

```csharp
var builder = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true);

IConfigurationRoot configuration = builder.Build();

Console.WriteLine(configuration.GetConnectionString("Storage"));
```

The _appsettings.json_ file might look like the following:

```json
{
    "ConnectionStrings": {
        "Storage": "STORAGE-CONNECTION-STRING"
    }
}
```
In your code file you'll also need to add the following using statements:  

```csharp
using System.IO;
using Microsoft.Extensions.Configuration;
```

You'll also need to install the following Nuget packages for the `ConfigurationBuilder`, `SetBasePath` and `AddJsonFile` to work:

> Install-Package Microsoft.Extensions.Configuration  
> Install-Package Microsoft.Extensions.Configuration.FileExtensions  
> Install-Package Microsoft.Extensions.Configuration.Json

Kris.