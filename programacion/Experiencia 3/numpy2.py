# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

##importamos librerias necesarias para el codigo

import numpy as np
import matplotlib.pyplot as plt

matriz = np.zeros([4,4])
matriz

matriz1 = np.ones([4,4])
matirz1

matriz [1,1] = 4

for fila in matriz:
    for columna in fila:
        if (fila == columna):
            matriz[fila,columna] = 1
            
a = matriz.shape
a[0]

for fila in range(matriz.shape[0]):
    for columna in range(matriz[fila].shape[0]):
        print("fila: ",fila, "columna: ", columna)
        if (fila == columna):
            matriz[fila,columna] = 1


matriz3 = np.zeros([4,4])

matriz3

for fila in range(matriz3.shape[0]):
    for columna in range(matriz3[fila].shape[0]):
        print("fila: ",fila, "columna: ", columna)
        if fila == 0:
            fila += 3
        if columna == 0:
            columna += 3
        if fila == 1:
            fila += 3
        if columna == 1:
            columna += 3
            if fila + columna == 6:
               matriz3[fila,columna] = 1
matriz3 
            