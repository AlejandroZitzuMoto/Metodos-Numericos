from .Raices.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio, error


def punto_fijo(a, f1, df=None, errores = "E_rel2", Ni=150, tol=1e-4):  
    """
    -----------------------------------------------
    Metodo del punto fijo para una raiz
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    a: Recibe dos solo parametros, usualmete los intervalo [a,b].
    f: La funcion g(x) lambda o el objeto def , estos refresentan la funcion que se analizara.
    df: La derivada de g(x), obsional
    
    errores: Tipos de errores, E_ab (error absoluto), E_rel (error relativo), 
    E_RPD (error diferencia de procentaje relativo), E_rel3
    (error de diferencia y cambio relativo), E_dis (error de sitancia), E_rel2 (error relativo para convergencias cercanas a cero).
    
    tol: la presicion a buscar, por defecto es en 1e-4.
    Ni: Numero de iteraciones, por defecto esta en 150.
    
    ------------------------
    Salida: raiz
    ------------------------
    """
    
    raiz = 0
    i = 1
    if es_flotante(a[0]) == True and es_flotante(a[1]) == True:
        w = [float(a[i]) for i in range(2)]
        if f1(w[0]) > w[0] and f1(w[1]) < w[1]:
            if derivada(df, w[0]):
                while i <= Ni:
                    p = f1(w[0])
                    if error(errores)(p,w[0]) <= tol:
                        print("La raiz de nuestra funcion es: %.5f" % p)
                        raiz = p
                        break
                    i += 1
                    w[0] = p
                else:
                    print("El sistema no es capaz de encontrar la raiz")
                return raiz
            else:
                print("No es posible encontrar la raiz por este metodo")
    else:
        print("Los valores introducidos son erroneos")



def raiz_fija(x0, f,  g,df = None, errores = 'E_rel2', tol = 1e-5, Ni = 200):
    """
    -----------------------------------------------
    Metodo del punto fijo para una o más raices
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    x0: Recibe dos parametros, usualmete los extremos del intervalo [a,b].
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.
    g: La funcion original f(x), en lambda o def.
    df: La derivada de la funcion, con lambda o def, refiriendoce a df(x)/dx.
    
    errores: Tipos de errores, E_ab (error absoluto), E_rel (error relativo), 
    E_RPD (error diferencia de procentaje relativo), E_rel3
    (error de diferencia y cambio relativo), E_dis (error de sitancia), E_rel2 (error relativo para convergencias cercanas a cero).
    
    tol: la presicion a buscar, por defecto es en 1e-4.
    Ni: Numero de iteraciones, por defecto esta en 200.
    
    ------------------------
    Salida: raices
    ------------------------
    """
    
    if es_flotante(x0[0]) == True and es_flotante(x0[1]) == True:   
        w = [float(x0[i]) for i in range(2)]
        raiz_loop = localizador(g, w)
        raiz = []
        for i in range(len(raiz_loop)):
                print(f)
                p = punto_fijo(raiz_loop[i], f, df, errores, Ni, tol)
                raiz.append(p)
        return raiz
    else:
        print("Valores incorrectos")
        