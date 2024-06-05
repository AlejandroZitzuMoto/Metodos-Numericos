import numpy as np
from .Raiz.Raices.heramientas.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio, error, derivada, D_central, ExRch

from .Raiz.Raices.biseccion import biseccion, raiz_biseccion
from .Raiz.Raices.Newton import Newton, raiz_newton
from .Raiz.Raices.punto_fijo import punto_fijo, raiz_fija
from .Raiz.Raices.secante1 import secante1, raiz_secante1
from .Raiz.Raices.secante2 import secante2, raiz_secante2

def I_bool(w,f,Ni = 51):
    '''
    Integral booleano
    -------------------------
    w: Intervalo
    f: función
    Ni: Numero de repeticiones
    -------------------------
    Salida: Resultado de la integral
    '''
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    x = np.linspace(x0[0],x0[1],Ni)
    I_S38 = (2*h/45)*(7*f(x[0]) + 7*f(x[-1]))
    I_S33, I_S32 = 0,0
    for i in range(0,len(x-1)):
        if i%2 == 0:
            I_S32 = I_S32 + (24*h/45)*f(x[i])
        else:
            I_S33 = I_S33 + (62*h/45)*f(x[i])
            
    return (I_S38 + I_S33 + I_S32)

def error(er):    
    """
    -----------------------------------------
    Entrada: Elegir un tipo de error
    -----------------------------------------

    Parametros
    x: Reprenta el nombre del tipo, donde estan: E_ab (error absoluto), E_rel (error relativo), 
    E_RPD (error diferencia de procentaje relativo), E_rel3
    (error de diferencia y cambio relativo), E_dis (error de sitancia), E_rel2 (error relativo para convergencias cercanas a cero).
    ------------------------------------------
    Salida: Regresa un error
    ------------------------------------------
    """
    
    errores = {
                "E_ab": lambda x, x0: abs(x-x0),
                "E_rel": lambda x, x0: abs(x-x0)/abs(x0),
                "E_rel2": lambda x,x0: abs(x-x0)/(1+abs(x0)),
                "E_RPD": lambda x, x0: 2*((x-x0)/abs(x)+abs(x0)),
                "E_rel3": lambda x, x0: abs(x-x0)/abs(max([x,x0])),
                "E_dis": lambda x, x0: abs((x - x0)/2)
             }
    return errores[er]

def D_simp(a,h,f, d = True):
    '''
    Deribada simple
    -------------------
    a: Intervalo
    h: paneles
    f: función
    d: True -> Derivada derecha, False -> Derivada por la izquierda
    ---------------------------------------------------
    Salida: la derivada
    '''
    df = (f(a+h)-f(a))/h if d else (f(a) - f(a+h))/h
    return df

def D_central(x,h,f):
    '''
    Derivada central
    ----------------
    x: Intervalo
    h: Paneles
    f: Función
    ----------------------
    Salida: derivada
    '''
    return (f(x+h/2) - f(x-h/2))/h


def Seg_derivada(x,h,f):
    '''
    Segunda derivada 
    ----------------
    x: Intervalo
    h: Paneles
    f: Función
    ----------------------
    Salida: Resultado de la segunda derivada
    '''
    return (f(x[0]+h/2)+f(x[1]-h/2)-2*f(x[2]))/h**2

def I_rectangular(w,f, Ni = 10):
    '''
    Integral rectangular
    -------------------------
    w: Intervalo
    f: función
    Ni: Numero de repeticiones
    -------------------------
    Salida: Resultado de la integral
    '''
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    x = np.linspace(x0[0],x0[1], Ni)
    I_R = 0
    for i in range((Ni-1)):
         I_R = I_R + f(x[i])*h 
    return I_R

def I_trapecio(w, f, Ni = 20):
    '''
    Integral trapecio
    -------------------------
    w: Intervalo
    f: función
    Ni: Numero de repeticiones
    -------------------------
    Salida: Resultado de la integral
    '''
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    I_T2 = 0
    x = np.linspace(x0[0],x0[1],Ni)
    I_T = h*f(x[0])/2
    I_T3 = h*f(x[-1])/2
    for i in range(0,len(x)-2):
        I_T2 = I_T2 + f(x[i+1])*h
    return (I_T+I_T2+I_T3)

def I_pmedio(w,f,Ni=50):
    '''
    Integral punto medio
    -------------------------
    w: Intervalo
    f: función
    Ni: Numero de repeticiones
    -------------------------
    Salida: Resultado de la integral
    '''
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    x = np.linspace(x0[0],x0[1],Ni)
    I_pm = 0
    for i in range(len(x)-2):
        x1 = (x[i] + x[i+1])/2
        I_pm = I_pm + f(x1)*h
    return I_pm

