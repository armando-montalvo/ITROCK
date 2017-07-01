# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:28:13 2017
@author: Mario
"""
from urllib.request import urlopen
from urllib.parse import quote
import json
from insert import *


a=quote('mario alberto briseño zamarripa')

dirs=[]
url='https://maps.googleapis.com/maps/api/geocode/json?address='
adrs=[]

temp=open('dir.txt','r')
tmp=temp.read()
temp.close()
tmp=tmp.split('\n')
tmp.remove('')

for i in tmp:
    adrs.append(i)
    dirs.append(url+quote(i))
        
jsons=[]
responses=[]
for i,j in enumerate(dirs):
    print(i)
    responses.append(urlopen(j).read().decode('utf-8'))
    jsons.append(json.JSONDecoder().decode(responses[i]))
#   print(jsons[i]['status'])


name='chido.txt'
name2='nochido.txt'
good=open(name,'a')
wrong=open(name2,'a')

for i in range(len(dirs)):
    if jsons[i]['status'] == 'OK':
        
        print(jsons[i]['results'][0]['formatted_address'],jsons[i]['status'],
              jsons[i]['results'][0]['geometry']['location']['lat'],
              jsons[i]['results'][0]['geometry']['location']['lng'],
              sep='|',file=good)
    else:
        print(adrs[i], jsons[i]['status'],sep='|',file=wrong)
good.close()
wrong.close()

ar=  open(name,'r').read()
ar=  ar.split('\n')
ar.remove('')
ar2= open(name2,'r').read()
ar2= ar2.split('\n')
ar2.remove('')


print('Creating tables from file with addresses')
insert_ok(ar)
insert_fail(ar2)
print('''Done, addresses have been splited in 2 different files. 
Also 2 schemes were created using MySQL. Available at irock server''')
