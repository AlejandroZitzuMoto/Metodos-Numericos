import numpy as np
# Hacer una funcion que se encarge de encontrar las condiciones donde se encuentran nuestras raices. 
# Tambien para cuando nuestras funciones no tengan nada que ya esten pre definidas y que esten a prueba de errores 

#////////////////////////////////////////////////////////////7
'''
Esta funcion se encarga de ver que el producto de las dos funciones se menor que cero
'''
def sigma(funcion, x):
    a, b = x[0], x[1]
    sigm = 1 if funcion(a)*funcion(b) > 0 else -1
    return sigm
'''
Esta se encarga de guardar los intervalos donde exista una posible raiz
'''

def localizador(funcion, a, b, Nint = 100):
    interval = np.linspace(a,b, Nint)
    localiz = []
    for i in range(1, Nint):
        comparar = [interval[i-1], interval[i]]
        if sigma(funcion, comparar) < 0:
            localiz.append(comparar)
    return localiz
'''
Para elegir el error
''
def error(num):
    T_error =  {
                    "1": lambda x,x1: abs(x - x1), #absolito
                    "2": lambda x,x1: abs((x-x1)/x1), #Relativo 
                    "3": lambda pn1, pn: abs(x-x1)/abs(max([x, x1])) #Cambio relativo
                }
    return T_error(num)
''
Suma
'''

def suma(a,b):
    return(a+b)/2

'''
Biseccion
'''

def biseccion(local, tol, funcion, suma,Ni):
    raiz = 0
    for i in range(len(local)):
        if i < Ni:
            p = suma(local[i-1],local[i])
            if abs((local[i-1] - local[i]/2) <= tol) or abs(funcion(p)) <= tol:
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

'''
Funcion biseccion como tal
'''

def raiz_b(local2, funcion, suma, Ni = 150, tol = 1e-4):
    raiz_loop = localizador(funcion,local2[0], local2[1]) 
    raiz_real = []
    print(raiz_loop) #///////////////////////////////////////////////// Aqui esta el problema
    for i in raiz_loop:
        p = biseccion(i, tol, funcion, suma, Ni)
        raiz_real.append(p)
    return raiz_real


'''
Verifica si es un int o flotante
'''
def es_flotante(variable):
	try:
		float(variable)
		return True
	except:
		return False

'''
Meter intervalo
'''
def intr_int():
    a = input("Ingrese el intervalo izquierdo: ")
    b = input("Ingrese el intervalo derecho: ")
    print(a, b)
    if es_flotante(a) == True and es_flotante(b) == True:
        w = float(a)
        y = float(b)
        return [w , y]
    
    else:
        print("Valor erroneo")    


    