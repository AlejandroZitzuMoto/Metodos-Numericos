import numpy as np

def D_simp(a,h,f, d = True, i = False):
    df = (f(a+h)-f(a))/h if d else (f(a) - f(a+h))/h
    return df

def D_central(x,h,f):
    return (f(x+h/2) - f(x-h/2))/h


def Seg_derivada(x,h,f):
    return (f(x[0]+h/2)+f(x[1]-h/2)-2*f(x[2]))/h**2

def I_rectangular(w,f, Ni = 10):
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    x = np.linspace(x0[0],x0[1], Ni)
    I_R = 0
    for i in range((Ni-1)):
         I_R = I_R + f(x[i])*h 
    return I_R

def I_trapecio(w, f, Ni = 20):
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    I_T2 = 0
    x = np.linspace(x0[0],x0[1],Ni)
    I_T = h*f(x[0])/2
    I_T3 = h*f(x[-1])/2
    for i in range(0,len(x)-2):
        I_T2 = I_T2 + f(x[i+1])*h
    return (I_T+I_T2+I_T3)

def I_pmedio(w,f,Ni=50):
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    x = np.linspace(x0[0],x0[1],Ni)
    I_pm = 0
    for i in range(len(x)-2):
        x1 = (x[i] + x[i+1])/2
        I_pm = I_pm + f(x1)*h
    return I_pm

def I_Sim13(w,f,Ni = 15):    
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    x = np.linspace(x0[0],x0[1],Ni)
    I_S2, I_S4 = 0, 0
    for i in range(0,len(x)-1):
        if i%2 == 0:
            I_S2 = I_S2 + f(x[i])*(2*h/3)
        else:
            I_S4 = I_S4 + f(x[i])*(4*h/3)
   
    I_S3 = (h/3)*(f(x[0]) + f(x[-1]))
    return (I_S4 + I_S3 + I_S2)

def I_Sim18(w,f,Ni = 51):
    x0 = [float(w[i]) for i in range(2)]
    h = (x0[1] - x0[0])/(Ni -1)
    x = np.linspace(x0[0],x0[1],Ni)
    I_S38 = (3*h/8)*(f(x[0]) + f(x[-1]))
    I_S33, I_S32 = 0,0
    for i in range(0,len(x-1)):
        if i%3 == 0:
            I_S32 = I_S32 + (6*h/8)*f(x[i])
        else:
            I_S33 = I_S33 + (9*h/8)*f(x[i])
            
    return (I_S38 + I_S33 + I_S32)

def I_Gauss(c,a,xr, f,n =2):
    I_G = 0
    for i in range(1,n):
        I_G = I_G + c[i]*f((a[1]+a[0])/2 + (a[1]-a[0])*xr[i]/2)
    return ((a[1]-a[0])*I_G)/2

