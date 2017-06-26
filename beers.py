# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 16:37:20 2017

@author: Mario
"""

beers=[{'name':'Modelo especial','precio':25.00,'ap':4.0},
       {'name':'Indio     ','precio':20.00,'ap':4.2},
       {'name':'Tecate Light', 'precio':30.00,'ap':3.5},
       {'name':'Minerva','precio':35.00,'ap':8.0},
       {'name':'Budlight','precio':18.00,'ap':5.0}]

print('Name               Precio         Procentaje')
for i in beers:
    print('%s          %0.2f     %0.2f' % (i['name'],i['precio'],i['ap']))


beers.append({'name':'XX','precio':20.00,'ap':2.00})
