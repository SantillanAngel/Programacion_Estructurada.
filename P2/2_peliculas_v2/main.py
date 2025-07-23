#Crear un proyecto  que permita  gestionar (administrar películas); colocar  un menu  de opciones para agregar, borrar,  modificar, consultar, buscar y vaciar películas 
#Notas: 
#1.-utiliza  funciones y mandar a llamar desde otro archivo 
#2.- Utilizar dict  para almacenar  los siguentes atrivutos (nombre, categoria, clasificacion, genero,idioama de la película, )

import peliculas

opcion=True
while opcion:
    peliculas.borra_pantalla()
    print("\n\t🍿..::: CINEPOLIS CLON :::... 🍿")
    print("\t🎬..::: Sistema de Gestión de Películas :::... 🎬\n")
    print(" 1️⃣.- Crear 📁")
    print(" 2️⃣.- Borrar 🗑️")
    print(" 3️⃣.- Mostrar 🖼️")
    print(" 4️⃣.- Agregar una característica ➕")
    print(" 5️⃣.- Modificar característica 🔧")
    print(" 6️⃣.- Borrar característica ❌")
    print(" 7️⃣.- SALIR 🚪")
    opcion = input("\t🎞️ Elige una opción: ").upper()


    match opcion:
        case "1":
            peliculas.crear_peliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrar_peliculas()
            peliculas.esperarTecla() 
        case "3":
            peliculas.mostrarPeliculas()   
            peliculas.esperarTecla()
        case "4":
            peliculas.agreagarCaracteristicaPeliculas() 
            peliculas.esperarTecla() 
        case "5": 
            peliculas.modificarCaracteristcaPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
            peliculas.esperarTecla()
            print("/n\tTerminaste la ejecucion del SW")
        case _:
            opsion=True 
            input("Opción invalida vuelva a intentarlo ... por favor")