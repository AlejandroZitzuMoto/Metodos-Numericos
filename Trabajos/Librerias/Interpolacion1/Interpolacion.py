import numpy as np

def Pi(xv,yv):
    """
    Pendiente
    -------------
    xv: Puntos de x
    yv: Puntos de y
    """
    p = (yv[1]-yv[0])/(xv[1]-xv[0])
    return p
    
def Di(xv,yv, op = True):
    
    """
    Derivada
    -------------
    xv: Puntos de x
    yv: Puntos de y
    op: Obsion para usar h diferentes(False), h iguales(Fal)
    """
    if op == False:
        hi1 = xv[1]-xv[0]
        hi = xv[2]-xv[1]
        d = (hi1*Pi([xv[0],xv[1]],[yv[0],yv[1]])-hi*Pi([xv[1],xv[2]],[yv[1],yv[2]]))/(hi1 + hi)
    else:
        d = (Pi([xv[0],xv[1]],[yv[0],yv[1]])-Pi([xv[1],xv[2]],[yv[1],yv[2]]))/2
    return d

def Interpol_Cubica_Class1(xv,yv,x):
    '''
    Interpolación split cubica
    --------------------------
    xv: Valores de x
    yv: Valores de y
    x: Valor de entrada
    '''
    # Se puede poner como una lista para encerrar las funciones y amacenarlas en una lista
    n = len(xv)
    # si = np.zeros(n-1)
    d0 = Pi([xv[0],xv[1]],[yv[0],yv[1]])
    d1 = Di([xv[0],xv[1],xv[2]],[yv[0],yv[1],yv[2]])
    if xv[0] < x and  xv[1] > x:
        si = yv[0] + d0 * (x - xv[0]) + ((d1 - d0)/(xv[1] - xv[0])**2 ) * (x - xv[0])**2 * (x-xv[1])
        return si
    
    if n > 3:
        for i in range(1,n-2):
            di = Di([xv[i-1],xv[i],xv[i+1]],[yv[i-1],yv[i],yv[i+1]])
            di1 = Di([xv[i],xv[i+1],xv[i+2]],[yv[i],yv[i+1],yv[i+2]])
            pi = Pi([xv[i],xv[i+1]],[yv[i],yv[i+1]])
            h = (xv[i+1]-xv[i])
            if xv[i] < x and x < xv[i+1]:
                si = yv[i] + di*(x-xv[i]) + ((pi-di)/h)*(x-xv[i])**2 + ((di1 + di - 2*pi)/h**2)*(x - xv[i])**2 * (x - xv[i+1])
                return si
    
    if xv[-2] < x and x < xv[-1]:
        dn1 = Di([xv[-3],xv[-2],xv[-1]],[yv[-3],yv[-2],yv[-1]])
        pn1 = Pi([xv[-2],xv[-1]],[yv[-2],yv[-1]])
        si = yv[-2] + dn1*(x-xv[-2]) + ((pn1 - dn1)/(xv[-1]-xv[-2]))*(x-xv[-2])**2 + ((dn1 - pn1)/(xv[-1]-xv[-2])**2)*(x-xv[-2])**2*(x-xv[-1])
        return si

