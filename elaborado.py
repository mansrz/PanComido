from Conexion import *
from objeto import *

#Table Element
class Elaborado(Objeto):

    nombre = ''
    precio = 0 
    #TODO enum or class 
    tipo = 1
    expiracion = 0 
    headernames = ['Nombre','Precio','Expiracion']
    atributos = 'Elaborado_id, Elaborado_nombre, Elaborado_precio,\
             , Elaborado_expiracion'
    tabla = ' elaborado'

    def __init__(self):
        self.inicializar()

    def guardar(self):
        id = str(self.contar())
        query = self.query_insert + ' %s,%s,%s '+self.query_insert_end
        conexion = self.conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute(query,(self.nombre,self.precio, self.expiracion,id))
        conexion.commit()
        cursor.close()

