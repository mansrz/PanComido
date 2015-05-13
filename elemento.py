from Conexion import *
from objeto import *

#Table Element
class Elemento(Objeto):

    nombre = ''
    precio = 0 
    #TODO enum or class 
    tipo = 1
    expiracion = 0 
    headernames = ['Nombre','Precio','Tipo','Expiracion']
    atributos = 'Elemento_id, Elemento_nombre, Elemento_precio,\
             ,Elemento_tipo, Elemento_expiracion'
    tabla = ' elemento'

    def __init__(self):
        self.inicializar()

    def guardar(self):
        id = str(self.contar())
        query = self.query_insert + ' %s,%s,%s,%s '+self.query_insert_end
        conexion = self.conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute(query,(self.nombre,self.precio,self.tipo, self.expiracion,id))
        conexion.commit()
        cursor.close()
        print query

