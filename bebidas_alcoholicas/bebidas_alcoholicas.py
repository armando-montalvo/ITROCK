# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 16:47:56 2017

@author: Mario
"""

#De peperoni
#Mario Briseño, Kamid Lozano, Marco Quiroga y Fernando Michel




class Bebidas(object):
    def __init__(self,marca,nombre,contenido):
        self.marca=marca
        self.nombre=nombre
        self.contenido=contenido

    
    def abrir(self):
        print('abierta')
        
    def consumir(self):
        print('consumida')
        
    def cerrar(self):
        print('cerrada')


class Refresco(Bebidas):
    def __init__(self,sabor):
        self.sabor=sabor
        
    def perder(self):
        print('perder gas')
        
    def explotar(self):
        print('explotando')


class Bebidas_Alcoholicas(Bebidas):
    
    def emborrachar(self):
        print('emborrachar')
        
        
class Cerveza(Bebidas_Alcoholicas):
    def __init__(self, tipo_de_bebida):
        self.tipo_de_bebida=tipo_de_bebida
    
    def quemarse(self):
        print('quemandose')
        
        
