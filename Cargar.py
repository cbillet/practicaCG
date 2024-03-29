#%%
"""
Función para levantar las salidas del modelo QG_barotrop.f

Leandro Díaz
2018
"""

#%%

""" 

Para utilizarlo agregar en el script es necesario definir todos los inputs y correr las siguientes dos líneas

from Cargar import cargar
psi_temp,vort_temp,psiF,vortF,QG_diag,QG_curlw,X,Y,dx,dy=cargar(dir_salida,Lx,Ly,nx,ny)

Extraccion de los datos de salida del modelo

INPUTS
dir_salida: str, direccion de la salida #entre comillas "ruta a carpeta out_temp"
Lx: float, tamano de la cuenca (direccion X) #4000 dimension de la cuenca en kilometros lo que devuelve va a ser kilometros si lo pongo en metros me devuelve en metros
Ly: float, tamano de la cuenca (direccion Y) #2000 dimension de la cuenca en kilometros o metros dependiendo de como quiero la salida
nx: int, numero de punto de grilla (direccion X) #200
ny: int, numero de punto de grilla (direccion Y) #100

OUTPUTS
psi_temp: Campos de función de corriente de todos los tiempos # dimension: 200 en x x 100 en y x 20 tiempos
vort_temp: Campos de vorticidada de todos los tiempos # dimension: 200 en x x 100 en y x 20 tiempos
psiF: Campo de función de corriente del tiempo final # dimension: 200 en x x 100 en y x 1 tiempo (el ultimo)
vortF: Campo de vorticidad del tiempo final # dimension: 200 en x x 100 en y x 1 tiempo (el ultimo)
QG_diag: Información temporal de función corriente, vorticidad y energía cinética en el punto central del dominio (2000 pasos temporales x 5 columnas)
QG_curlw: Campo del rotor del esfuerzo del viento utilizado en la simulación #dim matriz de 200 en x x 100 en y
X: Vector con los puntos del eje X dimensionalizado  #vector que se genera de 0 hasta la dimension zonal (Lx) poniendole la cantidad de numeros que tengo en los puntos de grilla en x
Y: Vector con los puntos del eje Y dimensionalizado 
dx: Distancia entre puntos del eje X
dy: Distancia entre puntos del eje y

"""
def cargar(dir_salida,Lx,Ly,nx,ny): 

    #Cargamos las librerias necesarias
    import os
    import numpy as np

    archivos=os.listdir(dir_salida) # nombre de los archivos en el directorio actual + \output

    tiempos=0

    for name in archivos:
        if name[0:3]=='psi':
            tiempos=tiempos+1

    # Creacion de las matriz para recibir los datos
    psi_temp=np.empty(shape=[ny+2,nx+2,tiempos])
    psi_temp[:]=np.nan
    vort_temp=np.empty(shape=[ny+2,nx+2,tiempos])
    vort_temp[:]=np.nan
         
    # Extraccion
    for name in archivos:
        if name[0:3]=='psi':
            k1=name[3]+name[4]
            psi_temp[:,:,int(k1)-1]=np.loadtxt(dir_salida+name) #fromfile(name)
        if name[0:3]=='vor':
            k2=name[3]+name[4]
            vort_temp[:,:,int(k2)-1]=np.loadtxt(dir_salida+name) #fromfile(name)
        if name[0:7]=='QG_diag':
            QG_diag=np.loadtxt(dir_salida+name) #fromfile(name) 
            # En el punto central del dominio
            # (Tiempo, Funcion Corriente,Vorticidad, EnCin)
        if name[0:7]=='QG_wind':
            QG_curlw=np.loadtxt(dir_salida+name) #fromfile(name)
 
    # Recorte de los datos
    a1=1; a2=np.size(vort_temp,0)-1;
    b1=1; b2=np.size(vort_temp,1)-1;

    psi_temp=psi_temp[a1:a2,b1:b2,:]
    psiF=psi_temp[:,:,np.size(psi_temp,2)-1]

    vort_temp=vort_temp[a1:a2,b1:b2,:]
    vortF=vort_temp[:,:,np.size(vort_temp,2)-1]

    X=np.linspace(0,Lx,num=nx)
    Y=np.linspace(0,Ly,num=ny)    

    dx=Lx/(nx-1);
    dy=Ly/(ny-1);
    
    return psi_temp,vort_temp,psiF,vortF,QG_diag,QG_curlw,X,Y,dx,dy
    