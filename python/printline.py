# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:51:22 2017

@author: Mario
"""

def print_line(long,symb='.'):
    print(symb*long)
    
    
def crear_piramide(x,sym):
    for i in range(x):
        print_line(i+1,sym)
        print('\n')
        

def crear_piramide_inv(x,sym):
    for i in range(x,0,-1):
        print_line(i,sym)
        print('\n')
        
        
def crear_piramidota(long,sym='+'):
    crear_piramide(long,sym)
    crear_piramide_inv(long-1,sym)


def piramide_1(long,datos):
    var=''
    for i in range(1,long+1):
        r=range(1,i+1)
        for j in r:
            if j == r[-1] and i == long:
                var+= datos['punta']
            elif j == r[-1]:
                #print(j,r[-1])
                var+= datos['extremo']
            else:
                var+= datos['relleno']
        print(var)
        var=''
        
        
def piramide_2(long,datos):
    var=''
    for i in range(long+1,1,-1):
        r=range(i-1,1,-1)
        for j in r:
#            if j == r[-1] and i == long+1:
#                var+= datos['punta']
            if j == r[-1]:
                #print(j,r[-1])
                var+= datos['extremo']
            else:
                var+= datos['relleno']
        print(var)
        var=''

            
def piramide(long,datos):
    piramide_1(long,datos)
    piramide_2(long,datos)
            
            
#def piramide_decorada(datos,long):
    