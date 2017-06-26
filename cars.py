# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:20:07 2017

@author: Mario
"""
x,y,z,w,t,p='Tesla','Buick','Ferrare','Ford','Lamborghini','Maserati'
a,e,i,o,u=1,2,3,4,5
k=[x,y,z,w,t,p]
m=[a,e,i,o,u]
f=['a','e','i','o','u']

for i in k:
    h=[]
    for j,b in enumerate(f):
        if b in i:
            h.append(m[j])
    print(i, h)