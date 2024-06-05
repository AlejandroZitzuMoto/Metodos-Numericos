import numpy as np
import Librerias.Raiz as rr

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

def rk4vectorial(f,x,y0, nptos= 50):
    '''
    rk4 vectorial
    ---------------------
    f: función vectorial
    x: intervalo
    y0: Vector de condiciones de frontera
    nptos: numero de puntos
    '''
    n = len(y0)
    yf = np.zeros([nptos,n])
    h = (x[-1]-x[0])/(nptos-1)
    xv = x[0] + np.arange(nptos)*h
    for i,xi in enumerate(xv):
        yf[i,:] = y0
        k0 = h*f(xi,y0)
        k1 = h*f(xi + 0.5*h, y0 + 0.5*k0)
        k2 = h*f(xi + 0.5*h, y0 + 0.5*k1)
        k3 = h*f(xi + h, y0 + k2)
        y0 = y0 + (k0 + 2*k1 + 2*k2 + k3)/6
    return xv, yf

def rk4vect_arg(f,x,y0,arg = None, nptos = 50):
    '''
    Funcion rk4vectorial
    -----------------------
    f: función vectorial
    x: intervalo 
    y0: Vector de condiciones de frontera
    arg: contantes de la función
    nptos: Cantidad de puntos
    '''
    if arg:
        f1 = lambda x, yv: np.array(f(x,yv, *arg))
    else:
        f1 = lambda x, yv: np.array(f(x, yv))
    xv, yv = rk4vectorial(f1,x,y0)
    
    return xv, yv

def shoot(f,x,yf,s,y0,arg = None, nptos = 50):
    '''
    Metodo para encontrar las condiciones de frontera en el ultimo punto
    ---------------------------------------------------------------------
    f: Funcion vector
    x: intervalo
    yf: valor final de frontera
    y0: vector de condiciones de frintera donde se integra la derivada
    arg: constantes de la función
    nptos: numero de puntos
    '''
    s,y0 = y0v
    _, yv = rk4vect_arg(f,x,y0v,arg = arg, nptos = nptos)
    return yv[-1,0]-yf

def shooting(f,x,y0,yf,arg,nptos = 50, inter = [-1e12,1e12]):
    '''
    la condición de fronera final y(b)
    -------------------------
    f: Función
    x: Intervalo
    y0: condicion de frontera
    yf: Valor final
    arg: contantes de la función
    nptos: Numero de puntos:
    inter: intervalo para encontrar vaolor de la derivada
    '''
    s ,y0v = y0
    f2 = lambda s: shoot(f,x,yf,s,y0,arg,nptos)
    ydrv = rr.raiz_secante1(inter,f2)
    return ydrv

def matriz(data, info=False):
    '''
    Crear los valores
    data: Valores de entrada
    salida: Devuelve la matriz A, vector bs, valores para x 
    '''
    a, b, b0, bf, npt = data
    h = (b-a)/(npt-1)
    xi = a + np.arange(npt)*h
    
    # creando alpha, beta, gamma discretos
    denom = (1-xi**2)
    alphaj = 1 + h*xi/denom
    betaj = -2 + 30*h**2/denom
    gamma = 1 - h*xi/denom
    
    # Creando la matriz de dimensión n x n
    A = np.zeros((npt, npt))
    np.fill_diagonal(A[:, :], betaj)  # recordar que no incluye el x_0
    np.fill_diagonal(A[1:-1, :], alphaj[1:])  # recordar que no incluye el x_0
    np.fill_diagonal(A[1:, 2:], gamma[1:])  # recordar que no incluye el x_0
    A[0, 0] = 1
    A[-1,-1] = 1
    
    # creando vector B
    bs = np.zeros(npt)
    bs[0] = b0
    bs[-1] = bf
    
    if info:
        print(alphaj[1], betaj[1], gamma[1])
        print(alphaj[-2], betaj[-2], gamma[-2])
        print(A)

    return A, bs, xi
    
def matriz2(data, info=False, q=1.5):
    a, b, npt = data
    h = (b-a)/(npt-1)  # h = 2*np.pi/npt equivale a tomar a=0, b=2pi, npt-1=N
    xi = a + np.arange(npt)*h  # np.arange(npt)*h
    
    # creando alpha, beta, gamma discretos
    alphaj = -2-2*h**2*q*np.cos(2*xi)
    
    # Creando la matriz de dimensión n x n
    A = np.zeros((npt, npt))
    np.fill_diagonal(A[:, :], alphaj)  # recordar que no incluye el x_0
    np.fill_diagonal(A[1:-1, :], 1)  # recordar que no incluye el x_0
    np.fill_diagonal(A[1:, 2:], 1)  # recordar que no incluye el x_0
    A[0, -1] = 1
    A[0,-1] = 1
    
    if info:
        print(A)

    return A, xi, h
