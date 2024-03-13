from .heramientas.comandos import es_flotante, intr_int, sigma, localizador, suma, derivada, Dominio, error

# Tambien para cuando nuestras funciones no tengan nada que ya esten pre definidas y que esten a prueba de errores 
# Importar la nueba libreria que creemos


'''
Biseccion
'''

def biseccion(local, funcion, errores = "E_dis", tol = 1e-4,Ni = 200):
    """
    -----------------------------------------------
    Metodo de biseccion para una raiz
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    local: Recibe dos parametros, usualmete los extremos del intervalo [a,b].
    funcion: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.

    errores: Tipos de errores, E_ab (error absoluto), E_rel (error relativo), 
    E_RPD (error diferencia de procentaje relativo), E_rel3
    (error de diferencia y cambio relativo), E_dis (error de sitancia), E_rel2 (error relativo para convergencias cercanas a cero).
    
    tol: la presicion a buscar, por defecto es en 1e-4.
    Ni: Numero de iteraciones, por defecto esta en 200.
    
    ------------------------
    Salida: raiz
    ------------------------
    """
    
    raiz = 0
    if es_flotante(local[0]) == True and es_flotante(local[1]) == True:
        w = [float(local[i]) for i in range(2)]
        for i in range(len(w)):
            if i < Ni:
                p = suma(w[0], w[1])
                if error(errores)(w[0],w[1]) <= tol or abs(funcion(p)) <= tol:
                    print("La raiz de la funcion es: %.5f"% p)
                    raiz = p 
                    break
                else:
                    if funcion(w[0])*funcion(p) > 0:
                         w[0] = p
                         
                    else:
                        w[1] = p
                        
                
                Ni -= 1
            else:
                print("No se logro encontrar la raiz")
                break
        return raiz
    else:
        print("Valores erroneos")

'''
Funcion biseccion como tal
'''

def raiz_b(x0, funcion, errores = "E_dis",Ni = 150, tol = 1e-4):
    """
    -----------------------------------------------
    Metodo de biseccion para una o más raices
    -----------------------------------------------
    
    Los parametros que cuenta:
    
    x0: Recibe dos parametros, usualmete los extremos del intervalo [a,b].
    funcion: La funcion lambda o el objeto def , estos refresentan la funcion que se analizara.
    
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
        raiz_loop = localizador(funcion,w) 
        raiz_real = []
        for i in raiz_loop:
            p = biseccion(i, funcion, errores, tol, Ni)
            raiz_real.append(p)
        return raiz_real
    else:
        print("Valores incorrectos")

