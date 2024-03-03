## Metodo de secante 2

## Importar libreria
def secante(a,b,tol,funcion,raiz):
    operador = True
    while operador:
        p = b-(funcion(b) * (b - a))/(funcion(b)-funcion(a))
        if abs(b-p) < tol:
            print("La raiz de su función es: ", p)
            raiz.append(p)
            operador = False
        a = b
        b = p
    return raiz

def raiz_secante2(x1, f, tol = 1e-4):
    if es_flotante(x1[0]) == True and es_flotante(x1[1]) == True:
        w = [float(x1[i]) for i in range(2)]
        raiz_loop = localizador(f, w)
        raiz = []
        for i in raiz_loop:
            p = secante_2(i, f, tol)
            raiz.append(p)
        return raiz
    else:
        print("Valor erroneo")