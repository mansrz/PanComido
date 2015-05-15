import sys
from conexion import *
from PyQt4 import QtGui,QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Usuario import *
import re

try:
    ui = uic.loadUiType('principal.ui')[0]
    login = uic.loadUiType('login.ui')[0]
    estilo = open('st.stylesheet','r').read()
except:
    print 'Error con los archivos de interfaz'

class VentanaPrincipal(QtGui.QMainWindow, ui):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        screen = QtGui.QDesktopWidget().screenGeometry()
        self.frame.move((screen.width()-self.frame.geometry().width())/2, (screen.height()-self.frame.geometry().height())/2)
        self.setStyleSheet(estilo )
        self.inicializar()

    def inicializar(self):
        self.actionPropio.triggered.connect(self.MantenimientoPropios)
        self.actionTerceros.triggered.connect(self.MantenimientoTerceros)
        self.actionDiario.triggered.connect(self.MantenimientoDiario)
        self.actionEntradas.triggered.connect(self.MantenimientoEntradas)
        self.actionGastos.triggered.connect(self.MantenimientoGastos)
        self.actionEstadsticas.triggered.connect(self.MantenimientoEstadisticas)

    def MantenimientoPropios(self):
        pass 

    def MantenimientoTerceros(self):
        pass 
    def MantenimientoDiario(self):
        pass

    def MantenimientoEntradas(self):
        pass

    def MantenimientoGastos(self):
        pass

    def MantenimientoEstadisticas(self):
        pass

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
        principal = VentanaPrincipal()
        principal.showMaximized()
        sys.exit(app.exec_())
           
