#proyecto 1 crear un proyecto que permita  gestionar (administrar peliculas) colocar un menu de opciones para agregar: crear, borrar, modificar, consultar, buscar y modificar peliculas

#notas: 
# 1 utilizar funciones y mandar llamar desde otro archivo
#2 utilizar una lista para almacenar los nombres
import os
os.system("cls")
import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Crear Peliculas \n 2.- Borrar Peliculas \n 3.- Mostrar Peliculas \n 4.-Buscar Peliculas \n 5.- Modificar Peliculas \n 6.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.buscarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "6":
            opcion=False    
            print(f"\n\"Terminaste la ejecucion del SW")
        case _: 
            input(f"\n\"Opción invalida vuelva a intentarlo ... por favor")