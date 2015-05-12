import sys
from conexion import *
from PyQt4 import QtGui,QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Usuario import *
import re

ui = uic.loadUiType('mainwindow.ui')[0]
login = uic.loadUiType('login.ui')[0]
ingresar = uic.loadUiType('ingresar.ui')[0]
estilo = open('st.stylesheet','r').read()

class VentanaPrincipal(QtGui.QMainWindow, principal_ui):
  def __init__(self,parent=None):
    QtGui.QMainWindow.__init__(self,parent)
    self.setupUi(self)
    screen = QtGui.QDesktopWidget().screenGeometry()
    self.frame.move((screen.width()-self.frame.geometry().width())/2, (screen.height()-self.frame.geometry().height())/2)
    self.setStyleSheet(estilo )
    self.inicializar()

  def inicializar(self):
    self.action_cliente.triggered.connect(self.Abrir_cliente)
    self.action_producto.triggered.connect(self.Abrir_producto)
    self.action_factura.triggered.connect(self.Abrir_factura)
    self.action_reporte.triggered.connect(self.Abrir_reporte)
  
  def Abrir_reporte(self):
    reporte = VentanaReporte()
    reporte.exec_()
  
  def Abrir_factura(self):
    factura = VentanaFactura()
    factura.exec_()

  def Abrir_producto(self):
    producto = VentanaProducto()
    producto.exec_()

  def Abrir_cliente(self):
    cliente = VentanaCliente()
    cliente.exec_()


class Login(QtGui.QDialog, login):
    conexion = Conexion()
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.setStyleSheet(estilo)
        self.boton_iniciarsesion.clicked.connect(self.login_act)

    def login_act(self):
        name = str(self.input_usuario.text())
        pwd = str(self.input_pwd.text())
        query = ('SELECT COUNT(*) FROM Usuario WHERE usuario_nick= %s AND usuario_pwd = %s')
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(query,(name,pwd))
        result=cursor.fetchone()
        print result
        if result[0]>0:
            self.accept()
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Usuario o contrasena equivocadas', QtGui.QMessageBox.Ok)
        cursor.close()
        

if __name__ == '__main__':
  app = QtGui.QApplication(sys.argv)
  if Login().exec_() == QtGui.QDialog.Accepted:
    print 'holiwis'
    principal = VentanaPrincipal()
    principal.showMaximized()
    sys.exit(app.exec_())
   
