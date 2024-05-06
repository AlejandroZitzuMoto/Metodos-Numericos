import numpy as np
import Raiz as rr

def Euler_Der(f, inter, y0,nptos = 5):
    '''
    Metodo de Euler hacia la derecha
    --------------------------------
    f: Funcion
    inter: Intervalo
    y0: Condición de frontera
    nptos: cantidad de puntos a evaluar
    '''
    h = (inter[1]-inter[0])/nptos
    xi = np.arange(nptos)*h
    yv = []
    yv.append(y0)
    for i in range(nptos-1):
        yj = yv[i] + h*f(xi[i+1],yv[i])
        yv.append(yj)
    return yv

def Euler_izq(f,xv, yo, mu = 1e-4,nptos = 10,k = False):
    '''
    Metodo de Euler hacia la izquierda
    --------------------------------
    f: Funcion
    xv: Intervalo
    yo: Condición de frontera
    mu: ditancia
    nptos: cantidad de puntos a evaluar
    k: para elegir entre dos formas
    '''
    h = (xv[1]-xv[0])/(nptos-1)
    x1 = xv[0] + np.arange(nptos)*h
    if k == True:
        yv = []
        yv.append(yo)
        for i in range(nptos-1):
            yj1 = yv[i]/(1-mu*h)
            yj1 = yv[i] + h*f(x1[i+1],yj1)
            yv.append(yj1)
    else:
        n = len(x1)
        yv = np.zeros(n)
        f2 = lambda x,y,z: z - y - h*f(x,z) 
        t = yo
        for i , xi in enumerate(x1):
            yv[i] = t
            z1 = lambda z: f2(xi,t,z)
            root = rr.raiz_biseccion([-1e5,1e5],z1,tol = 1e-6)[0]
            t = root
            
    return yv

def trapecio(f,xv,y0,nptos = 6):
    '''
    Metodo del trapecio
    ---------------------
    f: Función
    xv: Intervalo
    y0: Condición de frontera
    nptos: cantidad de puntos a evaluar
    '''
    h = (xv[1]-xv[0])/(nptos-1)
    x1 = xv[0] + np.arange(nptos)*h
    yv = np.zeros(len(x1))
    for i,x in enumerate(x1):
        yv[i] = y0
        k0 = h*f(x,yv[i])
        yj1 = yv[i] + h*f(x + 0.5*h,yv[i] + 0.5*k0)
        y0 = yj1
    return yv

def trapecio_disc(f,xv,y0,nptos = 6):
    '''
    Metodo del trapecio discreto
    ----------------------------
    f: función
    xv: intervalo
    y0: Condicion de frontera
    nptos: cantidad de puntos a evaluar
    '''
    h = (xv[1]-xv[0])/(nptos-1)
    x1 = xv[0] + np.arange(nptos)*h
    yv = np.zeros(nptos)
    f2 = lambda x,y,z: z - yv[i] - h*f(x + 0.5*h, (yv[i]+z)/2)
    for i,x in enumerate(x1):
        yv[i] = y0
        z1 = lambda z: f2(x,y0,z)
        root = rr.raiz_biseccion([-1e10,1e10],z1)[0]
        y0 = root 
    return yv

def Runge_kutta(f,xv,y0,nptos = 6):
    '''
    Metodo de Runge kutta
    ---------------------
    f: función
    xv: intervalo
    y0: Condicion de frontera
    nptos: cantidad de puntos a evaluar
    '''
    h = (xv[1]-xv[0])/(nptos-1)
    x1 = xv[0] + np.arange(nptos)*h
    yv = np.zeros(nptos)
    for i,x in enumerate(x1):
        yv[i] = y0
        k0 = h*f(x,y0)
        k1 = h*f(x + 0.5*h, y0 + 0.5*k0)
        k2 = h*f(x + 0.5*h, y0 + 0.5*k1)
        k3 = h*f(x + h, y0 + k2)
        y0 = y0 + (1/6)*(k0 + 2*k1 + 2*k2 + k3)
    return yv
