## Metodo de Newton
from .heramientas.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio, error, D_central, ExRch

# Importar las funciones

def Newton(x0,f, errores = 'E_dis',tol=1e-5):
    """
    -----------------------------------------------
    Metodo de Newton para una raiz
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    x0: Recibe un parametros, cualquier punto [a,b] cercano a la raiz.
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.
    
    errores: Tipos de errores, E_ab (error absoluto), E_rel (error relativo), 
    E_RPD (error diferencia de procentaje relativo), E_rel3
    (error de diferencia y cambio relativo), E_dis (error de sitancia), E_rel2 (error relativo para convergencias cercanas a cero).
    
    tol: la presicion a buscar, por defecto es en 1e-5.
    
    ------------------------
    Salida: raiz
    ------------------------
    """
    operador = True
    if es_flotante(x0) == True:
        w = float(x0)
        while operador:
            df = ExRch(w,f,D_central)
            if abs(df) != 0:
                p = w-f(w)/df
                if abs(w-p)/(1+abs(p)) < tol:
                    raiz = p
                    return raiz
                    operador = False
                else:
                    w = p
            else:
                print("Error, derivada = 0")
                operador = False
    else:
        print("Valores incorrectos.")


def raiz_newton(x0, f, errores = 'E_dis', tol = 1e-5):
    """
    -----------------------------------------------
    Metodo del punto fijo para una o más raices
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    x0: Recibe dos parametros, usualmete los extremos del intervalo [a,b].
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.
    df: La derivada de la funcio, con lambda o def, refiriendoce a f(x).

    errores: Tipos de errores, E_ab (error absoluto), E_rel (error relativo), 
    E_RPD (error diferencia de procentaje relativo), E_rel3
    (error de diferencia y cambio relativo), E_dis (error de sitancia), E_rel2 (error relativo para convergencias cercanas a cero).
    
    tol: la presicion a buscar, por defecto es en 1e-5.
    
    ------------------------
    Salida: raices
    ------------------------
    """
    if es_flotante(x0[0]) == True and es_flotante(x0[1]) == True:
        w = [float(x0[i]) for i in range(2)]
        raiz_loop = Dominio(w,f,tol)
        raiz = []
        for i in raiz_loop:
            p = Newton(i,f, errores, tol)
            raiz.append(p)
        return raiz
        
    else:
        print("Valores incorrectos.")
    
    