---
layout: post
title: Using Python in Power BI
date: 2024-02-13 10:59:12 +0200
comments: true
published: true
categories: ["post"]
tags: ["power bi","python"]
author: Kris van der Mast
---
In the former blog post we set up the [virtual environment][1] for [Python in Power BI][2]. In this post, I will show you how to use Python in Power BI.

### To check

Be sure to activate the virtual environment in a command prompt, I'm using powerbienv in the examples as set up in the [former blog post][2]. If you haven't yet install the packages `numpy`, `pandas` and `matplotlib` by typing `pip install numpy pandas matplotlib`. This will install the packages in the virtual environment. We will need these packages to manipulate and visualize data in Power BI.

### Create a new report

After creating a new reportin Power BI, check if the virtual environment is set up correctly as per the [former blog post][2]. If so select `Get datasource` > `More...` > `Other` > `Python script` and click `Connect`.

![][3]

Then provide some snippet of Python code and click `OK`.

I used the following sample code based on Lorem Ipsum text:

```python
import pandas as pd

data = [
    ['Lorem', 'ipsum', 'dolor', 'sit', 'amet'],
    ['consectetur', 'adipiscing', 'elit', 'sed', 'do'],
    ['eiusmod', 'tempor', 'incididunt', 'ut', 'labore'],
    ['et', 'dolore', 'magna', 'aliqua', 'Ut'],
    ['enim', 'ad', 'minim', 'veniam', 'quis'],
    ['nostrud', 'exercitation', 'ullamco', 'laboris', 'nisi'],
    ['ut', 'aliquip', 'ex', 'ea', 'commodo'],
    ['consequat', 'Duis', 'aute', 'irure', 'dolor'],
    ['in', 'reprehenderit', 'in', 'voluptate', 'velit'],
    ['esse', 'cillum', 'dolore', 'eu', 'fugiat']
]

df = pd.DataFrame(data, columns=['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5'])  
```

![][4]

Press OK and the navigator will appear. Here you can select the data you want to import.

![][5]

Press the Transform Data button.

After you followed all the steps you can open the Advanced Editor and see the Python script that was generated. You can now use Python to manipulate and visualize your data in Power BI.

{% raw %}

```lua
let
    Source = Python.Execute("import pandas as pd#(lf)#(lf)data = [#(lf)    ['Lorem', 'ipsum', 'dolor', 'sit', 'amet'],#(lf)    ['consectetur', 'adipiscing', 'elit', 'sed', 'do'],#(lf)    ['eiusmod', 'tempor', 'incididunt', 'ut', 'labore'],#(lf)    ['et', 'dolore', 'magna', 'aliqua', 'Ut'],#(lf)    ['enim', 'ad', 'minim', 'veniam', 'quis'],#(lf)    ['nostrud', 'exercitation', 'ullamco', 'laboris', 'nisi'],#(lf)    ['ut', 'aliquip', 'ex', 'ea', 'commodo'],#(lf)    ['consequat', 'Duis', 'aute', 'irure', 'dolor'],#(lf)    ['in', 'reprehenderit', 'in', 'voluptate', 'velit'],#(lf)    ['esse', 'cillum', 'dolore', 'eu', 'fugiat']#(lf)]#(lf)#(lf)df = pd.DataFrame(data, columns=['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5'])"),
    df1 = Source{[Name="df"]}[Value],
    #"Changed Type" = Table.TransformColumnTypes(df1,{{"Column 1", type text}, {"Column 2", type text}, {"Column 3", type text}, {"Column 4", type text}, {"Column 5", type text}})
in
    #"Changed Type"
```

{% endraw %}

You can now press the `Close & Apply` button and use the data in your reports just like any other data source. 

[1]: https://www.krisvandermast.com/post/2024/01/23/setting-up-a-virtual-environment-in-python
[2]: https://www.krisvandermast.com/post/2024/02/06/setting-up-python-for-power-bi
[3]: /images/python_power_bi_python_script_connector.png
[4]: /images/python_power_bi_python_script_editor.png
[5]: /images/python_power_bi_python_script_navigator.png
