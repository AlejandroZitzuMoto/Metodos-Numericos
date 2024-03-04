import numpy as np

#Verifica si es un int o flotante

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

def sigma(funcion, x):
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
    sigm = 1 if funcion(a)*funcion(b) > 0 else -1
    return sigm

#Esta se encarga de guardar los intervalos donde exista una posible raiz


def localizador(funcion, x0, Nint = 100):
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
    interval = np.linspace(x0[0],x0[1], Nint)
    localiz = []
    for i in range(1, Nint):
        comparar = [interval[i-1], interval[i]]
        if sigma(funcion, comparar) < 0:
            localiz.append(comparar)
    return localiz


#Para elegir el error
'''
def error(num):
    T_error =  {
                    "1": lambda x,x1: abs(x - x1), #absolito
                    "2": lambda x,x1: abs((x-x1)/x1), #Relativo 
                    "3": lambda pn1, pn: abs(x-x1)/abs(max([x, x1])) #Cambio relativo
                }
    return T_error(num)
'''

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
def Dominio(x, funcion, Nint = 100):
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
    
    lim = np.linspace(x[0],x[1], Nint)
    posible = []
    for i in range(len(lim)):
        comparar = [lim[i-1], lim[i]]
        if sigma(funcion, comparar) < 0:
            posible.append(lim[i])
    return posible


