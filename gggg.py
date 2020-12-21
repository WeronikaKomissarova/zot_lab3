import numpy as np
import matplotlib.pyplot as plt
from math import atan2, sqrt, pi
from cmath import exp
import time


def DFT_dot(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n1 = np.arange(N)
    k1 = np.arange(N/2)
    M = [[np.exp(-2j * np.pi * k * n / N) for n in n1 ] for k in k1]
    return np.dot(M, x)

"""
def FFT_dot(x):
    start=time.time()
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if np.log2(N) % 1 > 0:
        raise ValueError("размер вектора должен быть кратен 2")


    N_min = min(N, 32)

    # Perform an O[N^2] DFT on all length-N_min sub-problems at once
    n = np.arange(N_min)
    k = np.arange(N_min/2)[:, None]
    M = [np.exp(-2j * np.pi * n * k / N_min) for n in n1] for k in k1
    X = np.dot(M, x.reshape((N_min, -1)))

    # build-up each level of the recursive calculation all at once
    while X.shape[0] < N:
        X_even = X[:, :int(X.shape[1] / 2)]
        X_odd = X[:, int(X.shape[1] / 2):]
        factor = np.exp(-1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])
    end=time.time()
    print('time for dot:', end-start)
    return X.ravel()


def FFT_dot(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]


    if N == 1 :
        return x
    else:
        X_even = FFT_dot(x[::2])
        X_odd = FFT_dot(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)

        print('ev', np.shape(X_even), '  od', np.shape(X_odd), '  f', np.shape(factor), 'N', N)
        print(factor)
        return np.concatenate([X_even + factor[:int(N/2 )] * X_odd,
                               X_even + factor[int(N/2 ):] * X_odd])
"""
def FFT_dot(x):
    N = len(x)
    if N == 1:
        return np.asarray([x[0]])
    X = [None] * N
    even = FFT_dot(x[:N:2])
    odd = FFT_dot(x[1:N:2])
    for k in range(N // 2):
        w = exp(-2j * pi * k / N)
        X[k] = even[k] + w * odd[k]
        X[k + N // 2] = even[k] - w * odd[k]
    return np.asarray(X)

def en(y):
    return np.sum(np.array([x ** 2 for x in y])) * 0.01

def calc_spectr(sp, e_min):
    f = np.vectorize(sqrt)
    f2 = np.vectorize(atan2)
    a = f ( np.where ((sp.real ** 2 + sp.imag ** 2) < e_min , 0 , sp.real ** 2 + sp.imag ** 2))
    phi= - f2 ( sp.imag , sp.real ) * 180 / pi
    for i in np.where(a == 0):
        phi[i] = 0
    return a, phi

def draw(a, phi):
    fig, axes = plt.subplots(1, 2)
    axes[0].bar(np.arange(len(a)), a)
    axes[1].bar(np.arange(len(phi)), phi)
    plt.show()

def drawlab(a, phi,title):
    plt.title(title)
    fig, axes = plt.subplots(1, 2)
    axes[0].bar(np.arange(len(a)), a)
    axes[1].bar(np.arange(len(phi)), phi)
    plt.show()

def fft(x, lab=False, title =''):
    start = time.time()
    spectrum = FFT_dot(x)
    e_min = en(x)
    a, phi = calc_spectr(spectrum[:len(spectrum)//2], e_min)
    end = time.time()
    print('time fft: ', end - start)
    return a, phi

def dft(x):
    start = time.time()
    spectrum = DFT_dot(x)
    e_min = en(x)
    a, phi = calc_spectr(spectrum, e_min)
    return a,phi


