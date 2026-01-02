---
layout: post
title: "Find out which version of node.js currently runs on Windows Azure Web Sites"
date: 2012-10-02T15:08:04.192677-04:00
tags: ["node.js", "Windows Azure Web Sites"]
author: "adminKris"
guid: "50d60d6b-8d3f-43c4-b7a0-4ca96c92c58f"
published: true
comments: true
show_on_front: true
last_modified_at: 2012-10-02T15:08:04.192677-04:00
---

If you’ve already opened the [new portal of Windows Azure](/images/ "Windows Azure portal") then you’ll probably have noticed that both the .NET version and PHP version installed on Windows Azure Web Sites are filled in. However there’s no such thing currently for which version of [node.js](/images/ "node.js") can be run on it. Bummer.

Of course, it’s not that difficult to find out for yourself, or find out near the end of this article. The steps involved make use of Git deployment as I just wanted to play around with that but FTP or web publishing can also be used of course.

### Step 1: Create a new Windows Azure Web Site

Navigate to the portal:

[![nodejsversion01](/images/nodejsversion01_thumb.png "nodejsversion01")](/images/nodejsversion01_2.png)

Click on the CREATE A NEW WEBSITE link or on the big + NEW sign in the lower left corner, where I usually start my journey. Select WEB SITE > QUICK CREATE and give it a unique url. Select a region and press the CREATE WEB SITE button:

[![nodejsversion02](/images/nodejsversion02_thumb.png "nodejsversion02")](/images/nodejsversion02_2.png)

Once the initialization phase has passed you have the following result:

[![nodejsversion03](/images/nodejsversion03_thumb.png "nodejsversion03")](/images/nodejsversion03_2.png)

### Step 2: Prepare for Git publishing

Click on the darker blue part which states the name of your freshly created web site. Then click on link **Set up Git publishing**. If needed you can always reset your deployment credentials when you forgot your username and password to deploy:

[![nodejsversion04](/images/nodejsversion04_thumb.png "nodejsversion04")](/images/nodejsversion04_2.png)

After having selected the Set up Git publishing link and it’s done its behind the scenes voodoo magic you’ll be presented the following screen. See that GIT URL? Well that’s going to be important in a couple of steps so either copy and paste it right now into notepad or keep in mind where you can easily find it back.

[![nodejsversion05](/images/nodejsversion05_thumb.png "nodejsversion05")](/images/nodejsversion05_2.png)

### Step 3: Make a node.js script that shows the running version

This is the little script part that will show which version you’re running. Either locally, always safe to test there, and on Windows Azure.

Create a new folder on your hard disk and create in that folder a file named **server.js**. Open notepad or your favorite editing tool of choice and type in the following code (/images/note that it’s javascript hence case sensitive):

```
var http = require('http');
http.createServer(/images/function(req, res){
	res.writeHead(/images/200, {'content-type': 'text/plain'})
	res.end('Version - ' + process.version);
}).listen(/images/process.env.port || 1337)
```

### Step 4: Getting Gitted and pushing it to Windows Azure Web Sites

If you haven’t installed Git yet, then do so now. If you’re on Windows I suggest you install [Github for Windows](/images/ "Github for Windows") as it also has a handy shell which hooks into Powershell.

If you opened the Git commandline and changed to the directory where you put the file server.js, start typing in the following commands:

1. git init
2. git add .
3. git commit –m “Initial commit”
4. git remote add azure GIT URL (/images/yes, that’s that url I told you to keep a hold on or keep it handy in notepad)
5. git push azure master

That’s it. Open the portal again and if not finished already it’ll soon be and you’ll get to see your deployment:

[![nodejsversion06](/images/nodejsversion06_thumb_1.png "nodejsversion06")](/images/nodejsversion06_4.png)

Cool!

### Step 5: Le moment suprême: Hit that BROWSE button

Yes, that’s it, don’t be afraid. Click that BROWSE button at the bottom and get to see which version of node.js is running:

[![nodejsversion07](/images/nodejsversion07_thumb.png "nodejsversion07")](/images/nodejsversion07_2.png)

And the lucky winner is: **v0.6.20**.

### Summary

This article simply showed how to create a small node.js script, make use of Git and easily deploy it to Windows Azure Web Sites and uncover the hidden version number of the running node.js version.

A tip: if you want to start with node.js and have some fancy debugging capabilities and easy web publishing, or ftp, to Windows Azure Web Sites then make use of the new cool tool on the block: **[WebMatrix 2](/images/ "WebMatrix 2")**.

For more instructional videos be sure to check out [http://www.meetwindowsazure.com/DigitalChalkTalks](/images/DigitalChalkTalks "Digital chalk talks about Windows Azure") and [http://www.youtube.com/user/windowsazure](/images/windowsazure "Windows Azure video tutorials on Youtube").

Grz, Kris.
