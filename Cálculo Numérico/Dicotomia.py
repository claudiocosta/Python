# -*- coding: utf-8 -*-
import numpy as np
from sympy import *
import matplotlib.pyplot as plt

__author__ = 'Claudio'

#------------  ACHA OS INTERVALOS ----------------
def findIntervals():
    for y in np.linspace(-20,20, 401):
        x1.append(y)
        y1.append(func(y))
        if func(y) >= 0 and func(y + 0.1) <= 0:
            intervals.append([y,y+0.1])
        elif func(y) <= 0 and func(y + 0.1) >= 0:
            intervals.append([y + 0.1,y])
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
intervals = []
i = 1
f = input('Digite a Função: ')
func = Lambda(x , f)        #função
pprint(func)
pp = 3#int(input('Precisão: '))   #precisão
p = 10**-pp   #precisão

findIntervals()
print(intervals)


#--------------DICOTOMIA-------------------------------

for n in intervals:
  xa = n[0]
  xb = n[1]
  xc = ((xa + xb) /2)
  i+=1
  data.clear()

  while  abs(func(xc)) >= p:
        xc = ((xa + xb) /2)
        line = ((round(xa,pp)), round(xb,pp), round(xc,pp), round(func(xc),pp))
        table.append(line)
        if func(xc) > 0 :
            xa = xc
        else:
            xb = xc
        print(line)
        if func(xc) <= p:
            x2.append(xc)
            y2.append(0)
        if func(xc) == 0 :
            break

  data = list(table)
  table = []
  pprint(data)

  plt.figure(i)
  plt.gca().xaxis.set_visible(False)
  plt.gca().yaxis.set_visible(False)
  columns = ('XA', 'XB', 'XC', "f(xc)")
  row_labels = ['%d' % x for x in range(len(data))]
  rows = len(data)
  cellText = []
  the_table = plt.gca().table(cellText=data,
                              colLabels=columns,
                              rowLabels=row_labels,
                              loc='center')
  plt.title('Dicotomia')

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