## Metodo de secante 2
from .Raices.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio

## Importar libreria
def secante2(x,funcion, ,tol = 1e-4):
    """
    El metodo de la secante para una sola raiz
    
    Los parametros que cuenta:
    intervalo: Recibe dos parametros, usualmete los extremos del intervalo [a,b] a analizar
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara
    tol: la presicion a buscar, por defecto es en 1e-4

    ------------------------
    Salida: raiz
    ------------------------

    """
    operador = True
    raiz = 0
    if es_flotante(x[0]) == True and es_flotante(x[1]) == True:    
        while operador:
            p = x[1]-(funcion(x[1]) * (x[1] - x[0]))/(funcion(x[1])-funcion(x[0]))
            if abs(x[1]-p) < tol:
                #print("La raiz de su función es: ", p)
                raiz = p
                operador = False
            x[0] = x[1]
            x[1] = p
        return raiz
    else:
        print("Valores erroneos")

def raiz_secante2(x1, f, tol = 1e-4):
    """
    El metodo de la secante 2 para una o más raices

    Los parametros que cuenta:
    intervalo: Recibe dos parametros, usualmete los extremos del intervalo [a,b] a analizar
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara
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
            p = secante_2(i, f, tol)
            raiz.append(p)
        return raiz
    else:
        print("Valores erroneos")