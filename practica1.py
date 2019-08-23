#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:49:55 2019

@author: nadia
"""
import numpy as np
from matplotlib import pyplot as plt

#cargo con k1
from Cargar2 import cargar
psi_temp,vort_temp,psiF,vortF,QG_diag,QG_curlw,X,Y,dx,dy=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica1/Modelo_QG/out_tmp_1/",4000,2000,200,100)
psi_temp_2,vort_temp_2,psiF_2,vortF_2,QG_diag_2,QG_curlw_2,X_2,Y_2,dx_2,dy_2=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica1/Modelo_QG/out_tmp_2/",4000,2000,200,100)
psi_temp_3,vort_temp_3,psiF_3,vortF_3,QG_diag_3,QG_curlw_3,X_3,Y_3,dx_3,dy_3=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica1/Modelo_QG/out_tmp_3/",4000,2000,200,100)

#%%
###ejercicio 1a
plt.figure(1)
plt.plot(QG_diag[:,0],QG_diag[:,3],label="k1")
plt.plot(QG_diag_2[:,0],QG_diag_2[:,3],label="k2")
plt.plot(QG_diag_3[:,0],QG_diag_3[:,3],label="k3")
plt.xlabel("paso temporal")
plt.ylabel("energia cinetica")
plt.title("Ejercicio 1 a")
plt.legend()
plt.savefig("ejercicio1a")

#%%
###ejercicio 1b
####k1

#dimencionalizo funcion corriente
#considero dimensiones tipicas de modelo_oceanico
tau=0.3
D=3000
rho=1025
betha=1e-11
U=2*np.pi*tau/(rho*D*betha*L)
psiF_dim=psiF*U*L #dimension m*m/s

#ploteo funcion corriente k1
plt.figure(2)
plt.contourf(X,Y,psiF_dim)
plt.title("Campo de funcion corriente k1 (ej1b)")
plt.colorbar()
plt.savefig("1b funcion corriente k1")

#calculo transporte meridional k1
My=D*(np.diff(psiF_dim,n=1, axis=1))/1e6 #paso a Sv

#ploteo transporte meridional k1
plt.figure(3)
plt.contourf(X[0:199],Y,My)
plt.title("Transporte meridional k1 (ej1b)")
plt.colorbar()
plt.savefig("1b transporte meridional k1")

#%%
###ejercicio 1b
####k2

#dimencionalizo funcion corriente
#considero dimensiones tipicas de modelo_oceanico
psiF_2_dim=psiF_2*U*L #dimension m*m/s

#ploteo funcion corriente k2
plt.figure(4)
plt.contourf(X_2,Y_2,psiF_2_dim)
plt.title("Campo de funcion corriente k2 (ej1b)")
plt.colorbar()
plt.savefig("1b funcion corriente k2")

#calculo transporte meridional k2
My_2=D*(np.diff(psiF_2_dim,n=1, axis=1))/1e6 #paso a Sv

#ploteo transporte meridional k2
plt.figure(5)
plt.contourf(X_2[0:199],Y_2,My_2)
plt.title("Transporte meridional k2 (ej1b)")
plt.colorbar()
plt.savefig("1b transporte meridional k2")

#%%
###ejercicio 1b
####k3

#dimencionalizo funcion corriente
#considero dimensiones tipicas de modelo_oceanico
psiF_3_dim=psiF_3*U*L #dimension m*m/s

#ploteo funcion corriente k3
plt.figure(6)
plt.contourf(X_3,Y_3,psiF_3_dim)
plt.title("Campo de funcion corriente k3 (ej1b)")
plt.colorbar()
plt.savefig("1b funcion corriente k3")

#calculo transporte meridional k3
My_3=D*(np.diff(psiF_3_dim,n=1, axis=1))/1e6 #paso a Sv

#ploteo transporte meridional k3
plt.figure(7)
plt.contourf(X_3[0:199],Y_3,My_3)
plt.title("Transporte meridional k3 (ej1b)")
plt.colorbar()
plt.savefig("1b transporte meridional k3")

#%%PENDIENTES EJERCICIO 1B
#Poner las mismas barras para poder compararlos


#%% 1c
plt.plot(X[0:199],My[50,:]) #eje x distancia en y en km x transporte meridional en latitud numero 50


#dimesionalizo vorticidad
vortF_dim=vortF*U/L

#repito grafico anterior pero con vorticidad


#%% 2
My_central=My[50,:] #latitud numero 50
np.where(My_central==0) #longitud 22 donde termina el borde oeste en array

My_borde_oeste_suma=np.sum(My_central[0:22])

My_total_suma=np.sum(My_central)

extension_borde_oeste=np.sum(X[0:22])*20

#%% 3 con k1
ds=0.05
#primer termino
primer_termino=((np.diff(psiF,n=1, axis=1)))[50,:] /ds #este es el que tuvo que tirar magia dani con ese ds que viene del .dat (gridstep)
segundo_termino=-QG_curlw[51,:]
tercer_termino=0.29*vortF[50,:]
plt.figure(33)
plt.plot(primer_termino,"r")
plt.plot(segundo_termino,"b")
plt.plot(tercer_termino,"g")
legend()

#%%4
#se piensa conceptualmente
#%%HACER
###terminar los ejercicios, mejorar figuras y tamanios, armar presentacion para que se presente
###escribir concluciones luego de discucion 


