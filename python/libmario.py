# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:38:34 2017

@author: Mario
"""

def mario(name):
    print('Hola, %s' %name)
    
    
class silla(object):
    def __init__(self,material,color):
        self.material=material
        self.color=color
        self.status='Free'
        
        
    def usar_(self):
        self.status= 'Busy'
        print('Silla ocupada')
        
        
    def desocupar_(self):
        self.status='Free'
        print('Silla libre')
        
    
    
        
class motor(object):
    def __init__(self,potencia,capacidad,numero):
        self.potencia=potencia
        self.numero=numero
        self.capacidad=capacidad
        
        
    def encender(self):
        print('Encendido')
        
    def acelerar(self):
        print('acelerar')
        
        
class automovil(object):
    def __init__(self,marca,modelo,año):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.motor=motor(potencia='potencia',capacidad='5 vehículos',numero='número')
        
    def arrancar(self):
        print('Carro arrancado')
        
    def acelerar(self):
        print('Acelerando')
        
    def frenar(self):
        print('Frenando')




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


class Refreco(Bebidas):
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
        
    