def I_Sim13(w,f,Ni = 15):  
    '''
    Integral simpson 1/3
    -------------------------
    w: Intervalo
    f: función
    Ni: Numero de repeticiones
    -------------------------
    Salida: Resultado de la integral
    '''
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    x = np.linspace(x0[0],x0[1],Ni)
    I_S2, I_S4 = 0, 0
    for i in range(0,len(x)-1):
        if i%2 == 0:
            I_S2 = I_S2 + f(x[i])*(2*h/3)
        else:
            I_S4 = I_S4 + f(x[i])*(4*h/3)
   
    I_S3 = (h/3)*(f(x[0]) + f(x[-1]))
    return (I_S4 + I_S3 + I_S2)

def I_Sim18(w,f,Ni = 51):
    '''
    Integral simson 1/8
    -------------------------
    w: Intervalo
    f: función
    Ni: Numero de repeticiones
    -------------------------
    Salida: Resultado de la integral
    '''
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    x = np.linspace(x0[0],x0[1],Ni)
    I_S38 = (3*h/8)*(f(x[0]) + f(x[-1]))
    I_S33, I_S32 = 0,0
    for i in range(0,len(x-1)):
        if i%3 == 0:
            I_S32 = I_S32 + (6*h/8)*f(x[i])
        else:
            I_S33 = I_S33 + (9*h/8)*f(x[i])
            
    return (I_S38 + I_S33 + I_S32)

def RecBonnet(n,x):
    '''
    Disminuye el error de maquina
    --------------------------------
    n: Grado del polinimo
    x: puntos
    --------------------
    salida: 1) Punto inicial, 2) Punto final
    '''
    p0, pn = 1,x
    for j in range(1,n):
        pn1 = ((2*j+1)*x*pn - j*p0)/(j+1.0)
        p0,pn = pn,pn1
    return p0,pn

def legendre(n, x):
    '''
    Polinomio ortogonal de Legrenge
    -------------------------
    n: Grado del polinomio
    x: Punto
    --------------------------------
    salida: 1) El valor del polinomio, 2) El valor de su derivada
    '''
    if n==0:
        valn = 1
        dvaln = 0
    elif n==1:
        valn = x
        dvaln = 1
    else:
        valn_m1, valn = RecBonnet(n, x)
        dvaln = n*(valn_m1-x*valn)/(1.-x**2)
    return valn, dvaln


def legraiz(n, delt=.2, error='E_rel2', tol=1e-5):
    '''
    Encuntra raices del poli. de Legrenge
    -----------------------------------------
    n: Grado del polinimio
    delt: Delta
    error: Tipo de error
    tol: Tolerancia
    --------------
    Salida: Devuelve raices
    '''
    raices = np.zeros(n)
    npos = n//2 
    
    f = lambda x: legendre(n, x)[0]  
    for i in range(npos):
        p0 = np.cos(np.pi*(4*i+3)/(4*n+2)) - delt 
        p1 = p0 + 2*delt
        # print('p0 -->', p0,'p1-->', p1)
        raiz = secante2([p0, p1], f, error, tol)
        raices[i] = -raiz
        raices[-1-i] = raiz
    return raices

def Gus_param(n, delt=0.2, error='E_rel2', tol=1e-05): 
    '''
    Parametros de la integral de Gauss
    --------------------------------------
    n: Grado del polinomio
    delt: Delta
    error: Tipo de error
    tol: Tolerancia
    -------
    Salida: Devuelve las raices y los pesos
    '''
    xraiz = legraiz(n, delt, error, tol)
    Pn = legendre(n, xraiz)[1]
    W = 2/(1-xraiz**2)/Pn**2
    return xraiz, W

def I_Gauss(x,f,n =2, det = .2 ,error = 'E_rel2', tol = 1e-5):
    '''
    Integral de Gauss
    -------------------------
    x: Intervalo
    f: función
    n: Elegir el grado de polinomio.
    det: delta
    error: Elegir el tipo de error
    tol: Tolerancia
    -------------------------
    Salida: Resultado de la integral
    '''
    I_G = 0
    xr,W = Gus_param(n, delt=.2, error='E_rel2', tol=1e-05)
    for i in range(0,n):
        x2 = (x[1]+x[0])/2 + (x[1]-x[0])*xr[i]/2
        I_G = I_G + W[i]*f(x2)
    return ((x[1]-x[0])*I_G)/2
    
def I_Gauss2D(I2,I,f,n = 2):
    """
    Integral doble Gauss
    ----------------------------------
    I: Intervalo de y, con funciones.
    I2: Intervalo de x
    f: la funcion f(x,y)
    n: El gadro del polinomio de Legender
    ----------------------------------------
    Resultado: Integral
    """
    D2 = 0
    xr,W = Gus_param(n, delt=.2, error='E_rel2', tol=1e-05)
    for i in range(1,n):
        for j in range(1,n):
            u2 = (I2[1]+I2[0])/2 + ((I2[1]-I2[0])*xr[j])/2
            u = (I[1]+I[0])/2 + ((I[1]-I[0])*xr[i])/2
            D2 = D2 + (W[j]**2)*f(u2,u)
    return D2*(I2[1]-I2[0])*(I[1]-I[0])/2
