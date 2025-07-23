calificaciones=[]

#lista=[
 #  ["Eduardo", 10.0, 10.0, 10.0],
  # ["Joel", 10.0, 9.8, 8.5],
   #["Ruben", 5.0, 6.0, 7.0]
#]

def borrar_pantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar...")

def menu_principal():
    print("\n\t 📚 ..::: Sistema de Gestión de Calificacones  :::... 📚 \n\n 1️⃣.- Agregar 📥 \n 2️⃣.- Mostrar 📃 \n 3️⃣.- Calcular Promedio 🧮 \n 4️⃣.- SALIR ❌ ")
    opcion=input("\t ✨ Elige una opción (1-4):  ").upper()
    return opcion

def agregar_calificaciones(lista):
   borrar_pantalla()
   print("📝 Agregar Calificaciones 📥")
   nombre = input("👩‍🎓 Nombre del Alumno: ").upper().strip()
   calificaciones=[]
   for i in range(1,4):
      continua=True
      while continua:
         try:
            cal = float(input(f"📌 Calificación {i}: "))
            if cal>=0 and cal>=10:
               calificaciones.append(cal)
               continua=False
            else:
               print("⚠️ Ingresa un número válido (0-10)") 
         except ValueError:
            print("⚠️ Ingresa un valor numérico")
   lista.append([nombre]+calificaciones)
   print("✅ Acción realizada con éxito")

def mostrar_calificaciones(lista):
   borrar_pantalla()
   print("📊 Mostrar Calificaciones 📊") 
   if len(lista) > 0:
      print(f"{'👩‍🎓 Nombre':<15}{'📘 Calf. 1':<10}{'📗 Calf. 2':<10}{'📙 Calf. 3':<10}")
      print(f"{'-'*40}")
      for fila in lista:
         print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
      print(f"{'-'*40}")  
      cuantos = len(lista)
      print(f"👨‍🏫 Son {cuantos} alumnos registrados")
   else:
      print("📭 No hay calificaciones registradas en el sistema")    

def calcular_promedios2(lista):
    borrar_pantalla()
    print("📐 .:: PROMEDIOS ::. 📐")
    if len(lista) > 0:
      print(f"{'👩‍🏫 Alumno':<15}{'📈 Promedio':<10}")
      print(f"{'-'*30}")
      promedio_grupal=0
      for fila in lista:
         nombre=fila[0]
         i=1
         suma=0
         promedio=0
         while i<=3:
            suma+=fila[i]
            i+=1
         promedio=suma/3
         print(f"{nombre:<15}{promedio:<15}")  
         promedio_grupal+=promedio 
      print(f"{'-'*30}")
      promedio_grupal=promedio_grupal/len(lista)
      print(f"🧠 El promedio grupal es: {promedio_grupal:} ")
    else:
      print("📭 No hay calificaciones registradas en el sistema")     

def calcular_promedios(lista):
    borrar_pantalla()
    print(".:: PROMEDIOS ::. ")
    if len(lista)>0:
      print(f"{'Alumno':<15}{'Promedio':<10}")
      print(f"{'-'*30}")
      promedio_grupal=0
      for fila in lista:
         nombre=fila[0]
         promedio=sum(fila[1:])/3
         print(f"{nombre:<15}{promedio:.2f}")  
         promedio_grupal+=promedio 
      print(f"{'-'*30}")
      promedio_grupal=promedio_grupal/len(lista)
      print(f"El promedio grupal es: {promedio_grupal} ")
    else:
      print("No hay calificaciones registradas en el sistema")       

def buscar_calificaciones(lista):
    borrar_pantalla()
    print("🔍 Buscar Calificaciones 🔍")
    nombre = input("👩‍🎓 Nombre del Alumno a buscar: ").upper().strip()
    encontrado = False
    for fila in lista:
        if fila[0] == nombre:
            print(f"\n📘 Calificaciones de {nombre}:")
            print(f"📌 Calf. 1: {fila[1]}")
            print(f"📌 Calf. 2: {fila[2]}")
            print(f"📌 Calf. 3: {fila[3]}")
            encontrado = True
            break
    if not encontrado:
        print(f"❌ No se encontró al alumno '{nombre}' en el sistema.")
    esperarTecla()