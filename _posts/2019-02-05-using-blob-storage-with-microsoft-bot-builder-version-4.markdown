---
layout: post
title: "Using blob storage with Microsoft bot builder version 4"
date: 2019-02-05 07:57:00 +0200
comments: true
published: true
categories: ["post"]
tags: ["Bot builder", "Azure", "blob storage"]
author: Kris van der Mast
---
Even though the documentation of [Microsoft bot builder version 4]() is really good I noticed I couldn't find a decent explanation on how to replace the default that comes with the BOT templates in Visual Studio.

```csharp
IStorage dataStore = new MemoryStorage();
```

So I decided to figure things out, as I needed it for a project and didn't want to make use of the Azure CosmosDB option (it would've been overkill and too costly for the little startup I'm working with).  

Luckily for us when you create a new BOT with a template the code is alraedy there in the __Startup.cs__ file. Simply comment the line that sets up the `MemoryStorage` (the first code sample in this blog post). Then uncomment the following lines in the __Startup.cs__ file:  

```csharp
const string StorageConfigurationId = "botblob";
var blobConfig = botConfig.FindServiceByNameOrId(StorageConfigurationId);
if (!(blobConfig is BlobStorageService blobStorageConfig))
{
    throw new InvalidOperationException($"The .bot file does not contain an blob storage with name '{StorageConfigurationId}'.");
}
// Default container name.
const string DefaultBotContainer = "azurebotcontainerechobot";
var storageContainer = string.IsNullOrWhiteSpace(blobStorageConfig.Container) ? DefaultBotContainer : blobStorageConfig.Container;
IStorage dataStore = new Microsoft.Bot.Builder.Azure.AzureBlobStorage(blobStorageConfig.ConnectionString, storageContainer);
```

So far so good. I gave the `StorageConfigurationId` constant a name and also the `DefaultBotContainer`. The tricky part, and the one that gave me the hardest time as I didn't see documentation for it is to adapt the __.bot__ file. You'll need to add an extra service entry where the `"type": "blob"` needs to be specified exactly as is:  

```json
{
    "type": "blob",
    "name": "botblob",
    "connectionString": "UseDevelopmentStorage=true",
    "container": "azurebotcontainerechobot"
}
```

Ultimately the entire __.bot__ file for my project becomes:  

```json
{
  "name": "EchoBot3",
    "services": [
        {
            "type": "endpoint",
            "name": "development",
            "endpoint": "http://localhost:3993/api/messages",
            "appId": "",
            "appPassword": "",
            "id": "1"
        },
        {
            "type": "blob",
            "name": "botblob",
            "connectionString": "UseDevelopmentStorage=true",
            "container": "azurebotcontainerechobot"
        }
    ],
  "padlock": "",
  "version": "2.0"
}
```

As I'm testing this locally with the [Azure Storage Emulator](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-emulator) I'm using the connectionstring to make use of the setting `UseDevelopmentStorage=true`. When you deploy this you need to change this accordingly of course.

Kris.