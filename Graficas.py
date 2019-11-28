# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:54:17 2019

@author: Miguel
"""

import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


L= 20  #lado de la caja
R=L/40#radio de las particulas


with open('config_inicial.txt') as f:
    config_inicial = [ line.split() for line in f]
config_inicial = [list(map(float, sublist)) for sublist in config_inicial]

with open('config_final.txt') as f:
    config_final = [ line.split() for line in f]
config_final = [list(map(float, sublist)) for sublist in config_final]

with open('tiempos.txt') as f:
    tiempos = [ line.split() for line in f]
tiempos = [list(map(float, sublist)) for sublist in tiempos]

with open('energias.txt') as f:
    energias = [ line.split() for line in f]
energias = [list(map(float, sublist)) for sublist in energias]


###GRAFICART LA DISTRIBUCION INICIAL

fig1=plt.figure(figsize=(8.,8))#tamaño de la imagen 
ax = plt.subplot(111, aspect='equal')

box=plt.Rectangle((0,0),L,L,fill=False,lw=2)#Dibujo de la cajas
plt.gca().add_patch(box)  
           
for particula in config_inicial: 
    
    p= plt.Circle((particula[0],particula[1]),R,alpha=0.25
    ,color='r')      
    plt.gca().add_patch(p)         


plt.xlim( 0,  L)
plt.ylim(0,  L) 

plt.title('Configuración Inicial', fontsize = 30, pad = 30)
plt.axis('off')
plt.savefig('config_incial.png', quality = 95, dpi = 500)
plt.show()

###DISTRIBUCION FINAL
fig2=plt.figure(figsize=(8.,8))#tamaño de la imagen 
ax = plt.subplot(111, aspect='equal')

box=plt.Rectangle((0,0),L,L,fill=False,lw=2)#Dibujo de la cajas
plt.gca().add_patch(box)  
           
for particula in config_final: 
    
    p= plt.Circle((particula[0],particula[1]),R,alpha=0.25
    ,color='b')      
    plt.gca().add_patch(p)         


plt.xlim( 0,  L)
plt.ylim(0,  L) 
#vor = Voronoi(config_final)
#voronoi_plot_2d(vor, show_vertices= False,line_width=0.3,ax=ax,line_alpha=1)
plt.title('Configuración Final',fontsize = 30, pad = 30)
plt.axis('off')
plt.savefig('config_final.png', quality = 95, dpi = 500)
plt.show()

###ENERGIAS Y TIEMPOS   
fig3=plt.figure(figsize=(8.,8))#tamaño de la imagen  
plt.plot(energias,'k.', aa = True)
plt.xlabel('Cantidad de Configuraciones Aceptadas',labelpad= 15, fontsize = 25)
plt.ylabel('Energía',labelpad= 15, fontsize = 25)
plt.savefig('energia.png',bbox_inches = 'tight', quality = 95, dpi = 500,pad_inches=0.5)
plt.show()

fig4=plt.figure(figsize=(8.,8))#tamaño de la imagen  

plt.plot([tiempo[0]/60 for tiempo in tiempos],'r.',aa = True)
plt.xlabel('Cantidad de Configuraciones Aceptadas', labelpad= 15, fontsize = 25)
plt.ylabel('Tiempo',labelpad= 15, fontsize = 25)
plt.savefig('tiempo.png',bbox_inches = 'tight', quality = 95, dpi = 500,pad_inches=0.5)
plt.show()