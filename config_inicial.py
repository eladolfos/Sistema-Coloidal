# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:57:09 2019

@author: Asus
"""
import math
import random
import numpy


###VARIABLES DEL SISTEMA
L= 20*10**(-4) #lado de la caja
R=L/40#radio de las particulas
numero_de_particulas=128#numero de particulas que quiero desplegar

#Listas que usare en las iteraciones

particulas= [] #donde iran solo las particulas (objeto particula) que no se traslapan
coordenadas = []


###CONSTRUCCION DE PARTICULAS (CIRCULOS)

class particle():
    
    def __init__(self):
        
        self.x= random.uniform(R,L-R)
        self.y= random.uniform(R,L-R)
        self.R = R

###CONFIGURACION INICIAL DE PARTICULAS

while len(particulas)<numero_de_particulas:
    
    superposicion = False
    particula_propuesta = particle()
    
  
    for particula_existentes in particulas:
        distancia=math.sqrt((particula_propuesta.x-particula_existentes.x)**2
                            +(particula_propuesta.y-particula_existentes.y)**2)
            
        if distancia < 2*R and particula_propuesta != particula_existentes:
            superposicion = True
            break
        
    if not superposicion:
        particulas.append(particula_propuesta)   
        coordenadas.append([particula_propuesta.x,particula_propuesta.y])

#GUARDAR EN UN ARCHIVO TXT LA CONFIGURACION INICIAL 
myList = ["{0} {1}\n".format(x1, x2) for (x1, x2) in coordenadas]
with open('config_inicial.txt', 'w') as out_file:
    out_file.writelines(myList)

