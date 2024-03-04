from .Raices.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio


def punto_fijo(a, funcion1, tol = 1e-4 , Ni = 150):  
    raiz = 0
    i = 1
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

def raiz_fija(x0, f, f2,tol = 1e-5, Ni = 200):
    if es_flotante(x0[0]) == True and es_flotante(x0[1]) == True:   
        w = [float(x0[i]) for i in range(2)]
        raiz_loop = Dominio(w, f2)
        raiz = []
        print(raiz_loop)
        for i in raiz_loop:
                p = punto_fijo(i, f, f2, tol, Ni)
                raiz.append(p)
        return raiz
    else:
        print("Parametros erroneos")