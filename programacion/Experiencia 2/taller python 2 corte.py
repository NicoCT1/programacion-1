# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 18:53:25 2025

@author: cortes
"""
numeros_pares = 0
    
while (numero != -1):
    numero = int(input("Ingrese un número entero positivo : "))
        
    if (numero == -1:)
        break
            
    if (numero > 0):

        suma = 0
        temp = numero
        while (temp > 0):
            digito = temp % 10
            suma += digito
            temp = temp // 10
        print(f"Suma de dígitos de {numero}: {suma}")
            
        if (numero % 2 == 0):
                numeros_pares += 1
    
print(f"\nTotal de números pares ingresados: {numeros_pares}")

# %%


total = 0.0
    
while True:
        monto = float(input("Ingrese el monto de la compra (0 para terminar): "))
        
        if (monto == 0):
            break
        elif (monto < 0):
            print("Monto no válido. Ingrese un valor positivo.")
            continue
        else:
            total += monto
    
if (total > 1000):
        descuento = total * 0.10
        total -= descuento
        print(f"\nSe aplicó un descuento del 10% (${descuento:.2f})")
    
print(f"\nTotal a pagar: ${total:.2f}")



# %%


numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
    
print(f"\nTabla de multiplicar del {numero}:")
print("-----------------------------")
print("Multiplicando | Multiplicador | Producto")
print("---------------------------------------")
    
multiplicador = 1
while (multiplicador <= 10):
    producto = numero * multiplicador
    print(f"{numero:12} | {multiplicador:12} | {producto:8}")
    multiplicador += 1



# %%


numero = int(input("Ingrese un número para iniciar la secuencia: "))
print("Secuencia:", end=" ")
    
while (numero != 1):
    print(numero, end=" ")
    if numero % 2 == 0: 
        numero = numero // 2
    else:  
        numero = 3 * numero + 1
    
print(1)  



# %%


print("Juego de Piedra, Papel o Tijera")
print("Opciones válidas: piedra, papel, tijera")
    
while True:
    jugador1 = input("Jugador 1, ingrese su jugada: ").lower()
    jugador2 = input("Jugador 2, ingrese su jugada: ").lower()
        
    if jugador1 not in ["piedra", "papel", "tijera"] or jugador2 not in ["piedra", "papel", "tijera"]:
        print("Jugada no válida. Intente nuevamente.")
        continue
            
    if jugador1 == jugador2:
        print("Empate! Jueguen nuevamente.")
        continue
            
    match (jugador1, jugador2):
        case ("piedra", "tijera") | ("papel", "piedra") | ("tijera", "papel"):
                print("Ganador: jugador 1")
        case _:
                print("Ganador: jugador 2")
        
    break 

