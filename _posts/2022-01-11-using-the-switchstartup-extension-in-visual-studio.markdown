---
layout: post
title: "Using the switchstartup extension in Visual Studio"
date: 2022-01-11 09:17:00 +0200
comments: true
published: true
categories: ["post"]
tags: ["visual studio", "switchstartup", "extension"]
author: Kris van der Mast
---
Last week I wrote about [making use of the _Current selection_ setting to quickly have the startup project set][1] when you're having the focus on that particular project.

That's quite handy if you only need to startup only one particular project. But sometimes you need to have multiple running to test something. The solution at my current project contains 73 projects as we speak. Several class libraries, code generators, console ([TopShelf][2]) applications and [ASP.NET Web API][3]'s. As we make use of [NServiceBus][4] a lot in our solutions we like to test with different projects running at the same time. But also to quickly switch between other different publishers or receivers. In the past I went into the properties of the solution, select in the multiple startup projects and had to scroll, find and check the ones I wanted to start. Same again when switching to other applications.  
Quite a time waster...  

In [Visual studio][5]/[Visual Studio Code][6] ususally things go way smoother when installing extra [extensions][7]/[vs code extensions][8]. For the above described annoyance I found quite a nice extension for [Visual Studio][5]: [SwitchStartupProject for VS 2022][9].

Once installed the extension will add a new item in the toolbar of Visual Studio.

![Switch startup project][10]

Hitting that `Configure...` menu item will open up a json file like the following (for our demo project):

```json
/*
    This is a configuration file for the SwitchStartupProject Visual Studio Extension
    See https://heptapod.host/thirteen/switchstartupproject/blob/branch/current/Configuration.md
*/
{
    /*  Configuration File Version  */
    "Version": 3,

    /*  Create an item in the dropdown list for each project in the solution?  */
    "ListAllProjects": true,

    /*
        Dictionary of named configurations with one or multiple startup projects
        and optional parameters like command line arguments and working directory.
        Example:

        "MultiProjectConfigurations": {
          "A + B (Ext)": {
            "Projects": {
              "MyProjectA": {},
              "MyProjectB": {
                "CommandLineArguments": "1234",
                "WorkingDirectory": "%USERPROFILE%\\test",
                "StartExternalProgram": "c:\\myprogram.exe"
              }
            }
          },
          "A + B": {
            "Projects": {
              "MyProjectA": {},
              "MyProjectB": {
                "CommandLineArguments": "",
                "WorkingDirectory": "",
                "StartProject": true
              }
            }
          },
          "D (Debug x86)": {
            "Projects": {
              "MyProjectD": {}
            },
            "SolutionConfiguration": "Debug",
            "SolutionPlatform": "x86",
          },
          "D (Release x64)": {
            "Projects": {
              "MyProjectD": {}
            },
            "SolutionConfiguration": "Release",
            "SolutionPlatform": "x64",
          }
        }
    */
    "MultiProjectConfigurations": {}
}
```

The list already shows all the projects in our solution which is great. When we want to add a setup where we want to start the following applications we adjust the aforementioned json configuration file like this (left out the comments):

```json
  "MultiProjectConfigurations": {
    "AllThreeApps": {
      "Projects": {
        "Console01": {},
        "Console02": {},
        "WebApplication01": {}
      }
    }
  }
```

When you want to pass arguments you can change it like:

```json
  "MultiProjectConfigurations": {
    "AllThreeApps": {
      "Projects": {
        "Console01": {},
        "Console02": {
          "CommandLineArguments": "https://www.krisvandermast.com/"
        },
        "WebApplication01": {}
      }
    }
  }
```

When you save it you'll see all of sudden the following appear in the solution:

![Switch startup project json config with command line arguments][11]

Which holds the following json:

```json
{
  "profiles": {
    "Console02": {
      "commandName": "Project",
      "commandLineArgs": "https://www.krisvandermast.com/"
    }
  }
}
```

I changed the code of Console02 app to the following to showcase the arguments:

```csharp
Console.Title = "Console02 sample app";

Console.WriteLine(args[0]);

Console.Read();
```

And when running this (only took a screenshot of Console01 and Console02 here):

![Output Console01 and Console02 sample apps][12]

[1]: /post/2022/01/04/current-selection-startup-project-in-visual-studio.html
[2]: http://topshelf-project.com/
[3]: https://dotnet.microsoft.com/en-us/apps/aspnet/apis
[4]: https://www.particular.com/
[5]: https://visualstudio.microsoft.com/
[6]: https://code.visualstudio.com/
[7]: https://marketplace.visualstudio.com/vs
[8]: https://marketplace.visualstudio.com/VSCode
[9]: https://marketplace.visualstudio.com/items?itemName=vs-publisher-141975.SwitchStartupProjectForVS2022
[10]: /images/switchstartupprojectintoolbar.png
[11]: /images/switchstartupprojectintoolbarwitharguments.png
[12]: /images/switchstartupprojectintoolbarconsole02sampleappoutput.png
