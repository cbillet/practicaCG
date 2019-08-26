#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:49:55 2019

Este codigo resuelve la practica 1 de Circulacion general en el que se analiza el modelo de 
circulacion oceanica de Stommel 
Se trabaja con las salidas del modelo QG, en el que el unico parametro
que se modifico fue el coeficiente de friccion de fondo

@author: Nadia, Carolina
"""


#%% cargo librerias
import numpy as np
from matplotlib import pyplot as plt
#%%cargo las salidas del modelo para k1, k2, k3 con la funcion cargar dentro de Cargar2.py
from Cargar2 import cargar 
psi_temp,vort_temp,psiF,vortF,QG_diag,QG_curlw,X,Y,dx,dy=cargar("/Users/macbookair/Desktop/practicasCG/Practica 1/Modelo_QG/out_tmp_1/",4000,2000,200,100)
psi_temp_2,vort_temp_2,psiF_2,vortF_2,QG_diag_2,QG_curlw_2,X_2,Y_2,dx_2,dy_2=cargar("/Users/macbookair/Desktop/practicasCG/Practica 1/Modelo_QG/out_tmp_2/",4000,2000,200,100)
psi_temp_3,vort_temp_3,psiF_3,vortF_3,QG_diag_3,QG_curlw_3,X_3,Y_3,dx_3,dy_3=cargar("/Users/macbookair/Desktop/practicasCG/Practica 1/Modelo_QG/out_tmp_3/",4000,2000,200,100)
#%% ejercicio 1a (evolucion de energia cinetica total)
#tomo la cuarta columna de la salida QG_diag que tiene la energia cinetica para cada paso temporal (2000 pasos) en el punto central del dominio
plt.figure()
plt.plot(QG_diag[:,0],QG_diag[:,3],label="k1")
plt.plot(QG_diag_2[:,0],QG_diag_2[:,3],label="k2")
plt.plot(QG_diag_3[:,0],QG_diag_3[:,3],label="k3")
plt.xlabel("Paso temporal")
plt.ylabel("Eenergia cinetica")
plt.title("Evolucion de energia cinetica total")
plt.legend()
plt.savefig("ejercicio1a", dpi=100)
#%% ejercicio 1b (campo de funcion corriente + campo de transporte meridional My en sv)

##defino escalas
#0 a -350000 para funcion corriente porque son los valores mas extremos que toman la funcion corriente 
#es el correspondiente a K1
#25 a -175 para transporte meridional por la misma razon
levels_psi=np.arange(-350000,10000,10000) #vector de -350000 a 0 cada 10000
levels_my=np.arange(-175,30,5) #vector de -175 a 25 cada 5

##defino magnitudes tipicas para dimensionalizar 
L=4000 #longitud de la cuenca
tau=0.3 #tension del viento en superficie
D=3000 #profundidad del oceano 
rho=1025 #densidad
betha=1e-11 
U=2*np.pi*tau/(rho*D*betha*L) 

#%% ejercicio 1b (campo defuncion corriente + campo de transporte meridional My en Sv)
#K1

#dimensionalizo funcion corriente, considero dimensiones tipicas de modelo_oceanico

psiF_dim=psiF*U*L # funcion corriente dimensionalizada (dimension m*m/s)
#ploteo funcion corriente k1
plt.figure()
plt.contourf(X,Y,psiF_dim, levels_psi)
plt.title("Campo de funcion corriente k1")
plt.colorbar()
plt.savefig("1b funcion corriente k1", npi=100)

#calculo transporte meridional k1
My=D*(np.diff(psiF_dim,n=1, axis=1))/1e6 #(Profundidad * variacion de la funcion corriente en funcion de x (v) / paso a Sv)

#ploteo transporte meridional k1
plt.figure()
plt.contourf(X[0:199],Y,My,levels_my) #hasta 199 porque en la derivacion diff se fue un x 
plt.title("Campo de transporte meridional k1")
plt.colorbar()
plt.savefig(" 1b transporte meridional k1", npi=100)

#%% ejercicio 1b (campo defuncion corriente + campo de transporte meridional My en Sv)
#K2


#dimensionalizo funcion corriente, considero dimensiones tipicas de modelo_oceanico
psiF_2_dim=psiF_2*U*L #funcion corriente dimensionalizada (dimension m*m/s)

#ploteo funcion corriente k2
plt.figure()
plt.contourf(X_2,Y_2,psiF_2_dim,levels_psi)
plt.title("Campo de funcion corriente k2")
plt.colorbar()
plt.savefig("1b funcion corriente k2", npi=100)

#calculo transporte meridional k2
My_2=D*(np.diff(psiF_2_dim,n=1, axis=1))/1e6 

#ploteo transporte meridional k2
plt.figure()
plt.contourf(X_2[0:199],Y_2,My_2,levels_my)
plt.title("Campo de transporte meridional k2")
plt.colorbar()
plt.savefig("1b transporte meridional k2", npi=100)

#%% ejercicio 1b (campo defuncion corriente + campo de transporte meridional My en Sv)
#K3

#dimensionalizo funcion corriente
#considero dimensiones tipicas de modelo_oceanico
psiF_3_dim=psiF_3*U*L # funcion corriente dimensionalizada (dimension m*m/s)

#ploteo funcion corriente k3
plt.figure()
plt.contourf(X_3,Y_3,psiF_3_dim,levels_psi)
plt.title("Campo de funcion corriente k3")
plt.colorbar()
plt.savefig("1b funcion corriente k3", npi=100)

#calculo transporte meridional k3
My_3=D*(np.diff(psiF_3_dim,n=1, axis=1))/1e6 

#ploteo transporte meridional k3
plt.figure()
plt.contourf(X_3[0:199],Y_3,My_3,levels_my)
plt.title("Campo de transporte meridional k3")
plt.colorbar()
plt.savefig("1b transporte meridional k3", npi=100)

#%% Ejercicio 1c (transporte meridional My [sv] en la latitud central de la cuenca vs distancia [km]+
#vorticidad relativa [s-1] vs distancia [km])

#transporte meridional 
plt.figure()
plt.plot(X[0:199],My[50,:], label="k1") 
plt.plot(X_2[0:199],My_2[50,:], label="k2")
plt.plot(X_3[0:199],My_3[50,:], label="k3")
plt.xlabel("distancia [km]")
plt.ylabel("transporte meridional [sv]")
plt.title("Transporte meridional en la latitud central de la cuenca")
plt.legend()
plt.savefig("1c transporte meridional", dpi=100)

#vorticidad
##dimesionalizo vorticidad
vortF_dim=vortF*U/L
vortF_2_dim=vortF_2*U/L
vortF_3_dim=vortF_3*U/L
##ploteo
plt.figure()
plt.plot(X[0:200],vortF_dim[50,:], label="k1") 
plt.plot(X[0:200],vortF_2_dim[50,:], label="k2") 
plt.plot(X[0:200],vortF_3_dim[50,:], label="k3") 
plt.xlabel("distancia [km]")
plt.ylabel("vorticidad relativa [s-1]")
plt.title("Vorticidad relativa en la latitud central de la cuenca")
plt.legend()
plt.savefig("1c vorticidad relativa", dpi=100)

#%% Ejercicio 2
#K1
My_central=My[50,:] #latitud numero 50
np.where(My_central==0) #longitud 22 donde termina el borde oeste en array (donde el transporte meridional se hace positivo)
My_borde_oeste_suma=np.sum(My_central[0:22]) #en sv
My_total_suma=np.sum(My_central) #en sv
extension_borde_oeste=np.sum(X[0:22])*20 #en m 
#K2
My_2_central=My_2[50,:]
np.where(My_2_central==0) #longitud 46 y 49 ( elijo 49 )donde termina el borde oeste en array (donde el transporte meridional se hace positivo)
My_2_borde_oeste_suma=np.sum(My_2_central[0:49]) #en sv
My_2_total_suma=np.sum(My_2_central) #en sv
extension_borde_oeste_2=np.sum(X[0:49])*20 #en m 
#K3
My_3_central=My_3[50,:] #latitud numero 50
np.where(My_3_central==0) #longitud 60,62,64,66 (elijo 66) donde termina el borde oeste en array (donde el transporte meridional se hace positivo)
My_3_borde_oeste_suma=np.sum(My_3_central[0:66]) #en sv
My_3_total_suma=np.sum(My_3_central) #en sv
extension_borde_oeste_3=np.sum(X[0:66])*20 #en m 

#acomodo informacion en tabla devuelve archivo excel
import pandas as pd
resultados2= {' ': ["Transporte meridional borde oeste [sv]","Transporte meridional total [sv]","Extension borde oeste [m]"],
     "K1":[round(My_borde_oeste_suma),round(My_total_suma),extension_borde_oeste],
     'K2':[round(My_2_borde_oeste_suma),round(My_2_total_suma),extension_borde_oeste_2],
     "K3":[round(My_3_borde_oeste_suma),round(My_3_total_suma),extension_borde_oeste_3]}
resultados2 = pd.DataFrame(data=resultados2)
resultados2.to_excel("resultados_2.xls",index=False)

#%% 3 con k1
ds=0.05
#primer termino
primer_termino=((np.diff(psiF,n=1, axis=1)))[50,:] /ds #este es el que tuvo que tirar magia dani con ese ds que viene del .dat (gridstep)
segundo_termino=-QG_curlw[51,:]
tercer_termino=0.29*vortF[50,:]
plt.figure(33)
plt.plot(primer_termino,"r", label='Primer Termino')
plt.plot(segundo_termino,"b", label= 'Segundo Termno')
plt.plot(tercer_termino,"g", label ='Tercer Termino' )
plt.legend()
plt.savefig("EJERCICIO3", dpi=100)


#%%4
#se piensa conceptualmente