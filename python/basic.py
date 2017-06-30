# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:28:13 2017
@author: Mario
"""
from urllib.request import urlopen
from urllib.parse import quote
import json

a=quote('mario')
b=quote('Las alamedas')

dirs=[]
url='https://maps.googleapis.com/maps/api/geocode/json?address='

with open('file.txt') as file:
    for i in file:
        dirs.append(url+quote(i))

jsons=[]
responses=[]
for i,j in enumerate(dirs):
    print(i)
    responses.append(urlopen(j).read().decode('utf-8'))
    jsons.append(json.JSONDecoder().decode(responses[i]))
#    print(jsons[i]['status'])

#with open('')
#    print(jsons[i]['status'])












