# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LyX2LKJh7FfDegN5O1C--dZcMEap13i8
"""

import json

DATA_PATH = 'en_medical_dialog.json'

f = open(DATA_PATH)
content = json.load(f)


data_to_use = []
for i in range(1,len(content)):
    
    if "http" in content[i]["Doctor"]:
      data_to_use.append(content[i])

print(len(data_to_use))


#for i in range(1,len(data_to_use)):
   # print(data_to_use[i])


a = []
for i in range(1,len(content)):
    
    if "gist" in content[i]["Doctor"]:
      a.append(content[i])
    elif "rist" in content[i]["Doctor"]:
      a.append(content[i])
    elif "tist" in content[i]["Doctor"]:
      a.append(content[i])
     # print(content[i]["Doctor"])
    elif "surgeon" in content[i]["Doctor"]:
      a.append(content[i])
    elif "pist" in content[i]["Doctor"]:
      a.append(content[i])
    
print(len(a))