def Split_Cuadratico(xv,yv,x):
    '''
    Split Cuadratica
    ----------------------
    xv: Puntos en x
    yv: Puntos en y
    x: Punto a evaluar
    '''
    n = len(xv)
    if xv[0] < x and x < xv[1]:
        p0 = Pi([xv[0],xv[1]],[yv[0],yv[1]])
        d0 = Di([xv[0],xv[1],xv[2]],[yv[0],yv[1],yv[2]])
        h = (xv[-1]-xv[0])/(n-1)
        s = yv[0] + p0*(x-xv[0]) + ((d0 - p0)/h)*(x-xv[0])*(x-xv[1])
        return s
    if n > 3:
        for i in range(1,n-2):
            if i%2 == 0:
                if xv[i] < x and x < xv[i+1]:
                    pi = Pi([xv[i],xv[i+1]],[yv[i],yv[i+1]])
                    di = Di([xv[i],xv[i+1],xv[i+2]],[yv[i],yv[i+1],yv[i+2]])
                    h = xv[i+1]-xv[i]
                    s = yv[i] + pi*(x - xv[i]) + ((di - pi)/h)*(x - xv[i])*(x - xv[i+1])
                    return s
            else:
                if xv[i] < x and x < xv[i+1]:
                    pi = Pi([xv[i],xv[i+1]],[yv[i],yv[i+1]])
                    di = Di([xv[i],xv[i+1],xv[i+2]],[yv[i],yv[i+1],yv[i+2]])
                    h = xv[i+1]-xv[i]
                    s = yv[i] + pi*(x - xv[i]) + ((di + pi)/h)*(x - xv[i])*(x - xv[i+1])
                    return s
                
    if xv[-2] < x and x < xv[-1]:
        p = Pi([xv[-2],xv[-1]],[yv[-2],yv[-1]])
        h = xv[-1]-xv[-2]
        s = yv[-1] + p*(x - xv[-1]) + (p/h)*(x-xv[-2])*(x-xv[-1])
        return s

def Matriz(xv, yv):
    '''
    Matriz de split cubico clase 2
    --------------------------------
    xv: datos en x
    yv: datos en y
    --------------------------------
    Salida: Devuelve los valores de d en la formula
    '''
    n = len(xv)
    M = np.zeros([n,n])
    h = (xv[-1]-xv[0])/(n-1)
    # ////////////////////////////////
    B = np.zeros(n)
    B[0] = 3*((yv[1]-yv[0])/(xv[1]-xv[0]))
    for i in range(1,n-1):
        B[i] = 3*(((yv[i]-yv[i-1])/((xv[i]-xv[i-1])*(xv[i]-xv[i-1]))) + ((yv[i+1]-yv[i])/((xv[i+1]-xv[i])*(xv[i+1]-xv[i]))))
    
    B[-1] = 3*((yv[-1]-yv[-2])/(xv[-1]-xv[-2]))
    # ///////////////////////////////
    l = 2*(1/h + 1/h)
    l3 = 1/h
    np.fill_diagonal(M[:],l)
    np.fill_diagonal(M[1:,:],l3) 
    np.fill_diagonal(M[:, 1:],l3) 
    M[0][0] =2
    M[-1][-1] =2
    M[0][1] = 1
    M[-1][-2] = 1
    # ///////////////////////////////
    C = np.linalg.inv(M)
    # Resultado = C @ B
    Resultado = np.dot(C,B)
    return Resultado

def Inter_Cubica_Class2(xv,yv,x):
    '''
    Split Cubica clase 2
    --------------------
    xv: puntos en x
    yv: puntos en y
    x: Punto donde se evalua la función
    --------------------------------
    Salida: Valores de y entra cada punto
    '''
    n = len(xv)
    d = Matriz(xv,yv)
    if xv[0] < x and  xv[1] > x:
        h = (xv[1]-xv[0])
        pi = Pi([xv[0],xv[1]],[yv[0],yv[1]])
        p1 = (d[1] + d[0] - 2*pi)/h**2 
        s = yv[0] + d[0] * (x - xv[0]) + ((pi - d[0])/h) *(x-xv[0])**2 +  p1*(x - xv[0])**2 * (x-xv[1])
        return s
        
    if n > 3:
        for i in range(1,n-1):
            if x > xv[i] and x < xv[i+1]:
                pi = Pi([xv[i],xv[i+1]],[yv[i],yv[i+1]])
                h = xv[i+1]-xv[i]
                s = yv[i] + d[i]*(x-xv[i]) + ((pi-d[i])/h)*(x-xv[i])**2 + ((d[i+1] + d[i] - 2*pi)/h**2)*(x-xv[i])**2*(x-xv[i+1])
                return s
        
    if xv[-2] < x and x < xv[-1]:
        pn1 = Pi([xv[-2],xv[-1]],[yv[-2],yv[-1]])
        si = yv[-2] + d[-2]*(x-xv[-2]) + ((pn1 - d[-2])/(xv[-1]-xv[-2]))*(x-xv[-2])**2 + ((d[-1] + d[-2] - 2*pn1)/(xv[-1]-xv[-2])**2)*(x-xv[-2])**2*(x-xv[-1])
        return si

