from conexionBD import *

def crear(usuario_id,titulo,descripcion):
    try:
        cursor.execute("insert into notas (usuario_id,titulo,descripcion,fecha) values (%s,%s,%s,NOW())",(usuario_id,titulo,descripcion))
        conexion.commit()
        return True
    except:
        return False
    
def mostrar(usuario_id):
    try:
        cursor.execute("select * from notas where usuario_id=%s",(usuario_id,))
        return cursor.fetchall()
    except:
        return []
    