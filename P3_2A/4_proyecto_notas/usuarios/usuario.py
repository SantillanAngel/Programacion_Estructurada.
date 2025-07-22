from conexionBD import * 
import datetime

def registrar(nombre,apellidos,email,password):
    try:
        fecha=datetime.datetime.now()
        sql="insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s)"
        val=(nombre,apellidos,email,password,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False
    
def inicio_sesion(email,contrasena):
    try:
        sql="select * from usuarios where email=%s and passwor=%s"
        val=(email,contrasena)
        cursor.execute(sql,val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return False
    