def generatedata(n, f, nodes="cheb", int=[-1, 1], endpoint=True):
    '''
    Genera puntos al azar
    ---------------------------
    n: Numero de puntos a generar
    nodes: Porque metodo los quieres
    int: Intervalo a generar
    endpoint: ni ideaxd
    '''
    if nodes=="cheb":
        dataxs = -np.cos(np.linspace(0, np.pi, n))
    else:
        dataxs = np.linspace(int[0], int[1], n, endpoint=endpoint) 
    
    datays = f(dataxs)
    return dataxs, datays

def lagrenge(x,xv,k):
    '''
    Polinomio de Lagrenge
    ------------------------
    x: Valor a evaluar
    xv: Lista de datos
    k: Subindice 
    ------------------------
    Salida: Lista de datos, con el resultado del polinomio
    '''
    if x in xv:
        xb = np.where(xv == x)[0]
        lx = 1 if xb == k else 0 
    else: 
        lx = 1
        for i in range(0, len(xv)):
            if k != i:
                lx = lx * ((x-xv[i])/(xv[k]-xv[i]))
    return lx

def poli_cardinal(xv, yv, npto=100):
    '''
    Interpolación de Legendre
    ---------------------------
    xv: conjunto de datos en x
    yv: Conjunto de datos en y
    --------------------------
    Salida: Conjunto de datos 
    '''
    n = len(xv)
    px = []
    x = np.linspace(xv[0],xv[-1], npto)
    for j in range(npto):
        p=0
        for k in range(n):
            # if k != j:
            p = p + yv[k]*lagrenge(x[j],xv,k)
        px.append(p)
    return x, px
    
def dif_div(xv, yv):
    '''
    Obtiene las constantes para el motodo de Newton
    ----------------------------------------
    xv: Datos en x
    yv: Datos en y
    ----------
    Devueve las constantes
    '''
    n = len(yv)
    coef = np.zeros([n, n])
    #Pone la primer columno los valores de la lsta yv
    coef[:,0] = yv
    
    for j in range(1,n):
        for i in range(n-j):
            #Remplaza los ceros por los valores de que saque la funcion
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1])/(xv[i+j]-xv[i])
            
    return coef

def pesos(dataxs):
    '''
    Encuentra los pesos para Interpolación baricentrica
    -----------------------------------------------------
    dataxs: Puntos de la base.
    ------------------
    Salida: Pesos
    '''
    n = len(dataxs)
    ws = np.ones(n)
    for k in range(n):
        for j in range(n):
            if j == k:
                continue
            ws[k] *= (dataxs[k]-dataxs[j])
    return 1/ws

def bary(dataxs, datays, x):
    '''
    Interpolación Baricentrica
    -------------------------------
    dataxs: Puntos en x
    datay puntos en y
    x: Punto a evaluar
    ------------------
    Devuelve f(x) -> y
    '''
    ws = pesos(dataxs)
    k = np.where(x == dataxs)[0]
    if len(k) == 0:
        nume = np.sum(ws*datays/(x-dataxs))
        denom = np.sum(ws/(x-dataxs))
        val = nume/denom
    else:
        val = datays[k[0]]
    return val


def polinomial_Newton(xv, yv, x):
    '''
    evaluar el polinomio de newton
    ------------------------------
    '''
    coef = dif_div(xv, yv)[0, :]
    n = len(xv) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -xv[n-k])*p
    return p

