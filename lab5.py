import func
import numpy as np
import gggg
import matplotlib.pyplot as plt
import math


N=8192

def sinc(x):
    if x==0:
        return 1
    else:
        return math.sin(x*math.pi)/(x*math.pi)

def create_signal():
    _,sinexp = func.exp(N=N)
    _,sin = func.sin(N=N)
    _,sinc = func.sinc(N=N)
    return np.arange (len(sinc)),sinexp+sin+sinc

def draw(x1, signal, a, phi, title,i):
    plt.figure(i)
    fig, axes = plt.subplots(1, 3)
    axes[2].plot(x1,signal)
    plt.title(title)
    axes[0].bar(np.arange(len(a)), a)
    axes[1].bar(np.arange(len(phi)), phi)

    plt.show()

def nyq_freq(a):
    c=np.where(a!=0)
    return c[-1][-1]


def nyquist(x_data,y_data, dot): #передаю дискретизированный сигнал
    space = x_data[1] - x_data[0]
    dots = dot * len(x_data)
    x_result = list(np.linspace(x_data[0], x_data[-1] + space, dots))
    print('x_result ', len(x_result))

    y_result = [0] * len(x_result)
    for index in range(len(x_data)):
        x, y = x_data[index], y_data[index]
        for n in range(len(x_result)):
            x_n = x_result[n]
            y_n = y * sinc((x_n - x) / space)
            y_result[n] += y_n

    return x_result, y_result


def lab():
    x,y=create_signal()
    a,phi = gggg.fft(y)
    print('max freq in A: ', nyq_freq(a))
    interpolation = 128
    #draw(x,y,a[:500],phi[:500],'Оригинальный сигнал',0)

    dt = int(input("Введите шаг дискретизации:  "))

    x_disk = x[::dt]
    y_disk = y[::dt]
    print(y_disk)

    X_res,Y_res = nyquist(x_disk,y_disk,interpolation)
    a_res,_=gggg.fft(Y_res)

    fig, axes = plt.subplots(2, 2)
    axes[0][0].bar(np.arange(len(a[:500])), a[:500])
    axes[0][1].plot(x,y)
    axes[0][1].title.set_text('Оригинальный сигнал')
    axes[1][0].bar(np.arange(len(a_res[:500])), a_res[:500])
    axes[1][1].plot(X_res, Y_res)
    axes[1][1].title.set_text('Восстановленный сигнал')

    #draw(X_res,Y_res,a_res[:500],phi_res[:500],'Восстановленный сигнал', 1)

    plt.show()

lab()