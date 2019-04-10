# tutorial_django
What's this?
------------
tutorial django python and others web features

1. Colorer
-----------------

Had you ever thought, the offered site theme not pleased you? 
You imagined how it looks like if you could change color theme by yourself.
This project uses this idea of color changing by user click in django framework.
The hard nut to crack was how define a contrast font to given backgraund color. 
This link https://github.com/muesli/gamut gave me a hand.

2. Prerequisites:
------------------
You should have Python3
File requirements.txt in the project contains all modules you need
If you use PyCharm, add this file in section File->Settings->Tools->Python Integrated Tools into field Package requirements file
Set your virtual environment, and run django.

3. Description
-------------------
The main idea was generate random color and implement given number in css style. 
While implementation I realised that Python has not offering access to change DOM objects directly. 
So the first task is  -- How change the css parameter dynamically?
jquery could does this task easily, so I have adding support jquery in the project. The question is type difference in python and javascript. 
So the second task is -- How serialize variables in python and deserialize them in javascript?
JSON could does this task easily, so I have adding support jsonpickle in the project. jsonpickle.encode() serializes values in python, and  jQuery.parseJSON() deserializes them in javascript section of html.
The third task is -- How simplify changing of DOM objects and do this change in one place?
CSS offers root: definition of variables, so I have defining some variables there and using them in colors section of objects css. This way allows make one changing in many places in one act.
