---
layout: post
title: "Exporting and importing Visual Studio 2005 settings"
date: 2006-10-22T07:05:16.732000-07:00
tags: ["VS.NET"]
author: "adminKris"
guid: "b9b9c9a5-99a8-4be2-a61b-e373fa30cab6"
published: true
comments: true
show_on_front: true
last_modified_at: 2006-10-22T07:08:54.310125-07:00
---

I develop on several different pc's like the one that's provided by the customer, my laptop, ... I'm one of those people that likes their custom added keyboard shortcuts, custom color markup in the code. Loosing these settings, or having to set them all again when changing to another computer, would be cumbersome and a waste of time. Luckely for us Visual Studio 2005 provides the ability to export these settings and import them on another computer.

**Exporting**:

Go to Tools | Import and Export Settings... and the following screen will appear (/images/Figure 1):

[![](/images/ImportExportSettingsWizard_thumb6.png)](/images/ImportExportSettingsWizard10.png) 
**Figure 1**: Import and Export Settings Wizard

Choose Next and the following screen will be displayed:

[![](/images/ImportExportSettingsWizard2.png)](/images/ImportExportSettingsWizard21.png) 
**Figure 2**: Select the settings to export

Check all the settings you want to export and choose Next. In the next step you can provide the location and name for the exported settings:

[![](/images/ImportExportSettingsWizard3.png)](/images/ImportExportSettingsWizard31.png) 
**Figure 3**: Specify a name for the exported settings and a location

Choose Finish the wizard will export all your settings. Now you just copy the generated file to your other pc and follow the Importing steps.

**Importing**:

Go to Tools | Import and Export Settings... The screen of Figure 1 will display. Choose **Import selected environment settings** and click Next. You get another possibility to first backup the current settings of the new computer. If it's your computer you can decide to not backup the current settings but if it's a pc that's also used by others its a wise precaution to backup first!

[![](/images/ImportExportSettingsWizard4.png)](/images/ImportExportSettingsWizard41.png) 
**Figure 4**: Possibility to backup the current settings before importing new settings.

Then you select the settings you want. In this example I chose the exported settings:

[![](/images/ImportExportSettingsWizard5.png)](/images/ImportExportSettingsWizard51.png) 
**Figure 5**: Select the settings to import

[![](/images/ImportExportSettingsWizard6.png)](/images/ImportExportSettingsWizard61.png) 
**Figure 6**: Select settings to import

After that you choose Finish and let Visual Studio 2005 import the settings.

Grz, Kris.

[![kick it on DotNetKicks.com](/images/ExportingAndImportingVisualStudio2005Settings.aspx)](/images/ExportingAndImportingVisualStudio2005Settings.aspx)
