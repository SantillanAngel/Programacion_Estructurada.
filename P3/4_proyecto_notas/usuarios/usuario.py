from conexionBD import * 
import datetime
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def registrar(nombre,apellidos,email,password):
    try:
        fecha=datetime.datetime.now()
        password=hash_password(password)
        sql="insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s)"
        val=(nombre,apellidos,email,password,fecha)
        cursor.execute(sql,val)
        conexion.commit()
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return False
    return True
def inicio_sesion(email,contrasena):
    try:
        contrasena=hash_password(contrasena)
        sql="select * from usuarios where email=%s and password=%s"
        val=(email,contrasena)
        cursor.execute(sql,val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return False
    
