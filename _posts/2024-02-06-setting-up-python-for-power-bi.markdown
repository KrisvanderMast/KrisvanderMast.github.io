---
layout: post
title: Setting up Python for Power BI
date: 2024-02-06 10:59:05 +0200
comments: true
published: true
categories: ["post"]
tags: ["power bi","python"]
author: Kris van der Mast
---
It is possible to use Python in Power BI. This is a great feature because it allows you to use Python scripts to manipulate your data. In this post, I will show you how to set up Python for Power BI.  

First install a version of Python. I am using version 3.11 at the moment of writing. You can [download Python from the official website][2]. After the installation, you can check if Python is installed by opening a command prompt and typing `python --version`. This should return the version of Python you installed. In my case it displays `Python 3.11.6`.

It is also possible to install multiple version of Python on your machine. You can use the `py` command to check which versions are installed. In the same command prompt, type `py -0` to see the installed versions. For my local machine the output is:

> -V:3.11 *        Python 3.11 (64-bit)  
> -V:3.9           Python 3.9 (64-bit)

The `*` indicates the default version.  

By default Power BI comes with a version of Python. You can check the version of Python that is installed by opening Power BI and going to `File` > `Options and settings` > `Options` > `Python scripting`. Here you can see the version of Python that is installed.

However for the following posts we are going to set up a virtual environment. This is a clean environment that is isolated from the rest of the system. This way we can install packages without affecting the rest of the system. Check out my former post on [how to set up a virtual environment][1].

In the command prompt, navigate to the folder where you want to create the virtual environment. I went for the folder `C:\pythonvenvs`. Now type `python -m venv powerbivenv`. This will create our demo virtual environment. To activate the virtual environment, navigate to the `Scripts` folder and type `activate`. Or from the root folder of the virtual environment, type `.\powerbivenv\Scripts\activate`.  
You can check if the virtual environment is activated by checking the command prompt. The name of the virtual environment should be displayed in the prompt.

To use the virtual environment in Power BI, you need to set the path to the virtual environment in Power BI. You can do this by going to `File` > `Options and settings` > `Options` > `Python scripting` and setting the path to the virtual environment in the `Set a Python home directory` field. In my case the path is `C:\pythonvenvs\powerbivenv\Scripts`. Note that the path should point to the `Scripts` folder of the virtual environment as that's where the activation commands reside.

Now you can use the virtual environment in Power BI. In the next post, I will show you [how to use Python in Power BI][3].

[1]: https://www.krisvandermast.com/posts/2024/01/23/setting-up-a-virtual-environment-for-python
[2]: https://www.python.org/downloads/
[3]: https://www.krisvandermast.com/posts/2024/02/13/using-python-in-power-bi