def si(xv,yv,x):
    '''
    Función de la recta
    --------------------
    xv: Datos de los puntos x(Dos puntos del intervalo donde estara una recta)
    yv: Datos y de los puntos (Lo mismo que el anterior)
    x: El punto a evaluar
    '''
    y = yv[0] + (yv[1]-yv[0])*(x-xv[0])/(xv[1]-xv[0])
    return y


def Interpolacion_lineal(xv,yv,x):
    '''
    Crea una interpolacion lineal, simulando la forma de la posiblefuncion, con rectas.
    -----------------------------------------------------------------------------------
    xv: conjunto de los datos en x de los puntos.
    yv: Conjunto de los datos en y de los puntos.
    ----------------------------------------------
    Salida: Puntos de una función lineal
    '''
    # Numero de datos
    n = len(xv)
    # Primero creamos un ciclo que se encarge de crear las funciones.
    #Para crear los subintervalos igual al numero de funciones (n-1) --> Funciones
    for i in range(n-1):
        if xv[i] < x and xv[i+1] > x:
            y = si([xv[i],xv[i+1]],[yv[i],yv[i+1]],x)
            return  y



def Constantes(xv,yv):
    '''
    Son las constantes ak y bk respectivamente.
    -----------------------------
    xv: Datos en x
    yv: Datos en y
    k: Subindice de las constante
    ---------------------------
    Salida: Devuelve las constantes
    '''
    n = xv.size
    m = n//2
    ak = np.zeros(m+1)  
    bk = np.zeros(m-1)
    for k in range(m+1):
        # ak[k] = yv @ np.cos(k * xv)/m
        ak[k] = np.sum(yv*np.cos(k*xv))/m
    for k in range(1, m):
        # bk[k-1] = yv @ np.sin(k * xv)/m # @ es una multiplicacion de matriz
        bk[k-1] = np.sum(yv*np.sin(k*xv))/m
    return ak, bk


def Interpo_trigo(xv,yv, nptos = 50):
    '''
    Interpolación Trigonometrica
    ----------------------
    xv: Datos en x
    yv: Datos en y
    nptos: Numero de puntos a evaluar
    -----------------------
    Salida: Conjunto de datos para x y Conjunto de datos generados en F(x)
    '''
    Polinomio = []
    X = np.linspace(xv[0],xv[-1],nptos)
    ak, bk = Constantes(xv,yv)
    n = len(ak)+len(bk)
    m = n//2
    for i in X:
        F = 0.5 * (ak[0] + ak[-1] * np.cos(m * i)) 
        for j in range(1,m):
            F = F + ak[j]*np.cos(j*i) + bk[j-1]*np.sin(j*i)           
        Polinomio.append(F)
    return X, Polinomio
    
def Gnormalfit(dataxs, datays, datasigs, fb,n = 1):
    '''
    Fitin con diferentes bases lineales
    ---------------------------------------
    dataxs: Puntos en x
    datays: Puntos en y
    datasigs: Chi
    fb: Base de la función
    n: Depende de la base
    --------------------------
    Salida: Regresion polinominal.
    '''
    N = dataxs.size
    A = np.zeros((N, n))  # notar la dimensión
    
    for k in range(n):
        A[:, k] = fb(n,k, dataxs)/datasigs  # A_{jk} = phi_k(x_j)/sigma_j
    bs = datays/datasigs  # b_j = y_j/sigma_j
    
    matI = A.T@A  # np.dot(A.T, A)
    InvmatI = np.linalg.inv(matI) 
    matD = A.T@bs
    cs = InvmatI@matD
    
    sigS = np.diagonal(InvmatI)
    chisq = np.sum((bs - A@cs)**2)  # (bs - A@cs).T@(bs - A@cs)
    
    return cs, chisq, sigS