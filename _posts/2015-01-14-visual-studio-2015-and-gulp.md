---
layout: post
title: "Visual Studio 2015 and Gulp"
date: 2015-01-14T04:41:56.735631-05:00
tags: ["Bower", "Gulp", "Less", "Visual Studio", "Visual Studio 2015"]
author: "adminKris"
guid: "206224f2-6aa6-4cc8-8020-1ed702fe1b2f"
published: true
comments: true
show_on_front: true
last_modified_at: 2015-01-14T04:41:56.735631-05:00
---

I’ve been fiddling around lately with [Gulp](/images/ "Gulp") and [Bower](/images/ "Bower"). 2 tools that go hand in hand to make compelling web applications and… also integrate nicely in the new Visual Studio.

Gulp is a javascript based task runner and Bower is “package manager for the web”. Why bother you might ask yourself? Well, that’s a good question. In the recent years we’ve been enjoying bunding and minification which can be found in the [ASP.NET](/images/www.asp.net) [System.Web.Optimization](/images/system.web.optimization%28v=vs.110%29.aspx "System.Web.Optimization") namespace. That’s going to be gone in ASP.NET 5 (/images/or vNext as we’ve known it up until recently).

Just follow along on how to get started with the new wave.

### Create a new project

Start Visual Studio 2015. Create a new project. Opt for ASP.NET Web Application.

[![01](/images/01_thumb.png "01")](/images/01_2.png)

Give it a meaningful name and press OK and opt in the following screen for ASP.NET 5 Starter Web

[![02](/images/02_thumb.png "02")](/images/02_2.png)

Again press the OK button and let the project be generated. After that you can open the nodes of wwwroot and Dependencies.

What’s under wwwroot

[![03](/images/03_thumb.png "03")](/images/03_2.png)

### Quick overview of the new template

What’s new in ASP.NET 5.0 is the wwwroot folder. This is going to be the place to put static files like CSS, images, html, javascript files.

Something else which is new is that you don’t have a web.config file anymore. There are also some newcomers in the form of .json files:

* bower.js: contains the Bower packages
* config.json: the main configuration file
* package.json: lists the npm packages
* project.json: the main project file.

### Using npm to install Gulp

Gulp itself is not yet in the template. To get this into it take the following steps:

1. open package.json
2. add a new entry under devDependencies: “gulp”: “^3.8.10”. Save the file.
3. under the NPM node in your Solution Explorer pane you’ll notice that that a new subnode has appeared suffixed with (/images/not installed): 
 [![04](/images/04_thumb.png "04")](/images/04.png)
4. Right click the NPM node and select **Restore Packages** from the context menu that appears.
5. Now the package is installed: 
 
 [![05](/images/05_thumb.png "05")](/images/05.png)
6. Your package.json file will now look like the following:

```
{
 "version": "0.0.0",
 "name": "GulpTestingInVS2015",
 "devDependencies": {
 "grunt": "^0.4.5",
 "grunt-bower-task": "^0.4.0",
 "gulp": "^3.8.10"
 }
}
```

In the same fashion add entries for gulp-less and gulp-minify-css. As you can guess from the names these are respectively to transform a .less file to css and to minify a css file.

### Gulp it up

Now that we have our ingredients ready we’re going to start to follow the recepy. In the solution, in the root folder of your project add a new file called **gulpfile.js**. Right click on it. In the context menu you select **Task Runner Explorer**. A new pane will open and a reference to gulp will appear in it. If you want to get rid of the default Grunt tasks you can simply delete the gruntfile.js file. I noticed that it’s a good habit to frequently refresh the overview in the Task Runner Explorer with the dedicated Refresh button.

Create a subfolder Assets under the root of the application. In there place 2 .less files: Colors.less and Styles.less.

**Colors.less**:

```
@color:#b6ff00;
@backcolor:#808080;
```

**Styles.less**:

```
@import "Colors.less";

body {
 background-color: @backcolor;
}

a {
 color: @color;

 &:hover {
 color: @color + @backcolor;
 }
}
```

[![06](/images/06_thumb.png "06")](/images/06.png)

**gulpfile.js**:

```
"use strict";

var gulp = require('gulp');
var less = require('gulp-less');
var minifyCSS = require('gulp-minify-css');

gulp.task('LessAndMinifyCSS', function () {
 gulp.src('Assets/Styles.less')
 .pipe(/images/less())
 .pipe(/images/gulp.dest('wwwroot/css'));
});
```

What goes on in this gulp file is that first declarations are made for the packages we’re going to make use of in our function. Then a Gulp task is created with the name LessAndMinifyCSS. We’ll also see, after a refresh, that function name appear in the Task Runner Explorer.

In the Gulp task we first set the source of our less files. Then via pipiing we execute the less package functionality over what was just loaded. Then the transformed result will be written down with destination wwwroot/css.

In the Task Runner Explorer hit the refresh button. Drill down to the node LessAndMinifyCSS. Right click on it and select Run.

In the output window of the Task Runner Explorer we can see that our less transformation was successful:

[![07](/images/07_thumb.png "07")](/images/07.png)

When we take a look in the Solution Explorer pane we’ll also notice that a new file was generated:

[![08](/images/08_thumb.png "08")](/images/08.png)

If it doesn’t show up directly then click the Refresh button, circled in red.

The content of the **Styles.css** file is as expected:

```
body {
 background-color: #808080;
}
a {
 color: #b6ff00;
}
a:hover {
 color: #ffff80;
}
```

So with not too much effort we were able to transform our less file to a css file. Now lets take it one step further. We’ll easily as well add CSS minification to our process. Change the **gulpfile.js** file as follows:

```
"use strict";

var gulp = require('gulp');
var less = require('gulp-less');
var minifyCSS = require('gulp-minify-css');

gulp.task('LessAndMinifyCSS', function () {
 gulp.src('Assets/Styles.less')
 .pipe(/images/less())
 .pipe(/images/minifyCSS({keepBreaks:false}))
 .pipe(/images/gulp.dest('wwwroot/css'));
});
```

The output of the **Styles.css** file after running the Gulp task again has now become:

```
body{background-color:grey}a{color:#b6ff00}a:hover{color:#ffff80}
```

Now in the Task Runner Explorer right click the LessAndMinifyCSS task. Click the Bindings menu item and then select Before Build.

[![09](/images/09_thumb.png "09")](/images/09.png)

Now each time you build your project the Gulp task will be run resulting in your Styles.css file to be updated. Of course there are a lot more Gulp packages that you can use but that’s a story for another blog post.

Grz, Kris.
