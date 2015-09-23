# -*- coding: utf-8 -*-
#!/usr/bin/env python
import pylab as pl
import numpy as np
from sympy import *
import matplotlib.pyplot as plt

__author__ = 'Claudio'

#------------  ACHA OS INTERVALOS ----------------
def findKick():
    for y in np.linspace(-20,20, 401):
        x1.append(y)
        y1.append(func(y))
        if (func(y) >= 0 and func(y + 0.1) <= 0) or (func(y) <= 0 and func(y + 0.1) >= 0):
            kicks.append(y)
        if(func(y) == 0):
            x2.append(y)
            y2.append(0)
#-------------------------------------------------

x = symbols('x') #define 'x' como um simbolo para as funções
x1 = []
y1 = []
x2 = []
y2 = []
line = ()
table = []
data = []
xa = 0
xb = 0
xc = 1000
kicks = []
i = 0

f = input('Digite a Função: ' )
func = Lambda(x , f)        #função
dfunc = Lambda(x, diff(f)) # derivada da função
pprint(func)                 # x**3 - 5 * x**2 + 8 * x - 4
pprint(dfunc)
pp = 5#int(input('Precisão: '))   #precisão
p = 10**-pp   #precisão

findKick()
print(kicks)

#------------Newton_Raphson------------------------

for k in kicks:
    x = k

    i += 1
    data.clear()

    line = (round(x,pp), round(func(x),pp), round(dfunc(x),pp) )
    table.append(line)

    while abs(func(x)) > p:
        try:
            x = (x - func(x) / dfunc(x))
        except ZeroDivisionError:
            print('Derivada da função igual a zero')
        else:
            line = (round(x,pp),round(func(x),pp),round(dfunc(x),pp)) #line = (chute, func(chute) ,dfunc(chute))
            table.append(line)
            if abs(func(x)) <= 0.1:
                x2.append(x)
                y2.append(func(x))

    data = list(table)
    table = []
    pprint(data)

    plt.figure(i)
    plt.gca().xaxis.set_visible(False)
    plt.gca().yaxis.set_visible(False)
    columns = ('Valor', 'f(x)', "f'(x)")
    row_labels = ['%d' % x for x in range(len(data))]
    rows = len(data)
    cellText = []
    the_table = plt.gca().table(cellText=data,
                                  colLabels=columns,
                                  rowLabels = row_labels,
                                  loc='center')
    plt.title('Newton_Raphson')


#---------------------Grafico---------------------------------------------
plt.figure(0)
plt.title('Função '+ f)
plt.plot(x1, y1)
plt.plot([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])
plt.plot([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
plt.axis([-10, 10, -10, 10])
plt.grid(true)
plt.plot(x2 , y2, 'ro')

plt.show()