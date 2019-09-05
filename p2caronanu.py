#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:02:56 2019

@author: macbookair
"""
#%%

#Hola Nanus, en los graficos de funcion corriente y campo de vorticidad dividi a los X y X_1 por 1000 a lo cabeza para que en los plots quede en km que me parece mas lindo y no modifica 
# en nada a los resultados. 
#respecto al ej 1 no tengo mas nada que decir. La verdad es que cuando llega al estado estacionario tiene esas variaciones locas que para mi son por como esta planteado el termino de friccion, que ahora es lateral
# lo que se me ocurre es que al ser friccion lateral en el estado estacionario hay friccion entre las aguas de mas velocidad y menos veocidad pero no se si esta bien el razonamiento. Igual nada podesmo tirar esto como hipotesis
# y ver que nos dicen. La idea de discutir todos va de la mano a que nos digan que carajo pasa jajaj

#Respecto al ej dos la idea supongo que es que cuanto menos friccion tenes, mas velocidades agarra el tipo y mas tarda en llegar a quedar estacionario. Me parece curioso que cuando estabamos corriendo los modelos paso al reves, mas friccion mas tardaba el tipo en darnos el resultado. que habiamos pensado ahi?

#Respecto a los graficos de vorticidad en realidad en la P1 nos queda del mismo orden de magnitud solo que si te fijas en la barra aclara que son esos numeros por e-7. Por eso multiplique a la vortF_dim y a levels_vort por e7
# primero para quw nos quede comparable y segundo porque me parece visualmente mas lindo tener esos valores. Aun asi varia la vort en uno o dos ordenes de magnitud entre los modelos. Pero tene encuenta que no solo cambia la consepcion de la friccion si no tambien la magnitud de la misma
# asi que no me calentaria tanto en comparar esas cosas. Me parece que la comparacin copada se hace en terminos de la funcion corriente, donde en el modelo de Munk aparecen contracorrientes que en el modelo de Svedrup no. 

#Del ej 4 el analisis es el mismo que en la P1. MAs velocidad mas transporte mas se achica no?

#Idem de la P1 el analisis tamnien. La vorticiad compensa la Funcion ocrriente y es0.

#como comentario general me encantan los loops. Hace del script mucho mas lindo y los graficos estan chetisimos para mi. Somos todo un exito NAduuuuu


#Hola Caro, esto es lo que hice y las dudas que tengo de cada ejercicio

#Cargo datos. Puse la ruta de cada una asi no tenemos que andar escribiendo y copiando y pegando y bla, asique deshashtagea tu ruta, hashtagea
#la mia y listo, entra a tu carpeta. Ademas ya no es necesario que te pares en a ruta manualmente para trabajar, el script ya lo hace
#mi sol en virgo no me dejaba tener todas las cosas cargadas con _2 _3 _4 _5 y que no hubiera _1 asique se lo agregue 

#1. Estaba hermoso, no hice nada. Escribi como lo interpreto, dirias algo mas?

#2. Bueno comente todo en el codigo, estaba super lo que habias hecho o sea cumplia con la condicion de la consigna, pero esa condicion
#que nos soplaba la consigna no llegaba a lo que queriamos. Esta todo detallado y los resultados se presentan en un grafico con etiqueta
#en el salto temporal en el que se estabiliza, aunque sigue siendo medio cabeza como lo calculo, fijate que para la S5 queda medio raro, 
#pero para mi podemos presntar esto y de ultima preguntamos el viernes que onda.  Otra cosa, preferi entrar en un loop a lo tash sultana 
#que copiar y pegar, pero por si te perdes (a mi me suele suceder con los ciclos) te deje comentado el razonamiento para una de las simulaciones
#aislada 

#3. 
#Amo como lograste los contourf. Le agregue isolinea de cero. y los meti en un loop 

# En la practica anterior nos quedo 7 (o 6 no me acuerdo)
# ordenes de magnitud mayor que al resto, por ahi
#creo que esto fue porque pusimos L en km y lo deberiamos haber puesto en metros (lo 
#cambie para plotearlos aca, fijate que te parece asi corrijo la practica 1)
#habria que comparar con lo que le quedo al resto a ver que onda



#4 
#ya estaba hermoso!
#quise meterlo en un loop y se me complico. Por ahi en estos dias lo logro. 
#igual esto es solo para calmar mi sol en virgo (una vez mas)


#5
#solo agregue que significaba cada termino


#pendientes (esto lo puedo hacer yo vos hiciste banda!)
#1) verificar que este ok el 3
#2) verificar los plots que rehice de la practica 1 para que sean comparables con esta.
#Esto lo hice poniendo L en metros. Comparar lo que le dio al resto

#hacer la PP


#%%
#Hola nanusss, estive jugando un rato con los estilos del counturf. Por un lado podes cambiarle el estilo con el comando  plt.style.use('estilo') y podes ver los que hay en el siguiente
#link  https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html lo que hace es cambiarte el fondo y tener colores tipicos por defoult. Manteniendo el estilo tambien 
#podes cambiar los colores  importanto from matplotlib import cm y usas el comando cmap=cm.jet donde jet es ejemplo y en el link ves todas las opciones 
# https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html. 

#EL ej 2 no iba porque era lista y el np.where funciona con float(hasta que me di cuenta pasaron las elecciones ). Lo pase pero igual estan mal las condiciones porque el minimo valor es cero y estamos buscando un valor mayor a 1 que tambien sea cero. Lo hice desde esta
#otra manera que me funciona para la 1 pero nme queda lupeando eternamente para los otros. Yo ya estoy quemada si se te ocurre algo bien si no manana sera otro dia
#en los campos de vorticidad queda mucha diferencia entre las simulaciones que cuando le metes una barra unificada para poder comparar no se ve. Dani dice que hay mucha dif pero tambien dice que no le parece que el codigo este mal asi que no se. Abra que ver que les da al resto y ver que onda.
#Despues  en el 5to lo consulte con dani y habia que tirar de nuevo la magia del ds


#%% cargo librerias
import numpy as np
import os #para setear directorio desde el codigo
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
#%%cargo las salidas del modelo para las 5 simulaciones con la funcion cargar dentro de Cargar2.py
#ruta="/home/nadia/Documentos/materias/circulaciongeneral/practica2/modelo_QG/" #ruta NANU
ruta="/Users/macbookair/Desktop/practicasCG/practica2/modelo_QG/" #ruta CARO
os.chdir(ruta)
from Cargar2 import cargar 
psi_temp_1,vort_temp_1,psiF_1,vortF_1,QG_diag_1,QG_curlw_1,X_1,Y_1,dx_1,dy_1=cargar(ruta+"out_tmp_s1/",1000000,500000,100,50)
psi_temp_2,vort_temp_2,psiF_2,vortF_2,QG_diag_2,QG_curlw_2,X_2,Y_2,dx_2,dy_2=cargar(ruta+"out_tmp_s2/",1000000,500000,100,50)
psi_temp_3,vort_temp_3,psiF_3,vortF_3,QG_diag_3,QG_curlw_3,X_3,Y_3,dx_3,dy_3=cargar(ruta+"out_tmp_s3/",1000000,500000,100,50)
psi_temp_4,vort_temp_4,psiF_4,vortF_4,QG_diag_4,QG_curlw_4,X_4,Y_4,dx_4,dy_4=cargar(ruta+"out_tmp_s4/",1000000,500000,100,50)
psi_temp_5,vort_temp_5,psiF_5,vortF_5,QG_diag_5,QG_curlw_5,X_5,Y_5,dx_5,dy_5=cargar(ruta+"out_tmp_s5/",1000000,500000,100,50)

#%% ejercicio 1
#Grafique la energia cinetica total de la cuenca (adimensional) en funcion del numero de iteracion temporal para cada simulacion (en un mismo grafico).
#tomo la cuarta columna de la salida QG_diag que tiene la energia cinetica para cada paso temporal (10000 pasos) en el punto central del dominio
plt.figure()
plt.plot()
plt.plot(QG_diag_1[:,0],QG_diag_1[:,3],label="S1")
plt.plot(QG_diag_2[:,0],QG_diag_2[:,3],label="S2")
plt.plot(QG_diag_3[:,0],QG_diag_3[:,3],label="S3")
plt.plot(QG_diag_4[:,0],QG_diag_4[:,3],label="S4")
plt.plot(QG_diag_5[:,0],QG_diag_5[:,3],label="S5")
plt.xlabel("Paso temporal")
plt.ylabel("Energia cinetica")
plt.title("Evolucion de energia cinetica total")
plt.legend(loc='upper right')
plt.savefig("ejercicio1", dpi=100)

#A que se deben las diferencias?
#cuando menor es el coeficiente de friccion lateral, o sea cuando menor es la friccion, mas energia
#cinetica tendra asociada la simulacion. A demas (quizas sea por la escala, planteo duda) varia
#mucho mas una vez "estabilizado". Y a demas (aunque despues se ve en maor detalle) tarda mas en 
#estabilizarse la simulacion con menor friccion. 
#Esto se debe a que a menor friccion, menor disipacion habra y las velocidades inducidas por
#el viento seran mayores, reflejandose en una mayor energia cinetica
#Notar que, aunque el coeficiente de friccion lateral cambia linealmente de una simulacion a otra,
#la relacion entre las energias cineticas de las simulaciones no es lineal (podria ser logaritmica o
#exponencial inversa  

#%% Ejercicio 2
#Calcule para cada simulacion el numero de iteraciones necesario para alcanzar el estado estacionario.

#Queremos ver cuando se estabiliza el modelo
Ec1=QG_diag_1[:,3]
Ec2=QG_diag_2[:,3]
Ec3=QG_diag_3[:,3]
Ec4=QG_diag_4[:,3]
Ec5=QG_diag_5[:,3]


#lo que hizo caro caso S1:
#k1=0
#while abs(((Ec1[-1]-Ec1[k1])/Ec1[-1])*100)>=1: #0.008 nda ok para lo que queremos
 #   k1=k1+1 #k1  corresponde al paso a partir del cual la el cociente de energia cinetica se hace menor a 1 (como lo pide el enunciado)
    
#esto esta super hermoso pensado y cumple con la condicion de la consigna

#pero la condicion de la consigna no verifica lo que queremos que es ver a partir
#del cual esta estable (la condicion dada por la consigna nos lleva a ese pico a partir 
#del cual baja la energia cinetica "abruptamente"
#para estabilizarse),
    
#lo que podria hacer es ademas, imponer una condicion que indique que la diferencia con el paso
#siguiente. y los siguientes, no sea muy grande (justamente para evitar ese salto), y de esos tomo 
#el correspondiente al mas chico de todos 
#claramente si elijo justo el valor del paso temporal inmediatamente siguiente siemrpe
#van a estar cerca, asique pido que el valor de energia cinetica este cerca del 
#valor de energia cinetica correspondiente a cierta cantidad de pasos siguientes,
#arbitrariamente elijo a 10 pasos siguientes y veo graficamente que toma el punto que quiero

#esta es la logica: (para entender)
        
#kas1=[]
#for k in range(0,len(Ec1)-30):
#    if abs(((Ec1[-1]-Ec1[k])/Ec1[-1])*100) <1 and abs(((Ec1[k+10]-Ec1[k])/Ec1[k+10])*100)<1:
#        kas1.append(k)
#k1_est=min(kas1)
#print k1_est

#lo hago en un loop me canse de copiar y pegar 
Ec=[Ec1,Ec2,Ec3,Ec4,Ec5]
ind=["1","2","3","4","5"]
kas1=[]
kas2=[]
kas3=[]
kas4=[]
kas5=[]
kas=[kas1,kas2,kas3,kas4,kas5]
k_est=[]
plt.plot()
for i in range(0,5):
    for k in range(0,len(Ec1)-10):
        if abs(((Ec[i][-1]-Ec[i][k])/Ec[i][-1])*100) <1 and abs(((Ec[i][k+10]-Ec[i][k])/Ec[i][k+10])*100)<1:
         kas[i].append(k)
    k_est.append(min(kas[i])) #k en los que se estabiliza simulacion i+1 (s1) en posicion i (posicion 0 = elemento 1)
    plt.plot(Ec[i],label="S"+ind[i])
    plt.plot(k_est[i],Ec[i][k_est[i]],"ro")   
    plt.annotate(str(k_est[i]), (k_est[i],Ec[i][k_est[i]])) #agrego etiqueta con paso temporal
    plt.xlabel("Paso temporal")
    plt.ylabel("Energia cinetica")
    plt.title("Evolucion de energia cinetica total")
    plt.legend(loc='upper right')
    plt.savefig("ejercicio2", dpi=100)
print(k_est) #k en el que se estabiliza para cada simulacion 

#muestro resultados en tabla
simulacion=["s1","s2","s3","s4","s5"]
show_k_est=[simulacion,k_est]
resultados2=pd.DataFrame(data=show_k_est)
resultados2.to_excel("resultados_2.xls",index=False)



        
        
#%% Ej 3

levels_psi=np.arange(-800000,10000,10000) #vector de -350000 a 0 cada 10000
levels_vort=np.arange(-1e-5,3.5e-5,1e-6)
#levels_psiF=np.arange()

##defino magnitudes tipicas para dimensionalizar 
L=1000000 #longitud de la cuenca en METROS. practica 1 lo dimensionalizamos con L en km 
#(verificar que sea en metros y cambiarlo en practica 1). poniendo esto en metros la vorticidad
#nos queda razonable 
tau=0.3 #tension del viento en superficie
D=3000 #profundidad del oceano EN metros
rho=1025 #densidad
betha=1e-11 
U=2*np.pi*tau/(rho*D*betha*L) 

#
#dimensionalizo funciones corriente
psiF_1_dim=psiF_1*U*L # funcion corriente dimensionalizada (dimension m*m/s) S1
psiF_2_dim=psiF_2*U*L # funcion corriente dimensionalizada (dimension m*m/s) S2
psiF_3_dim=psiF_3*U*L # funcion corriente dimensionalizada (dimension m*m/s) S3
psiF_4_dim=psiF_4*U*L # funcion corriente dimensionalizada (dimension m*m/s) S4
psiF_5_dim=psiF_5*U*L # funcion corriente dimensionalizada (dimension m*m/s) S5
psiF_dim=[psiF_1_dim,psiF_2_dim,psiF_3_dim,psiF_4_dim,psiF_5_dim]

#dimensionalizo vorticidad 
vortF_1_dim=vortF_1*U/L 
vortF_2_dim=vortF_2*U/L 
vortF_3_dim=vortF_3*U/L 
vortF_4_dim=vortF_4*U/L 
vortF_5_dim=vortF_5*U/L 
vortF_dim=[vortF_1_dim,vortF_2_dim,vortF_3_dim,vortF_4_dim,vortF_5_dim]

#ploteo
X=[X_1/1000,X_2/1000,X_3/1000,X_4/1000,X_5/1000]
Y=[Y_1,Y_2,Y_3,Y_4,Y_5]
sim=["S1","S2","S3","S4","S5"]
#funcion corriente
for i in range(0,5):
    plt.figure()
    plt.contourf(X[i],Y[i],psiF_dim[i],levels_psi, cmap=cm.jet)
    plt.title("Campo de funcion corriente "+sim[i])
    cbar=plt.colorbar()
    plt.contour(X[i], Y[i],psiF_dim[i], levels=0,colors="white")
    cbar.ax.set_title("m2/s")
    plt.savefig("Funcion corriente "+sim[i], npi=100)
#vorticidad
for i in range(0,5):
    plt.figure()
    #multipli1ue a la vort poe e7 para que me quede en las mismas magnitudes la barra que en la P1 
    #plt.contourf(X[i],Y[i],vortF_dim[i],cmap=cm.jet) #para analizar cual es la escala mas grande 
    plt.contourf(X[i],Y[i],vortF_dim[i]*1e7,levels=levels_vort*1e7,cmap=cm.jet) #defino la escala mas arriba en funcion de lo que de el ploteo con la linea anterior descomentada
    cbar=plt.colorbar()
    plt.title("Campo de vorticidad "+sim[i])
    cbar.ax.set_title("1/s 1e-7")
    plt.contour(X[i], Y[i],vortF_dim[i], levels=0,colors="white")
    plt.savefig("Campo de vorticidad "+sim[i], npi=100)
    

#Hago los graficos analogos de practica 1 
######### practica 1 tengo cargo datos y todo aca pero despues habria que corregir directamente el script 1##########
psi_temp_1_1,vort_temp_1_1,psiF_1_1,vortF_1_1,QG_diag_1_1,QG_curlw_1_1,X_1_1,Y_1_1,dx_1_1,dy_1_1=cargar("/Users/macbookair/Desktop/practicasCG/Practica 1/Modelo_QG/out_tmp_1/",4000000,2000000,200,100)
psi_temp_1_2,vort_temp_1_2,psiF_1_2,vortF_1_2,QG_diag_1_2,QG_curlw_1_2,X_1_2,Y_1_2,dx_1_2,dy_1_2=cargar("/Users/macbookair/Desktop/practicasCG/Practica 1/Modelo_QG/out_tmp_2/",4000000,2000000,200,100)
psi_temp_1_3,vort_temp_1_3,psiF_1_3,vortF_1_3,QG_diag_1_3,QG_curlw_1_3,X_1_3,Y_1_3,dx_1_3,dy_1_3=cargar("/Users/macbookair/Desktop/practicasCG/Practica 1/Modelo_QG/out_tmp_3/",4000000,2000000,200,100)


#psi_temp_1_1,vort_temp_1_1,psiF_1_1,vortF_1_1,QG_diag_1_1,QG_curlw_1_1,X_1_1,Y_1_1,dx_1_1,dy_1_1=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica1/Modelo_QG/out_tmp_1/",4000000,2000000,200,100)
#psi_temp_1_2,vort_temp_1_2,psiF_1_2,vortF_1_2,QG_diag_1_2,QG_curlw_1_2,X_1_2,Y_1_2,dx_1_2,dy_1_2=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica1/Modelo_QG/out_tmp_2/",4000000,2000000,200,100)
#psi_temp_1_3,vort_temp_1_3,psiF_1_3,vortF_1_3,QG_diag_1_3,QG_curlw_1_3,X_1_3,Y_1_3,dx_1_3,dy_1_3=cargar("/home/nadia/Documentos/materias/circulaciongeneral/practica1/Modelo_QG/out_tmp_3/",4000000,2000000,200,100)

##defino magnitudes tipicas para dimensionalizar 
L_1=4000000 #longitud de la cuenca metros
tau_1=0.3 #tension del viento en superficie
D_1=3000 #profundidad del oceano EN metros 
rho_1=1025 #densidad
betha_1=1e-11 
U_1=2*np.pi*tau/(rho*D*betha*L) 

#dimensionalizo funciones corriente
psiF_1_1_dim=psiF_1_1*U_1*L_1 # funcion corriente dimensionalizada (dimension m*m/s) k1
psiF_1_2_dim=psiF_1_2*U_1*L_1 # funcion corriente dimensionalizada (dimension m*m/s) k2
psiF_1_3_dim=psiF_1_3*U_1*L_1 # funcion corriente dimensionalizada (dimension m*m/s) k1
psiF_1_1_2_3_dim=[psiF_1_1_dim,psiF_1_2_dim,psiF_1_3_dim]

#dimensionalizo vorticidad 
vortF_1_1_dim=vortF_1_1*U_1/L_1 
vortF_1_2_dim=vortF_1_2*U_1/L_1 
vortF_1_3_dim=vortF_1_3*U_1/L_1
vortF_1_1_2_3_dim=[vortF_1_1_dim,vortF_1_2_dim,vortF_1_3_dim] 

#ploteo
levels_psi_1=np.arange(-1400000,10000,10000)
levels_vort_1=np.arange(0,0.00000105,1e-8)
X_11=[X_1_1/1000,X_1_2/1000,X_1_3/1000]
Y_11=[Y_1_1,Y_1_2,Y_1_3]
sim_11=["K1","K2","K3"]
#funcion corriente
for i in range(0,3):
    plt.figure()
    #plt.contourf(X_11[i],Y_11[i],psiF_1_1_2_3_dim[i], cmap=cm.jet)
    plt.contourf(X_11[i],Y_11[i],psiF_1_1_2_3_dim[i],levels_psi_1, cmap=cm.jet)
    plt.title("Campo de funcion corriente "+sim_11[i])
    cbar=plt.colorbar()
    plt.contour(X_11[i], Y_11[i],psiF_1_1_2_3_dim[i], levels=0,colors="white")
    cbar.ax.set_title("m2/s")
    plt.savefig("Funcion corriente "+sim_11[i], npi=100)
#vorticidad
for i in range(0,3):
    plt.figure()
    #plt.contourf(X_11[i],Y_11[i],vortF_1_1_2_3_dim[i],cmap=cm.jet) #para analizar cual es la escala mas grande 
    plt.contourf(X_11[i],Y_11[i],vortF_1_1_2_3_dim[i],levels=levels_vort_1,cmap=cm.jet) #defino la escala mas arriba en funcion de lo que de el ploteo con la linea anterior descomentada
    cbar=plt.colorbar()
    plt.title("Campo de vorticidad "+sim_11[i])
    #cbar.ax.set_title("1/s")
    plt.contour(X_11[i], Y_11[i],vortF_1_1_2_3_dim[i], levels=0,colors="white")
    plt.savefig("Campo de vorticidad "+sim_11[i], npi=100)

##
#%% Ejercicio 4



#S1
My_1=D*(np.diff(psiF_1_dim,n=1, axis=1))/1e6
My_1_central=My_1[25,:] #latitud numero 25
cambio_1=np.where(My_1_central[:-1] * My_1_central[1:] < 0 )[0]  #(lugar 6 elemento 7) te da la primer longitud donde cambia de signo termina el borde oeste en array (donde el transporte meridional se hace positivo)
cambio_1=int(cambio_1)
cambio_1=cambio_1+1
My_1_borde_oeste_suma=np.sum(My_1_central[0:cambio_1]) #en sv hasta 
My_1_total_suma=np.sum(My_1_central) #en sv
extension_1_borde_oeste=np.sum(X_1[0:cambio_1])*20 #en m 

#S2
My_2=D*(np.diff(psiF_2_dim,n=1, axis=1))/1e6
My_2_central=My_2[25,:] #latitud numero 25
cambio_2=np.where(My_2_central[:-1] * My_2_central[1:] < 0 )[0]  #(5) te da la primer longitud donde cambia de signo termina el borde oeste en array (donde el transporte meridional se hace positivo)
cambio_2=int(cambio_2)
cambio_2=cambio_2+1
My_2_borde_oeste_suma=np.sum(My_2_central[0:cambio_2]) #en sv hasta 
My_2_total_suma=np.sum(My_2_central) #en sv
extension_2_borde_oeste=np.sum(X_1[0:cambio_2])*20 #en m 

#S3
My_3=D*(np.diff(psiF_3_dim,n=1, axis=1))/1e6
My_3_central=My_3[25,:] 
cambio_3=np.where(My_3_central[:-1] * My_3_central[1:] < 0 )[0]  #(4)Cambia en 4 14y 16. Elijo qudatme con 5
cambio_3=int(cambio_3[0])
cambio_3=cambio_3+1
My_3_borde_oeste_suma=np.sum(My_3_central[0:cambio_3]) #en sv hasta 
My_3_total_suma=np.sum(My_3_central) #en sv
extension_3_borde_oeste=np.sum(X_1[0:cambio_3])*20 #en m 


#S4
My_4=D*(np.diff(psiF_4_dim,n=1, axis=1))/1e6
My_4_central=My_4[25,:] 
cambio_4=np.where(My_4_central[:-1] * My_4_central[1:] < 0 )[0]  #(3)Cambia en 3 10 y 13. Elijo qudatme con 4
cambio_4=int(cambio_4[0])
cambio_4=cambio_4+1
My_4_borde_oeste_suma=np.sum(My_4_central[0:cambio_4]) #en sv hasta 
My_4_total_suma=np.sum(My_4_central) #en sv
extension_4_borde_oeste=np.sum(X_1[0:cambio_4])*20 #en m 

#S5
My_5=D*(np.diff(psiF_5_dim,n=1, axis=1))/1e6
My_5_central=My_5[25,:] 
cambio_5=np.where(My_5_central[:-1] * My_5_central[1:] < 0 )[0]  #(1)Cambia en 1 5 y 8. Elijo qudatme con 2
cambio_5=int(cambio_5[0])
cambio_5=cambio_5+1
My_5_borde_oeste_suma=np.sum(My_5_central[0:cambio_5]) #en sv hasta 
My_5_total_suma=np.sum(My_5_central) #en sv
extension_5_borde_oeste=np.sum(X_1[0:cambio_5])*20 #en m 


#acomodo informacion en tabla devuelve archivo excel
import pandas as pd
resultados4= {' ': ["Transporte meridional borde oeste [sv]","Transporte meridional total [sv]","Extension borde oeste [m]"],
     "S1":[round(My_1_borde_oeste_suma),round(My_1_total_suma),extension_1_borde_oeste],
     'S2':[round(My_2_borde_oeste_suma),round(My_2_total_suma),extension_2_borde_oeste],
     "S3":[round(My_3_borde_oeste_suma),round(My_3_total_suma),extension_3_borde_oeste],
     'S4':[round(My_4_borde_oeste_suma),round(My_4_total_suma),extension_4_borde_oeste],
     "S5":[round(My_5_borde_oeste_suma),round(My_5_total_suma),extension_5_borde_oeste]}

resultados4 = pd.DataFrame(data=resultados4)
resultados4.to_excel("resultados_4.xls",index=False)

#%% Ejercicio 5
from Laplaciano import Calc_del2
ds=0.1
primer_termino=((np.diff(psiF_1,n=1, axis=1)))[25,:]/(ds) #este es el que tuvo que tirar magia dani con ese ds que viene del .dat (gridstep)
segundo_termino=-QG_curlw_1[26,:]
tercer_termino=-(0.025)*Calc_del2(vortF_1,1)[25,:]/(ds**2)

plt.figure(33)
plt.plot(primer_termino,"r", label='Primer Termino')
plt.plot(segundo_termino,"b", label= 'Segundo Termno')
plt.plot(tercer_termino,"g", label ='Tercer Termino' )
plt.legend()
plt.savefig("EJERCICIO 5", dpi=100)


#primer termino: adveccion meridional de vorticidad planetaria
#segundo termino: rotor de la tension del viento
#tercer termino: vorticidad relativa dada por cortantes de velocidad inducidas por friccion lateral