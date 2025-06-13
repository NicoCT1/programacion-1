# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 17:14:19 2025

@author: corte
"""

def chatbot():
    print("¡Hola! Bienvenido al generador de imágenes digitales.")
    print("¿En qué te puedo ayudar hoy?")
    print("1. Quiero solicitar una imagen")
    print("2. Quiero hablar con un asesor")
    
    opcion = input("Escribe 1 o 2 según lo que deseas hacer: ")
    
    if opcion == "1":
        datos = {}
        datos["nombre"] = input("Por favor, dime tu nombre: ")
        datos["correo"] = input("Escribe tu correo electrónico: ")
        datos["descripcion"] = input("Describe la imagen que quieres crear: ")
        
        print("\nGracias por tu solicitud. Aquí está un resumen:")
        for k, v in datos.items():
            print(f"{k.capitalize()}: {v}")
        
        print("\nTu solicitud ha sido enviada al sistema. ¡Gracias!")
        return datos
    
    elif opcion == "2":
        print("Un momento por favor, te conectamos con un asesor humano...")
        print("Puedes escribirnos directamente a soporte@digitalart.com o en nuestro WhatsApp: +123456789")
    
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        chatbot() 


# %%

import os

def soli_ima_pers():
    print("Bienvenido al sistema de solicitud de imagen personalizada.")
    
    cliente = {}
    cliente["nombre"] = input("¿Cuál es tu nombre?: ")
    cliente["correo"] = input("¿Cuál es tu correo electrónico?: ")
    cliente["descripcion_deseada"] = input("Describe cómo te gustaría que sea transformada la imagen: ")
    
    ruta_imagen = input("Por favor, indica la ruta de la imagen que deseas subir (ej: ./imagen.jpg): ")
    
    if not os.path.exists(ruta_imagen):
        print(" La ruta proporcionada no existe. Por favor verifica e intenta de nuevo.")
        return None
    
    cliente["ruta_imagen"] = ruta_imagen
    
    print(" Resumen de tu solicitud:")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Correo: {cliente['correo']}")
    print(f"Transformación deseada: {cliente['descripcion_deseada']}")
    print(f"Imagen subida: {cliente['ruta_imagen']}")
    
    print("\nTu solicitud será procesada. Gracias por usar nuestro servicio.")
    
    return cliente


# %%

artistas = ["Nicolas", "Roger", "Wilfredo", "Felipe", "Miller"]

def asignar_artista():
    print("Se ha recibido una solicitud de imagen personalizada.")
    
    for artista in artistas:
        print(f" Notificando a {artista} sobre un nuevo encargo...")
        print("Detalles del pedido: Ilustración estilo anime, fondo personalizado.")
        decision = input(f"{artista}, ¿deseas aceptar el encargo? (si/no): ").lower()
        
        if decision in ["si", "acepto"]:
            print(f" {artista} ha aceptado el encargo.")
            print("Se le notificará al cliente que su pedido ya fue asignado a un artista.")
            
            inquietud = input("¿Deseas hacerle alguna pregunta al cliente? (si/no): ").lower()
            if inquietud == "si":
                print("Puedes comunicarte con el cliente al correo: ana@example.com")
            print(" El encargo está en curso.")
            return  

        else:
            print(f"{artista} rechazó el encargo.")
            print("Se intentará con otro artista...")
    
    print(" Ningún artista disponible aceptó el encargo.")
    print(" Se le notificará al cliente que su pedido está en espera.")

                
                
# %%
                
def admin():
    agregar = input("Si quieres agregar un nuevo catalogo digíta si")
    if agregar == "si":
        print("¿Como quiere llamar su nuevo catálogo?")
        
        nuevo_cata = {}
        print(f"¿Que quiere que tenga {nuevo_cata} en sus productos?")
        
        nuevo_cata["primer_producto"] = input("Descripcion del primer producto") 
        nuevo_cata["segundo_producto"] = input("Descripcion del nuevo producto") 
        nuevo_cata["tercer_producto"] = input("Descripcion del nuevo producto") 
        
        print("catalogo creado exitosamente con los siguientes productos: ")
        
        for producto in nuevo_cata:
            print(f"producto 1: {nuevo_cata['primer producto']}")
            print(f"producto 2: {nuevo_cata['segundo producto']}")
            print(f"producto 3: {nuevo_cata['tercer producto']}")
            
    else:
        print("Cancelaste la creación del catálogo")
        
        
# %%

def satisfaccion():
    print("Califica de uno a 10 como fue tu experiencia")
    print("¿Estas satisfecho con los siguientes aspectos?:")
    calidad = int(input("Calidad del arte: "))
    atencion = int(input("Atencion al cliente por parte de los asesores: "))
    tiempo = int(input("El tiempo que tardó el artsta en entregar su pedido: "))
    recomendacion = int(input("¿De 1 a 10, que tanto recomendaria nuestros servicios asus conocidos?"))
    
    if calidad + atencion + tiempo + recomendacion <= 5:
        print("Lamentamos la mala experiencia que recibio, como recompensa, tendrá un 7% de descuento en su proximo pedido")
    else:
        print("agradecemos su cinceridad, vuelva pronto a solicitar nuestros servicios para recibir descuetos extraordinarios")
   









# %%

chatbot()                
                
                
                
                
                
                
                
                
                
                
                
                
