import math
import numpy as np




def sin(N=1024):
    x=np.around(np.linspace(0,2*math.pi,N),decimals=4)
    y=np.array([math.sin(i) for i in x])
    return x,y

def dirac(t=0, N=1024):
    x=np.arange(-10,10,20/N)
    y = np.where(x==t,1,0)
    return x,y

def heaviside(t=0, N=1024):
    x = np.around(np.linspace(-10, 10, N), decimals=4)
    y=np.where(x<t,0,1)
    return x,y

def rand_signal(N=1024):
    x = np.around(np.linspace(-10, 10, N), decimals=4)
    y = np.array([np.random.randint(-1000,1000)/1000 for i in x])
    print(y)
    return x,y

def rectangular(duty=50,N=1024):
    x = np.around(np.linspace(0, N, N), decimals=4)
    y = np.array([(i < (N )*(duty/100)) for i in x], dtype=int)
    return x,y

def random_signal(N=1024):
    x = np.arange(0,N)
    y = np.array([np.random.randint(0, 2) for i in x])
    print(y)
    return x,y

def noise (fun=sin(), proz=50, N=1024):
    ns = np.random.normal(0, 0.1, N)
    x, y = fun
    y += (proz/100) * ns
    return x,y

def radio_impulse(N=1024):
    k = int(N / 3)
    x = np.arange(0, N, 1)
    y = np.where(x > k,   np.sin(5 * 2 * np.pi * x / k), 0) + np.where(x > 2 * k,- np.sin(2 * 5 * np.pi * x / k), 0)
    return x, y

def exp(q=5, sl=0.005,N=1024):
    x = np.arange(0, N, 1)
    y = np.array([q * np.exp(-sl * i) * np.sin(10 * 2 * np.pi * i / N) for i in x])
    return x,y

def sinc(N=1024):
    x = np.around(np.linspace(-5 * math.pi, 5 * math.pi, N),decimals=8)
    y = [(math.sin(x) / x) for x in x]
    return x, y
