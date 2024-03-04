from .Raices.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio

# Tambien para cuando nuestras funciones no tengan nada que ya esten pre definidas y que esten a prueba de errores 
# Importar la nueba libreria que creemos


'''
Biseccion
'''

def biseccion(local, funcion, tol = 1e-4,Ni = 200):
    """
    -----------------------------------------------
    Metodo de biseccion para una raiz
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    intervalo: Recibe dos parametros, usualmete los extremos del intervalo [a,b].
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.
    tol: la presicion a buscar, por defecto es en 1e-4.
    Ni: Numero de iteraciones, por defecto esta en 200.
    
    ------------------------
    Salida: raiz
    ------------------------
    """
    
    raiz = 0
    if es_flotante(local[0]) == True and es_flotante(local[1]) == True:
        for i in range(len(local)):
            if i < Ni:
                p = suma(local[i-1],local[i])
                if abs((local[i-1] - local[i]/2)) <= tol or abs(funcion(p)) <= tol:
                    print("La raiz de la funcion es: %.5f"% p)
                    raiz = p 
                    break
                else:
                    if funcion(local[i-1])*funcion(p) > 0:
                         local[i-1] = p
                         
                    else:
                        local[i] = p
                        
                
                Ni -= 1
            else:
                print("No se logro encontrar la raiz")
                break
        return raiz
    else:
        print("Valores incorrectos")


'''
Funcion biseccion como tal
'''

def raiz_b(x0, funcion, tol = 1e-4, Ni = 200):
    """
    -----------------------------------------------
    Metodo de biseccion para una o más raices
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    intervalo: Recibe dos parametros, usualmete los extremos del intervalo [a,b].
    f: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.
    tol: la presicion a buscar, por defecto es en 1e-4.
    Ni: Numero de iteraciones, por defecto esta en 200.
    
    ------------------------
    Salida: raices
    ------------------------
    """
    
    if es_flotante(x0[0]) == True and es_flotante(x0[1]) == True:
        w = [float(x0[i]) for i in range(2)]
        raiz_loop = localizador(funcion,w) 
        raiz_real = []
        for i in raiz_loop:
            p = biseccion(i, funcion, tol, Ni)
            raiz_real.append(p)
        return raiz_real
    else:
        print("Valores incorrectos")

