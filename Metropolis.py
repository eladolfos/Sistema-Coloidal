# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:50:48 2019

@author: Miguel
"""

import math
import random
import time
from scipy.stats import variation 




###Caracteristicas del sistema
L= 20 #lado de la caja
R=L/40#radio de las particulas

###POTENCIAL LENNARD-JONES  Y ENERGIA DEL SISTEMA
     
def v(r):
    
    s=4*R#s(sigma): distancia a la que el potencial entre particulas es 0
    e=1#e(epsilon): profundidad del potencial
    #r: distancia entre particulas
    return 4*e*((s/r)**12-(s/r)**6)


def energia(lista):
    E=0
    for particula1 in lista:
        for particula2 in lista:
            if particula1 != particula2:
                r =math.sqrt((particula1[0]-particula2[0])**2+(particula1[1]-particula2[1])**2)
                E=E + v(r)
    return 0.5*E
    
#Funcion de movimiento

def movimiento(lista):
    
    desplazamiento = 0.1*R
    angulo = random.uniform(0,2*math.pi)
    
    nueva_lista = [x[:]for x in lista]
    
    particula_a_mover= random.choice(nueva_lista)
    nueva_lista.remove(particula_a_mover)                                                                                                  
    
    particula_a_mover[0]=particula_a_mover[0]+desplazamiento*math.cos(angulo)
    if particula_a_mover[0]<R:
        particula_a_mover[0] = R
    if particula_a_mover[0]>L-R:
        particula_a_mover[0] = L-R  
        
    particula_a_mover[1]=particula_a_mover[1]+desplazamiento*math.sin(angulo)
    if particula_a_mover[1]<R:
        particula_a_mover[1] = R
    if particula_a_mover[1]>L-R:
        particula_a_mover[1] = L-R 
    return nueva_lista, particula_a_mover



        
    



        
###DINAMICA Y METROPOLIS
tiempos = []
start_time= time.time()

energias = []
#n=0
with open('config_inicial.txt') as f:
    coordenadas = [ line.split() for line in f]
coordenadas = [list(map(float, sublist)) for sublist in coordenadas]


for i in range(1,100001): 
    nuevas_coordenadas = []
    while len(coordenadas) != len(nuevas_coordenadas):
        superposicion = False
        nueva_energia_mayor = False
        nuevas_coordenadas, nueva_particula = movimiento(coordenadas)
        
      
        for coordenada in nuevas_coordenadas :
            nueva_distancia=math.sqrt((nueva_particula[0]-coordenada[0])**2
                            +(nueva_particula[1]-coordenada[1])**2)
            
            if nueva_distancia < 2*R :
                superposicion = True
              
                break
           
        if not superposicion and energia(nuevas_coordenadas + [nueva_particula])<=energia(coordenadas):
            nuevas_coordenadas.append(nueva_particula)
            coordenadas = [x[:]for x in nuevas_coordenadas]
            energias.append(energia(nuevas_coordenadas))
            #n += 1 
            #print(n)
            tiempos.append(time.time()-start_time)
    #GUARDAR EN UN ARCHIVO TXT: Tiempo y Energia para cada nueva configuracion aceptada y configuracion final
    if len(tiempos)%200 ==0:
        mitiempo = ["{0} \n".format(x) for x in tiempos]
        with open('tiempos.txt', 'w') as out_file:
            out_file.writelines(mitiempo)           

        misposiciones = ["{0} {1}\n".format(x1, x2) for (x1, x2) in coordenadas]
        with open('config_final.txt', 'w') as out_file:
            out_file.writelines(misposiciones) 

        misenergias = ["{0} \n".format(x) for x in energias]
        with open('energias.txt', 'w') as out_file:
            out_file.writelines(misenergias)
            
        desviacion = variation(energias[-100:])
        if abs(desviacion) <= 0.005:
            break
#tiempo que le tomo terminar
print(time.time()-start_time)           

  
                  







        
              

      
    
