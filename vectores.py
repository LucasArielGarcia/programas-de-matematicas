import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
def restar():
    vec1 = []
    vec2 = []
    c = int(input('vec r2 o r3 '))

    for i in  range(c):
        ingreso = int(input('ingrese el numero del vector'))
        vec1.append(ingreso)
    for  i  in range(c):
        ingreso = int(input('ingrese el numero del vector'))
        vec2.append(ingreso)

    for i in range (c):
        vec1[i] = vec1[i] - vec2[i]

    resultado = vec1
    print(resultado)

def sumar():
    vec1 = []
    vec2 = []
    c = int(input('vec r2 o r3 '))

    for i in  range(c):
        ingreso = int(input('ingrese el numero del vector'))
        vec1.append(ingreso)
    for  i  in range(c):
        ingreso = int(input('ingrese el numero del vector'))
        vec2.append(ingreso)

    for i in range (c):
        vec1[i] = vec1[i] + vec2[i]

    resultado = vec1
    print(resultado)

def modulo():
    vec1 = []
    suma = 0
    c = int(input('ingrese r2 o r3 : '))
    for i in  range(c):
        ingreso = int(input('ingrese el numero del vector'))
        vec1.append(ingreso)
        
    for i in range (c):
        vec1[i] = vec1[i] ** 2
        
    suma = sum(vec1)
    print('poner en la calculadora raiz de ',suma)

def graficar2D():
    x = []
    y = []
    c = int(input('cuantas lineas quiere hacer?'))
    for i in range(c):
        agx = int(input('agregar x '))
        x.append(agx)
    for i in range(c):  
        agy = int(input('agregar y '))
        y.append(agy)   
        
    for i in range(c):
        plt.quiver(x[i],y[i],scale_units='xy', angles='xy',  scale=1)
        plt.axvline(x[i], alpha=0.2, linestyle='--')
        plt.axhline(y[i], alpha=0.2, linestyle='--')
            
    plt.axvline(x=0)
    plt.axhline(y=0)
    plt.xlim(0,agx+5)
    plt.ylim(0,agy+5)
    plt.show()

def graficar3D():
    fig = plt.figure()
    ax =plt.axes(projection = '3d')
    z = [0]
    y = [0]
    x = [0]
   
    agx = int(input('agregar x '))
    x.append(agx)
    agy = int(input('agregar y '))
    y.append(agy)   
    agz = int(input('agregar y '))
    z.append(agz)
    ax.plot3D(x,y,z, 'gray')
    plt.show()
    

def matrices(): # que no hace la cuenta 
    vec1 = []
    vec2 = []
    for i in range(3):
        ag =int(input('aregar numero del vec1: '))
        vec1.append(ag)
        
    for i in range(3):
        ag =int(input('aregar numero del vec2: '))
        vec2.append(ag)
    r = [(vec1[1]*vec2[2] - vec2[1]* vec1[2]),-(vec1[0]*vec2[2] - vec2[0]* vec1[2]),(vec1[0]*vec2[1] - vec2[0]* vec1[1])]
    print(r)

def paralelas():
    vec1 = []
    vec2 = []
    for i in  range(3):
            ingreso = int(input('ingrese el numero del vector'))
            vec1.append(ingreso)
    for  i  in range(3):
        ingreso = int(input('ingrese el numero del vector'))
        vec2.append(ingreso)
    try:
        res1 = vec1[0]/vec2[0]
    except:
        res1 = 0
    try:
        res2 = vec1[1]/vec2[1]
    except:
        res2 = 0
    try:
        res3 = vec1[2]/vec2[2]
    except:
        res3 = 0

    print ("x=",res1, " y = ",res2, "z = ",res3)


# ------ progama proncipal -----------
opcion = int(input('elija opcion, 1 restar, 2 sumar, 3 modulo, 4 graficar en 2D, 5 para graficar en 3D, 6 para matrices, 7 paralelas. -1 para salir'))

while opcion != -1:
    if opcion == 1:
        restar()
    elif opcion == 2:
        sumar()
    elif opcion == 3:
        modulo()
    elif opcion == 4:
        graficar2D()
    elif opcion == 5:
        graficar3D()

    elif opcion == 6:
        matrices()
    elif opcion == 7:
        paralelas()
    opcion = int(input('elija opcion, 1 restar, 2 sumar, 3 modulo, 4 graficar en 2d,5 para graficar en 3D, 6 para matrices, 7 paralelas. -1 para salir'))
        
