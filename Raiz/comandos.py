
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
    return [a,b]

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


# derivada evaluada en "a" (a,b)
def derivada(df,a):
    if abs(df(a)) < 1:
        return True
    else:
        return False

#Hace lo mismo que localizador pero solo da un valor donde puede estar la raiz
def Dominio(x, funcion):
    lim = np.linspace(x[0],x[1], 100)
    posible = []
    for i in range(len(lim)):
        comparar = [lim[i-1], lim[i]]
        if sigma(funcion, comparar) < 0:
            posible.append(lim[i])
    return posible


