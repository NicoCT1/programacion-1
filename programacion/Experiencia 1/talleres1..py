# Taller Programa 1

valor =  int(input("ingrese un valor"))
if (valor == 0):
  print("el numero es cero")
  if (valor % 2 == 0):
      print("el numero es par")
  else:
      if(valor % 2 != 0 < 0):
          print("el numero es negativo impar")
else:
      if(valor < 0):
        print("el numero es negativo")
      else:
        print("el numero es positivo")
          
# Taller Programa 2  #1

valor1 = int(input("Ingresar un valor: "))

if(valor1 > 0):
  valor2 = int(input("Ingresar un nuevo valor: "))
  suma = valor2 + valor1
  producto = valor2 * valor1
  resta = valor2 - valor1
  print("La suma es: ", suma)
  print("El producto es: ", producto)
  print("La resta es: ", resta)
else:
  print("Fin del programa.")
  
  #2
  
valor1 = int(input("Ingresar un valor entero: "))
valor2 = int(input("Ingresar un otro valor entero: "))

if(valor1 > valor2):
  print("El primer valor es mayor")
else:
  print("El segundo valor es mayor")
  
  #3
  
valor1 = int(input("Ingresar un valor entero: "))
valor2 = int(input("Ingresar un otro valor entero: "))
valor3 = int(input("Ingresar uno más: "))

if(int(valor1 > valor2 and valor1 > valor3)):
  print("El primer valor es mayor")
else:
  if(int(valor2 > valor1 and valor2 > valor3)):
    print("El segundo valor es mayor")
  else:
    if(int(valor3 > valor1 and valor3 > valor2)):
      print("El tercer valor es mayor")
    else:
      print("Los tres valores son iguales")
      
 #4
 
valor1 = int(input("Ingresar un valor entero: "))
valor2 = int(input("Ingresar un otro valor entero: "))
valor3 = int(input("Ingresar uno más: "))
valor4 = int(input("Ingresar uno más por favor: "))

if(int(valor1 > valor2 and valor1 > valor3 and valor1 > valor4)):
  print("El primer valor es mayor")
else:
  if(int(valor2 > valor1 and valor2 > valor3 and valor2 > valor4)):
    print("El segundo valor es mayor")
  else:
    if(int(valor3 > valor1 and valor3 > valor2 and valor3 > valor4)):
      print("El tercer valor es mayor")
    else:
        if(int(valor4 > valor1 and valor4 > valor2 and valor4 > valor3)):
          print("El cuarto valor es mayor")
        else:
            print("Los tres valores son iguales")
            
 #5
 
 temperatura = int(input("Ingresar la temperarura de el agua: "))
 
 if (temperatura < 0):
     print("El agua está en estado solido")
 else:
     if (temperatura > 0 and temperatura < 100):
         print("El agua está en estado liquido")
     else:
             if (temperatura > 100):
                 print("El agua está en estado gaseoso")

 #6
