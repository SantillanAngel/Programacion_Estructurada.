agenda={}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar... 💫 ")

def menu_principal():
    print("\n\t 🧸📒 ..::: Sistema de Gestión de Agenda de Contactos :::... 🧸📒 \n 1️⃣ Agregar contacto \n 2️⃣ Mostrar todos los contactos \n 3️⃣ Buscar contacto por nombre \n 4️⃣ Modificar Contacto \n 5️⃣ Eliminar Contacto \n 6️⃣ SALIR ❌ ")
    opcion=input("\t ✨ Elige una opción (1-4):  ").upper()
    return opcion

def agregar_contacto(agenda):
   borrarPantalla()
   print("🎀 .:: Agregar Contactos a Agenda ::. 🎀 ") 
   nombre=input(" 💁 Nombre del contacto:").upper().strip()
   if nombre in agenda:
       print("Contacto existente ⚠️")
   else:
       tel=input("📞 Ingrese el numero de telefono:").strip()
       email=input("📧 Ingrese el email:").upper().strip()
       agenda[nombre]=[tel,email]
       print("\n✅ ¡Acción realizada con éxito!\n")

def mostrar_contacto(agenda):
   borrarPantalla()
   print("\n📖 .:: Mostrar Contactos de la Agenda ::. 📖\n")
   if not agenda:
       print("📭 No hay contactos en la agenda.")
   else:
       print(f"{'👤 Nombre':<15}{'📱 Teléfono':<15}{'📧 Email':<15}")
       print(f"-"*60)
       for nombre,datos in agenda.items():
           print(f"{nombre:<15}{datos[0]:<15}{datos[1]:<15}")
       print(f"-"*60)
   
def buscar_contacto(agenda):
    borrarPantalla()
    print("\n🔍 .:: Buscar Contacto en Agenda ::. 🔍\n")
    if not agenda:
       print("📭 No hay contactos en la agenda.")
    else:
        nombre = input("🔎 Nombre del contacto: ").upper().strip()
        if nombre in agenda:
           print(f"{'👤 Nombre':<15}{'📱 Teléfono':<15}{'📧 Email':<15}")
           print(f"-"*60)
           print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
           print(f"-"*60)
        else:
            print("❌ El contacto no existe en la agenda.")

def modificar_contacto(agenda):
    borrarPantalla()
    print("\n🛠️ .:: Modificar Contacto de la Agenda ::. 🛠️\n")
    if not agenda:
        print("📭 No hay contactos en la agenda.")
    else:
        nombre = input("👤 Nombre del contacto: ").upper().strip()
        if nombre in agenda:
           print(f"{'👤 Nombre':<15}{'📱 Teléfono':<15}{'📧 Email':<15}")
           print(f"-"*60)
           print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
           print(f"-"*60)
           resp=input("📝 ¿Deseas modificar el contacto? (Si/No) ").lower().strip()
           if resp=="si":
               tel = input("📱 Nuevo numero de teléfono: ").strip()
               email = input("📧 Nuevo email: ").upper().strip()
               agenda[nombre]=[tel,email]
               print("\n🧹 ¡Contacto modificado exitosamente!\n")
        else:
            print("❌ El contacto no existe.")
               
def eliminar_contacto(agenda):
    borrarPantalla()
    print("\n🗑️ .:: Eliminar Contacto ::. 🗑️\n")
    if not agenda:
        print("📭 No hay contactos en la agenda.")
    else:
        nombre = input("👤 Nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
           print(f"{'👤 Nombre':<15}{'📱 Teléfono':<15}{'📧 Email':<15}")
           print(f"-"*60)
           print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
           print(f"-"*60)
           resp = input("❓ ¿Deseas eliminar este contacto? (si/no): ").lower().strip()
           if resp == "si":
               agenda.pop(nombre)
               print("\n🧹 ¡Contacto eliminado exitosamente!\n")
        else:
            print("❌ El contacto no existe.")