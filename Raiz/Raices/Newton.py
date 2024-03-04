## Metodo de Newton
from .Raices.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio

# Importar las funciones

def Newton(x0,f,df, tol=1e-5):
    operador = True
    raiz = 0
    while operador:
        p = x0 - (f(x0)/df(x0))
        if abs(x0-p) < tol:
            #print("La raiz de su función es: ", p)
            raiz = p
            operador = False
        x0 = p
    return raiz


def raiz_N(x0, f, df,tol = 1e-5):
    if es_flotante(x0[0]) == True and es_flotante(x0[1]) == True:
        w = [float(x0[i]) for i in range(2)]

        raiz_loop = Dominio(w,f)
        raiz = []
        for i in raiz_loop:
            p = Newton(i,f,df,tol)
            raiz.append(p)
        return raiz
    else:
        print("Parametros incorrectos")

    