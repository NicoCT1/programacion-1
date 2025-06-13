# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 19:38:40 2025

@author: corte
"""
print
lista = [5, 4, 2, -4, 0, 20, 50, 1, -100, 9]


for n in lista:
    if n <= 0:
        print(f"{n} es menor que 1")
    if n == 1:
        print(f"{n} es igual a 1")
    if n > 1:
        print(f"{n} es mayor que 1")
        
print("\n")
print("la cantidad de numeros es: ")
print(len(lista))
# %%
p = 0
n = 0
arroba = 0
punto = 0
correo_1 = 0

correo = input("Ingrese un correo electronico:\n")

for s in correo:
    if s == "@":
        arroba = 1
    if s == ".":
        punto = 1
if arroba and punto:
    correo_1 = 1
    
for s in correo:
    if (s == "."):
        p+=1
    if (s .isdigit()):
        n+=1

if correo_1 > 0:
    print("El correo si es valido.")
else:
    print("El correo no es valido")
print(f"La cantidad de puntos es: {p}")
print(f"La cantidad de numeros es: {n}")

# %%

num_cuadrado = 0
num_par = 0
num_primo = 0

numero = int(input("Ingrese un numero: "))

for n in numero:
    if n 













# %%
palindromo = 0
palabra = input("Ingrese una palabra: ") .lower()

for n in range(0, len (palabra)//2):
    if palabra [n] == palabra[len(palabra)-1-n]:
        palindromo +=1
    if palindromo > 0:
        print("Es un palíndromo.")
    else:
        print("No es un palindromo.")