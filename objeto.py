from Conexion import *
class Objeto():
    conexion = Conexion()
    tabla = ''
    id = 0
    #name = ''
    #atribute = ''
    atributos = ''
    query_insert = ''
    query_insert_end = ''
    query_update = ''
    query_update_end = ''
    query_delete = ''
    query_select_all = ''
    query_select_me = ''
    query_search = ''
    query_delete_all= ''
    query_search_date = ''
    query_search_date_end = ''
    es_nuevo = True 

    def inicializar(self):
        tabla = self.tabla
        atributos = self.atributos
        self.query_insert = 'INSERT INTO '+tabla.title()+' ('+atributos+') VALUES ('
        self.query_insert_end = ');'
        self.query_update = 'UPDATE '+tabla.title()+' SET '
        self.query_update_end = ' WHERE '+tabla+'_id= %s ;'
        self.query_delete = 'DELETE FROM '+tabla.title()+ ' WHERE '+tabla+'_id = %s ;'
        self.query_delete_all = 'DELETE FROM ' + tabla.title() + ' ;' 
        self.query_select_all = 'SELECT * FROM '+ tabla.title() +' ;'
        self.query_select_me  = 'SELECT * FROM '+ tabla.title() +' WHERE '+tabla+'_id =%s ;'
        self.query_search = 'SELECT * FROM '+ tabla.title() + ' WHERE '+ tabla + '_' 
        self.query_search_end = ' =%s ;'
        self.query_search_date = 'SELECT * FROM ' + tabla.title() + ' WHERE ' + tabla + '_'
        self.query_search_date_end = ' BETWEEN %s and %s ;'

    def contar(self):
        print (self.tabla.title())
        query = ('SELECT '+self.tabla+'_id from '+self.tabla.title()+' ORDER BY '+self.tabla+'_id DESC LIMIT 1;')
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(query)
        result=cursor.fetchone()
        cursor.close()
        if result is None:
              return 1
        return (result[0]+1)
 
      def __init__(self):
          pass
     
      def modificar(self):
          pass

    def consultar_todos(self):
        lista=[]
        query = self.query_select_all
        print query
        conexion = self.conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print result
        lista = self.enlistar(result)
        print len(lista)
        cursor.close()
        print lista
        return lista

    def consultar_By_Atribute(self,atribute,name):
        lista=[]
        query = self.query_search + name + self.query_search_end
        print query
        conexion = self.conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute(query,(atribute,))
        result = cursor.fetchall()
        print result
        lista = self.enlistar(result)
        print len(lista)
        cursor.close()
        print lista
        return lista

    def consultar_By_Date(self,desde,hasta,name):
        lista=[]
        query = self.query_search_date + name + self.query_search_date_end
        print query
        conexion = self.conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute(query,(desde,hasta))
        #cursor.execute(query,('2005-01-01','2009-01-01'))
        result = cursor.fetchall()
        print result
        lista = self.enlistar(result)
        print len(lista)
        cursor.close()
        print lista
        return lista

    def mapeardatos(self, datarow):
        pass

    def consultar(self):
        query = self.query_select_me
        print query
        conexion = self.conexion.getConnection()
        cursor = conexion.cursor()
        print self.id 
        cursor.execute(query,(self.id,))
        result = cursor.fetchall()
        self.mapeardatos(result[0])
        cursor.close()

    def eliminar(self):
        pk = self.id
        query = self.query_delete 
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(query,(pk,))
        conexion.commit()
        cursor.close()

    def eliminar_todo(self):
        query = self.query_delete_all
        conexion = self.conexion.getConnection()
        cursor = conexion.cursor()
        cursor.execute(query)
        conexion.commit()
        cursor.close()

