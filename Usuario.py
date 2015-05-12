from conection import *
class Cuenta():
  nick=''
  nombre=''
  conexion = Conexion()
  def crear(self):
    pass
  def eliminar(self):
    pass
  def modificar(self):
    pass

  def guardar(self):
    query = ('INSERT INTO `Cuenta`\
    (`usuario_id`,`usuario_nombre`,`usuario_nick`,\
    `usuario_pwd`) VALUES(%s,%s,%s,%s)')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(str(self.contar()),self.nombre,self.nick,self.pwd))
    conexion.commit()
    cursor.close()


  def contar(self):
    query = ('SELECT Usuario_id from pancomido.Usuario ORDER BY usuario_id DESC LIMIT 1;')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query)
    result=cursor.fetchone()
    cursor.close()
    print result[0]
    return (result[0]+1)
 
 
