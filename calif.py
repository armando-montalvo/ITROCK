# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:10:46 2017

@author: Mario
"""

import numpy as np

print('Alumno    ','Score     ','Message     ')
print("")
arturo=[90,100,50,70]
juan=[90,90,100,80]
artemio=[70,65,100,80]
rene=[50,60,70,80]
pedro=[100,50,100,90]
h=['arturo','artemio','juan','rene','pedro']

studs=[arturo,artemio,juan,rene,pedro]

for j,i in enumerate(studs):
    u=np.array(i).mean()
    if u > 95:
        t="excentado"
    elif u<95 and u>=85:
        t="aprobado"
    elif u>=70 and u<85:
        t="promedio"
    elif u<70:
        t="reprobado"
    print("%s    %0.2f        %s" % (h[j],u,t))
    

    