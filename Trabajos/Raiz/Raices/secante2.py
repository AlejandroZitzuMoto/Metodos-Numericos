## Metodo de secante 2
from .heramientas.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio, error

## Importar libreria
def secante2(x,funcion, errores = 'E_ab',tol = 1e-4):
    """
    El metodo de la secante para una sola raiz
    
    Los parametros que cuenta:
    x: Recibe dos parametros, usualmete los extremos del intervalo [a,b] a analizar.
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.

    errores: Tipos de errores, E_ab (error absoluto), E_rel (error relativo), 
    E_RPD (error diferencia de procentaje relativo), E_rel3
    (error de diferencia y cambio relativo), E_dis (error de sitancia), E_rel2 (error relativo para convergencias cercanas a cero).
    
    tol: la presicion a buscar, por defecto es en 1e-4

    ------------------------
    Salida: raiz
    ------------------------

    """
    operador = True
    raiz = 0
    if es_flotante(x[0]) == True and es_flotante(x[1]) == True:    
        w = [float(x[i]) for i in range(2)]
        while operador:
            p = w[1]-(funcion(w[1]) * (w[1] - w[0]))/(funcion(w[1])-funcion(w[0]))
            if error(errores)(w[0],w[1]) < tol:
                #print("La raiz de su función es: ", p)
                raiz = p
                operador = False
            w[0] = w[1]
            w[1] = p
        return raiz
    else:
        print("Valores erroneos")

def raiz_secante2(x1, f, errores = 'E_ab', tol = 1e-4):
    """
    El metodo de la secante 2 para una o más raices

    Los parametros que cuenta:
    x1: Recibe dos parametros, usualmete los extremos del intervalo [a,b] a analizar.
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.

    errores: Tipos de errores, E_ab (error absoluto), E_rel (error relativo), 
    E_RPD (error diferencia de procentaje relativo), E_rel3
    (error de diferencia y cambio relativo), E_dis (error de sitancia), E_rel2 (error relativo para convergencias cercanas a cero).
    
    tol: la presicion a buscar, por defecto es en 1e-4

    ------------------------
    Salida: raices
    ------------------------
    """
    if es_flotante(x1[0]) == True and es_flotante(x1[1]) == True:
        w = [float(x1[i]) for i in range(2)]
        raiz_loop = localizador(f, w)
        raiz = []
        for i in raiz_loop:
            p = secante_2(i, f, errores, tol)
            raiz.append(p)
        return raiz
    else:
        print("Valores erroneos")