
import func as lf
import gggg as lab
from tkinter import *


root=Tk()
root.title('ЦОС')

def clicked():
    function = getattr(lf, selected.get())
    x,y=function()
    lab.dft(y)

def clicked1():
    function = getattr(lf, selected.get())
    x,y=function()
    lab.fft(y)


selected=StringVar()
selected.set('heaviside')
rad1=Radiobutton(root,text='Синус',value='sin',variable=selected).grid(column=0,row=0)
rad2=Radiobutton(root,text='Хивисайд',value='heaviside',variable=selected).grid(column=1,row=0)
rad3=Radiobutton(root,text='Дирак',value='dirac',variable=selected).grid(column=2,row=0)
rad4=Radiobutton(root,text='Случайный сигнал',value='rand_signal',variable=selected).grid(column=0,row=2)
rad5=Radiobutton(root,text='Прямоугольный импульс',value='rectangular',variable=selected).grid(column=1,row=2)
rad6=Radiobutton(root,text='Случайный цифровой',value='random_signal',variable=selected).grid(column=2,row=2)
rad7=Radiobutton(root,text='Шум',value='noise',variable=selected).grid(column=0,row=4)
rad8=Radiobutton(root,text='Радиоимпульс',value='radio_impulse',variable=selected).grid(column=1,row=4)
rad9=Radiobutton(root,text='Синус убывающий \n по экспоненте',value='exp',variable=selected).grid(column=2,row=4)
rad10=Radiobutton(root,text='sin(x)/x',value='sinc',variable=selected).grid(column=0,row=6)

but=Button(root,text='Draw DFT',command=clicked ).grid(column=0,row=8)
but=Button(root,text='Draw FFT',command=clicked1 ).grid(column=1,row=8)
root.mainloop()