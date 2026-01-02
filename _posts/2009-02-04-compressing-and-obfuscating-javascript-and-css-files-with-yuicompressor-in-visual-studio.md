---
layout: post
title: "Compressing and obfuscating javascript and css files with YUICompressor in Visual Studio"
date: 2009-02-04T15:19:01.773375-08:00
tags: ["Compression", "CSS", "Javascript", "Visual Studio"]
author: "adminKris"
guid: "a13a3adf-dfed-4b1b-ab56-732e0e38cac8"
published: true
comments: true
show_on_front: true
last_modified_at: 2009-02-04T15:19:01.773375-08:00
---

Though external javascript and css files can be cached by a browser the initial download can still be quite large. For example the minified [jQuery](/images/www.jquery.com) library compared with the uncompressed one, or even the visual studio documented one is considerable. A while ago, for my current project, I also faced the problem of lots of script files in the project either created by the team or provided by a design company. This however hurt performance so I took some time to dig into the matter and try out several compression tools. The best one I found so far is **[YUICompressor](/images/compressor)** from Yahoo!. It’s written in java but that shouldn’t stop you from giving it a try. The nice thing about it is that one can provide arguments to the command line tool to get a different outcome like for example the switch --nomunge which tells the tool to only minify the javascript and not to obfuscate local symbols. According to Wikipedia obfuscation means:

***Obfuscation** is the concealment of meaning in* [*communication*](/images/Communication)*, making communication* [*confusing*](/images/Confusing)*, intentionally* [*ambiguous*](/images/Ambiguity)*, and more difficult to* [*interpret*](/images/Interpret)*.*

It also has a side effect benefit that mostly the file even becomes a little bit smaller.

Because as a .NET developer I mainly work with Visual Studio and I like to stay in that environment instead of going to a command prompt, typing in the commands to run the tool. Luckily Visual Studio provides the needed mechanism to automate this process without leaving the IDE itself.

In the menu select **Tools** > **External Tools…** 
There you can add a new entry like in the image by clicking the Add button.

[![YUICompressor](/images/YUICompressor_thumb.jpg "YUICompressor")](/images/YUICompressor_2.jpg)

I added the YUICompression entry. The command is the executable file, in this case java.exe which is needed to run the jar file. The arguments section is the most interesting one though as this provides us the way to tweak the arguments of the command line tool. Also note that I put the compression tool in my c:\ root directly.

The whole line reads as:

**-jar C:\yuicompressor-2.4.2.jar $(/images/ItemPath) -o $(/images/ItemDir)$(/images/ItemFileName).min$(/images/ItemExt) –v**

For the CSS file compression I added another entry but with this in the Arguments section:

**-jar C:\yuicompressor-2.4.2.jar $(/images/ItemPath) -o $(/images/ItemPath) –v**

The reason for this is because I like the javascript, when minified, get the filename that indicates that it was minified so I add the .min in between. The added benefit for this is that you can still keep the original .js file for changes, and then minify it again of course. I don’t do this for the css files as they don’t get obfuscated and it’s easy to reformat the document again with the default keyboard combination ctrl + k, ctrl + d (/images/Menu > **Edit** > **Advanced** > **Format document**).

Now that we’ve got this into place it’s quite easy. In the Solution explorer you just select a .js or .css file and from the menu **Tools** > **YUICompression** you can let the tool do its magic.

Grz, Kris.
