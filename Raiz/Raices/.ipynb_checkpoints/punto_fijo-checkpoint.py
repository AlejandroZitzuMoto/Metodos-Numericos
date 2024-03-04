from .Raices.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio


def punto_fijo(a, funcion1, tol = 1e-4 , Ni = 150):  
    """
    -----------------------------------------------
    Metodo del punto fijo para una raiz
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    intervalo: Recibe un solo parametros, usualmete uno de los extremos del intervalo [a,b].
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.
    tol: la presicion a buscar, por defecto es en 1e-4.
    Ni: Numero de iteraciones, por defecto esta en 150.
    
    ------------------------
    Salida: raiz
    ------------------------
    """
    
    raiz = 0
    i = 1
    if es_flotante(a) == True:
        while i <= Ni:
            p = funcion1(a)
            if abs((p - a)/a) <= tol:
                print("La raiz de nuestra funcion es: %.5f"% p)
                raiz = p
                break
            i += 1
            a = p
        
        else:
            print("El sistema no es capaz de encontrar la raiz")
        return raiz    
    else:
        print("Valores incorrectos")
        

def raiz_fija(x0, f, tol = 1e-5, Ni = 200):
    """
    -----------------------------------------------
    Metodo del punto fijo para una o más raices
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    intervalo: Recibe dos parametros, usualmete los extremos del intervalo [a,b].
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.
    df: La derivada de la funcion, con lambda o def, refiriendoce a df(x)/dx.
    tol: la presicion a buscar, por defecto es en 1e-4.
    Ni: Numero de iteraciones, por defecto esta en 200.
    
    ------------------------
    Salida: raices
    ------------------------
    """
    
    if es_flotante(x0[0]) == True and es_flotante(x0[1]) == True:   
        w = [float(x0[i]) for i in range(2)]
        raiz_loop = Dominio(w, f2)
        raiz = []
        print(raiz_loop)
        for i in raiz_loop:
                p = punto_fijo(i, f, tol, Ni)
                raiz.append(p)
        return raiz
    else:
        print("Valores incorrectos")
        