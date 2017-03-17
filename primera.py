import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import ctypes #GetSystemMetrics
import completo
import pruebas
import os.path
#Clase heredada de QMainWindow (Constructor de ventanas)


  #Asignar estilos CSS
  #self.setStyleSheet("background-color: #000; color: #fff;")


class Ventana(QMainWindow):
 #Método constructor de la clase
	def __init__(self):
  #Iniciar el objeto QMainWindow
		QMainWindow.__init__(self)
  #Cargar la configuración del archivo .ui en el objeto
		uic.loadUi("mainwindow.ui", self)
		#self.setStyleSheet("background-color:#0099FF; color: #fff;font-size:Bold")
		#self.dir.setStyleSheet("background-color:#1aa3ff;font-size: bold")
		#self.recipiente.setStyleSheet("background-color:#1aa3ff;font-size: Bold")
		self.setWindowTitle("Cambiando el título de la ventana")
		self.drop = completo.DropObj("colores.py")
		qfont = QFont("Arial", 12, QFont.Bold)
		self.setFont(qfont)
  #Asignar un tipo de cursor
		self.setCursor(Qt.SizeAllCursor)
		#self.ventana2=Ventana2()
  #Asignar estilos CSS
  #self.setStyleSheet("background-color: #000; color: #fff;")
		self.boton.setStyleSheet("background-color: #0000e6; color: #fff; font-size: Bold")
		self.boton.clicked.connect(self.cambio)
		self.dir.setText(self.drop.getAutorize())

	def cambio(self):
		print(type(self.recipiente.text()))
		self.drop.nuevoToken(str(self.recipiente.text()))
		self.ventana2=pruebas.MainWindow(self.drop)
		self.ventana2.show()
		self.close()




#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
if os.path.exists(".token.txt"):
	drop = completo.DropObj("colores.py")
	drop.autoiden()
	ventana2=pruebas.MainWindow(drop)
	ventana2.show()
	ventana2.activateWindow()
else:
	_ventana = Ventana()
#Mostra la ventana
	_ventana.show()

#Ejecutar la aplicación
app.exec_()
