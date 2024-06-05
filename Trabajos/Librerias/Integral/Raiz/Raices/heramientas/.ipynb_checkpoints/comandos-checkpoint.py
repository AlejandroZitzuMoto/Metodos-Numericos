import numpy as np

#Verifica si es un int o flotante

def D_central(f,x,h):
    """
    ----------------------
    Entrada
    ----------------------
    x: Punto evaluado
    h: ditancia entre cada corte
    f: Funcion
    """
    df = (f(x+h/2) - f(x-h/2))/h
    return df
    
def ExRch(x,f,g,h =1e-6 ,p = 2):
    """
    --------------------------
    Entrada
    --------------------------
    x: Punto evaluado
    h: ditancia entre cada corte
    p: Orden del error
    f: Funcion
    g: Derivada
    
    """
    G = (2**p *g(f,x,h/2) - g(f,x,h))/(2**p -1)
    return G

def derivada(df, a):
    if df is None:
        return True
    if abs(df(a)) < 1:
        return True
    else:
        return False

def es_flotante(variable):
    """
    -----------------------
    Verificador de numeros
    ------------------------
    
    Parametros:
    float: una valor de tipo int o flotante
    
    -----------------------------------
    Salida: Regresa un verdadero si cumple con un numero y un falso si es un caracter
    ----------------------------------
    """
    try:
        float(variable)
        return True

    except:
        return False

#Meter intervalo

def intr_int():
    """
    --------------------
    Ingresar Parametros
    --------------------

    Parametros:
    a: El intervalo menor
    b: El intervalos mayor
    
    -----------------------
    Salida: Regresa una lista con los intervalos
    -----------------------
    """
    
    a = input("Ingrese el intervalo izquierdo: ")
    b = input("Ingrese el intervalo derecho: ")
    return [a,b]


#Esta funcion se encarga de ver que el producto de las dos funciones se menor que cero

def sigma(funcion, x, tol = 1e-4):
    """
    --------------------------------------
    Retrorno de sigo evaluado en funcion
    --------------------------------------
    
    Parametros:
    f: Una funcion lambda o def, la cual sera nuestra función
    x: Nuestras variables que se encargaran de evaluar nuestra función

    -------------------------------------------------------------
    Salida: Regresa -1 si f(a)*f(b) es menor y 1 si es mayor
    -------------------------------------------------------------
    """

    a, b = x[0], x[1]
    # sigm = 1 if funcion(a)*funcion(b) > 0 else -1
    if funcion(a)*funcion(b) > 0:
        sigm = 1
    elif (funcion(a)*funcion(b) == 0 ) or funcion(a)*funcion(b) <= tol:
        sigm = 0
    else: 
        sigm = -1
    return sigm

#Esta se encarga de guardar los intervalos donde exista una posible raiz


def localizador(f,x0,tol = 1e-4, Ni = 100):
    """
    ----------------------------------------------------
    Busca las posibles raices en una funcion
    ----------------------------------------------------
    Parametros:
    f: Funcion lambda o def, f(x).
    intervalo: los extremos del intervalo a analizar
    Nint: La cantidad de puntos a partir

    ----------------------------------------------------------------------------------------------
    Salida: Una lista que aguarda varias posiciones para nuestras posibles raices, la cual alberga otra lista con dos posiciones donde se encuentra una raiz
    ----------------------------------------------------------------------------------------------------
    
    """
    x1 = (x0[1]-x0[0])/Ni
    x2 = []
    x3 = x0[0] + x1
    x4 = x3
    x2.append(x3)
    for i in range(Ni):
        x4 = x4 + x1
        x2.append(x4)
    localiz = []
    for i in range(1, Ni):
        comparar = [x2[i-1],x2[i]]
        if sigma(f, comparar, tol) < 0 or sigma(f, comparar, tol) == 0:
            localiz.append(comparar)
    return localiz



#Suma


def suma(a,b):
    """
    ------------------------------
    Suma dos valores
    ------------------------------
    Parametros:
    a: Numero cualquiera
    b: Numero cualquiera que no sea a

    ------------------------------------------
    Salida: Regresa el promedio de estos dos
    ------------------------------------------
    """

    return(a+b)/2


# derivada evaluada en "a" (a,b)
def derivada(df,a):
    if abs(df(a)) < 1:
        return True
    else:
        return False

#Hace lo mismo que localizador pero solo da un valor donde puede estar la raiz
def Dominio(x0,f,tol = 1e-4,Ni = 100):
    """"
    ------------------------------------------------------
    Busca las posibles raices en una funcion
    ------------------------------------------------------
    
    Parametros:
    f: Funcion lambda o def, f(x).
    intervalo: los extremos del intervalo a analizar
    Nint: La cantidad de puntos a partir

    ----------------------------------------------------------------------------------------------
    Salida: Devuelve una lista con la posicion de las raices
    ----------------------------------------------------------------------------------------------
    
    """
    x1 = (x0[1]-x0[0])/Ni
    x2 = []
    x3 = x0[0] + x1
    x4 = x3
    x2.append(x3)
    for i in range(Ni):
        x4 = x4 + x1
        x2.append(x4)
    localiz = []
    for i in range(1, Ni):
        comparar = [x2[i-1],x2[i]]
        if sigma(f, comparar, tol) < 0 or sigma(f, comparar, tol) == 0:
            localiz.append(comparar[0])
    return localiz

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


