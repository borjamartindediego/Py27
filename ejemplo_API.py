# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:48:10 2019

@author: BorjaLocal
"""
import json,io
#convertimos el json a python

#"_entityId" "slug"



#C:\Users\BorjaLocal\Desktop\PYTHON\Eljercicios 3.7\DOCS\ejemplo_API.txt



#f = open('ejemplo_API.txt') #,encoding='utf-8' valido en py3

f = io.open('ejemplo_API.txt',mode='r',encoding='utf-8')
txtjson=f.read()



json.loads(txtjson)

