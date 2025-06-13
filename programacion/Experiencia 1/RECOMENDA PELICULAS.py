# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 17:34:43 2025

@author: Nicolas
"""

    print("Bienvenidos, este es un recomendador de películas")
    print()
    
    peliculas = {
    "acci ́ón": ("Mad Max: Fury Road, John Wick, Gladiador, El agente invisible,"),
    "comedia": ("Ted, La m ́ascara, Ted 2, Borat, Proyecto x,"),
    "terror": ("El conjuro, IT, Halloween, La noche del demonio"),
    "drama": ("Forrest Gump, En busca de la felicidad, El padrino,"),
    "ficcion": ("Los vengadores, Los vengadores infinity war, Los vengadores endgame")
    }
    print( )
    eleccion = input("Seleccione un genero entre: Acción, Comedia, Terror, Drama y Ficcion: ").lower()
    print()
    
    
    match eleccion:
        case "acción":
            print("Te recomiendo las peliculas: ", peliculas ["acción"])
            if eleccion == "acción":
                acción = input ("Selecciona una pelicula de acción: ")
            match acción:
                case "Mad Max: Fury Road":
                    print("Fecha de estreno: 14 / 05 / 2015")
                case "John Wick":
                    print("Fecha de estreno: 25 / 12 / 2014")
                case "Gladiador":
                    print("Fecha de estreno: 05 / 05 / 2000")
                case "El agente invisible":
                    print("Fecha de estreno: 22 / 07 / 2022")
                    
        case "comedia":
            print("Te recomiendo las peliculas: ", peliculas ["comedia"])
            if eleccion == "comedia":
                comedia = input ("Selecciona una pelicula de comedia: ")
            match comedia:
                case "Ted":
                    print("Fecha de estreno: 29 / 06 / 2012")
                case "La m ́ascara":
                    print("Fecha de estreno: 29 / 07 / 1994")
                case "Ted 2":
                    print("Fecha de estreno: 26 / 06 / 2015")
                case "Borat":
                    print("Fecha de estreno: 02 / 11 / 2006")
                case " Proyecto x":
                    print("Fecha de estreno: 19 / 06 / 2012")
                    
        case "terror":
            print("Te recomiendo las peliculas: ", peliculas ["terror"])
            if eleccion == "terror":
                terror = input ("Selecciona una pelicula de terror: ")
            match terror:
                case "El conjuro":
                    print("Fecha de estreno: 19 / 07 / 2013")
                case "IT":
                    print("Fecha de estreno: 08 / 09 / 2017")
                case "Halloween":
                    print("Fecha de estreno: 25 / 10 / 1978")
                case "La noche del demonio":
                    print("Fecha de estreno: 01 / 04 / 2011")
                    
        case "drama":
            print("Te recomiendo las peliculas: ", peliculas ["drama"])
            if eleccion == "drama":
                drama = input ("Selecciona una pelicula de drama: ")
            match drama:
                case "Forrest Gump":
                    print("Fecha de estreno: 06 / 07 / 1994")
                case "En busca de la felicidad":
                    print("Fecha de estreno: 23 / 02 / 2007")
                case "El padrino":
                    print("Fecha de estreno: 24 / 03 / 1972")
                    
        case "ficcion":
            print("Te recomiendo las peliculas: ", peliculas ["ficcion"])
            if eleccion == "ficcion":
                ficcion = input ("Selecciona una pelicula de ficcion: ")
            match ficcion:
                case "Los vengadores":
                    print("Fecha de estreno: 27 / 04 / 2012")
                case "Los vengadores infinity war":
                    print("Fecha de estreno: 25 / 04 / 2018")
                case "Los vengadores endgame":
                    print("Fecha de estreno: 25 / 04 / 2019")
        case _: print("Lo siento, no tengo recomendaciones para ese g ́enero.")
