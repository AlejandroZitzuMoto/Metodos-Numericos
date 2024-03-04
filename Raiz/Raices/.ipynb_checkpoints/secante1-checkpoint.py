## Metodo secante
from .Raices.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio

## Importar libreria de funciones
def secante1(x,f, tol= 1e-4):
    """
    ---------------------------
    Metodo de la secante 1
    ---------------------------
    
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
            p = x[1]-(f(x[1]) * (x[1] - x[0]))/(f(x[1])-f(x[0]))
            if abs(x[1]-p) < tol:
                #print("La raiz de su función es: ", p)
                raiz = p
                operador = False
            x[0] = x[1]
            x[1] = p
        return raiz
    else:
        print("Valores erroneos")

def raiz_secante1(x0, f, tol = 1e-4): 
    """
    -----------------------------------------------
    Metodo de la secante 1 para una o más raices
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    intervalo: Recibe dos parametros, usualmete los extremos del intervalo [a,b] a analizar
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara
    tol: la presicion a buscar, por defecto es en 1e-4
    
    ------------------------
    Salida: raices
    ------------------------
    """
    
    if es_flotante(x0[0]) == True and es_flotante(x0[1]) == True:
        w = [float(x0[i]) for i in range(2)]
        raiz_loop = localizador(f,w)
        raiz = []
        for i in raiz_loop:
            p = secante(i,f,tol)
            raiz.append(p)
        return raiz
    else:
        print("Valores erroneos")
        