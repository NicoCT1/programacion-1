# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:40:16 2025

@author: AULA
"""

sumatoria = 0
for k in range (1, 11):
    print(k, sumatoria)
    sumatoria += k
print("-----------------------")
print(f"el total de la sumatoria es: {sumatoria}")

# %%

num2 = [8, 7, 3, 4, 0, 9, 1, 2]

for n in range(len(num2)):
    print("posicion:", n)
    
for n in range(len(num2)):
    print(f"posicion: {n} - elemento: {num2[n]}")
    
# %%

estudiante = "Nicolas Cortes Trujillo"
s = 0

for letra in estudiante:
    if (letra=="o" or letra == "O" or letra == "ó"):
        s+=1
        
print("En su nombre hay", s, "Letras o")

# %%

num = int(input("Ingrese el valor al que desee obtener el factorial: "))
num3 = num
factorial = 1
for i in range({num}, 0, -1):
    if (num <=0):
        factorial= "num*(num-1)*(num-2)*(num-3)*(num-4)*(num-5)*(num-6)[num-(num-1)]"
print("el valor de la integral de", num3, "es de: ", factorial)