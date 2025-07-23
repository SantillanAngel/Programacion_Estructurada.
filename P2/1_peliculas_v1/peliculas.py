def modificarPeliculas():
   borrarPantalla()
   print("\n\t.:: Modificar Películas ::. \n")
   pelicula_buscar=input("Ingrese el nombre de la película que desea buscar: ").upper().strip()#quita espacios 
   encontro=0
   if not(pelicula_buscar in peliculas): 
      print("\n\t\t ¡No se encuentra la película a buscar!")   
   else:   
      for i in range(0,len(peliculas)):
        if pelicula_buscar==peliculas[i]:
          resp=input("¿Deseas actualizar la pelicula? (Si/No) ").lower()
          if resp=="si":
            peliculas[i]=input("\nIntroduce el nuevo nombre de la película: ").upper().strip()
            encontro+=1
            print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      
      print(f"\nSe modifico {encontro} pelicula(s) con este titulo")

peliculas=[]

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()

def agregarPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  pelicula=input("Ingresa el nombre: ").upper().strip()
  peliculas.append(pelicula)
  input("\n\t\t\t :::LA OPERACION SE REALIZO CORRECTAMENTE:::")

def mostrarPeliculas():
  print(".:: Mostrar las Peliculas ::.")
  if len(peliculas)>0:
    for i in range(0,len(peliculas)):
      print(f"{i+1}:{peliculas}")
    else:
      print("\t .:: No hay peliculas en este momento en el Sistema ::.")

def limparPeliculas():
  borrarPantalla()
  print("\n\t.:: Limpiar o quitar TODAS las peliculas ::.")
  resp=input("¿Deseas borrar todas las peliculas del sistema?").lowe() .strip
  if resp=="si":
    peliculas.clear
    print("\n\t.:: LLa operacion fue ralizada con exito::.")

def buscarPeliculas():
  borrarPantalla()
  print("\n\t.::Buscar Peliculas::.")
  pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar").upper() .strip()
  if not(pelicula_buscar in peliculas):
    print("\n\t..::Esta pelicula a buscar no existe")
  else:
    encontro=0
    for i in range(0,len(peliculas)):
      if pelicula_buscar==peliculas [i]:
        print(f"la pelicula{pelicula_buscar} se encontro en el casillero{i+1}")
        encontro+=1
        print(f"n Tenemos{encontro} pelicula(s) con es titulo")
    print("La operacion se realizo con exito")

def modificarPeliculas():
  borrarPantalla()
  print("\n\t.::Modificar Peliculas::.")
  pelicula_modificar=input("Ingrese el nombre de la pelicula a modificar").upper() .strip()
  if not(pelicula_modificar in peliculas):
    print("\n\t..::Esta pelicula a modificar no existe")
  else:
    encontro=0
    for i in range(0,len(peliculas)):
      resp=input("Desea actualizar la pelicula?").lower()
      if resp=="si":
        peliculas[i]=input("Introduce el nombre de la pelicula").upper().strip
        encontro+=1
        print("La operacion se realizo con exito")
    print("Se modifico {encontro} pelicula con ese titulo")

def borrarPeliculas():
  borrarPantalla()
  print("\n\t.::Borrar  Peliculas::.")
  pelicula_buscar=input("Ingrese el nombre de la pelicula que desea borrar").upper() .strip()
  if not(pelicula_buscar in peliculas):
    print("\n\t..::Esta pelicula a borrar no existe")
  else:

    while pelicula_buscar in peliculas:
        resp=input("Desea Borrar la pelicula?").lower()
        if resp=="si":
          posicion=peliculas.index(pelicula_buscar)
          

          print("La pelicula que se borro fue {posicion}")
    print("Se modifico {encontro} pelicula con ese titulo")