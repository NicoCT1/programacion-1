# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 07:13:25 2025

@author: corte
"""

saldo = 1000  # Saldo inicial
    
while True:
    print("\nCajero Automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
        
    opcion = input("Seleccione una opción: ")
        
    if (opcion == "1"):
        print(f"Su saldo actual es: ${saldo}")
        
    elif (opcion == "2"):
        monto = float(input("Ingrese la cantidad a retirar: "))
        if (monto > saldo):
            print("Fondos insuficientes.")
        else:
            saldo -= monto
            print(f"Ha retirado ${monto}. Su saldo actual es: ${saldo}")
        
    elif (opcion == "3"):
        monto = float(input("Ingrese la cantidad a depositar: "))
        saldo += monto
        print(f"Ha depositado ${monto}. Su saldo actual es: ${saldo}")
        
    elif (opcion == "4"):
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break

            
# %%
            
while True:
        print("Conversor de Temperatura")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if (opcion == "1"):
            celsius = float(input("Ingrese la temperatura en Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")
        
        elif (opcion == "2"):
            fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F equivale a {celsius:.2f}°C")
        
        elif (opcion == "3"):
            print("Gracias por usar el conversor... Hasta luego")
            break
