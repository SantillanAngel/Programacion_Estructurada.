import agenda

def main():
    datos = {}  

    opcion=True
    while opcion:
     agenda.borrarPantalla()
     opcion=agenda.menu_principal()

     match opcion:
        case "1":  
            agenda.agregar_contacto(datos)
            agenda.esperarTecla()
        case "2":
            agenda.mostrar_contacto(datos)
            agenda.esperarTecla() 
        case "3":
            agenda.buscar_contacto(datos)
            agenda.esperarTecla()
        case "4":
            agenda.modificar_contacto(datos)
            agenda.esperarTecla()
        case "5":
            agenda.eliminar_contacto(datos)
            agenda.esperarTecla()  
        case "6":
            opcion=False    
            agenda.borrarPantalla()
            print(" Terminaste la ejecucion del SW")
        case _:
            opcion=True 
            print("Opción invalida vuelva a intentarlo") 
            agenda.esperarTecla()

if __name__ == "__main__":
    main()
 