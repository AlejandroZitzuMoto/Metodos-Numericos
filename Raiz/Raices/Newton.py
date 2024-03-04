## Metodo de Newton
from .Raices.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio

# Importar las funciones

def Newton(x0,f,df, tol=1e-5):
    """
    -----------------------------------------------
    Metodo de Newton para una raiz
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    intervalo: Recibe dos parametros, usualmete los extremos del intervalo [a,b].
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.
    df: La derivada de la funcion, con lambda o def, refiriendoce a df(x)/dx.
    tol: la presicion a buscar, por defecto es en 1e-5.
    
    ------------------------
    Salida: raiz
    ------------------------
    """
    
    operador = True
    raiz = 0
    if es_flotante(x0[0]) == True and es_flotante(x0[1]) == True:
        while operador:
            p = x0 - (f(x0)/df(x0))
            if abs(x0-p) < tol:
                #print("La raiz de su función es: ", p)
                raiz = p
                operador = False
            x0 = p
        return raiz
    else:
        print("Valores incorrectos")
        

def raiz_N(x0, f, df,tol = 1e-5):
    """
    -----------------------------------------------
    Metodo del punto fijo para una o más raices
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    intervalo: Recibe dos parametros, usualmete los extremos del intervalo [a,b].
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.
    df: La derivada de la funcio, con lambda o def, refiriendoce a f(x).
    tol: la presicion a buscar, por defecto es en 1e-5.
    
    ------------------------
    Salida: raices
    ------------------------
    """
    
    if es_flotante(x0[0]) == True and es_flotante(x0[1]) == True:
        w = [float(x0[i]) for i in range(2)]

        raiz_loop = Dominio(w,f)
        raiz = []
        for i in raiz_loop:
            p = Newton(i,f,df,tol)
            raiz.append(p)
        return raiz
    else:
        print("Valores incorrectos")

    