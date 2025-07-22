#Proyecto 3
#Crear un proyecto  que permita  gestionar (administrar) calificaciones, colocar  un menu  de opciones para agregar,  mostrar, calcular promedios 
#de calificaciones de los alumnos y salir
# Notas:

#1.- Utiliza  funciones y mandar a llamar desde otro archivo 
#2.- Utilizar listas  para almacenar  el nombre de un alumno y 3 clasificaciones  
import calificaciones

def main():
    datos = []  

    opcion=True
    while opcion:
     calificaciones.borrar_pantalla()
     opcion=calificaciones.menu_principal()

     match opcion:
        case "1":  
            calificaciones.agregar_calificaciones(datos)
            calificaciones.esperarTecla()
        case "2":
            calificaciones.mostrar_calificaciones(datos)
            calificaciones.esperarTecla() 
        case "3":
            calificaciones.calcular_promedios(datos)
            calificaciones.esperarTecla()   
        case "4":
            opcion=False    
            calificaciones.borrarPantalla()
            print(" Terminaste la ejecucion del SW")
        case _:
            opcion=True 
            print("Opción invalida vuelva a intentarlo") 
            calificaciones.esperarTecla()

if __name__ == "__main__":
    main()