import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import ctypes 
import completo
import os.path
import AESCipher
######################################################################## 
class MainWindow(QMainWindow):
	"""Constructor"""
	def __init__(self,dr):
  		#Iniciar el objeto QMainWindow
		QMainWindow.__init__(self)
		#Cargar la configuración del archivo .ui en el objeto
		uic.loadUi("mainwindow2.ui", self)
		iconCar=QIcon('New-Folder-icon.png')
		iconFil=QIcon('nfile.png')
		iconSa=QIcon('save-icon.png')
		iconL=QIcon('lista-icon.png')
		iconN=QIcon('bold.png')
		iconApp=QIcon('app.png')
		iconSub=QIcon('underline.png')
		self.hijos=""
		self.drop = dr
		self.clave=AESCipher.AESCipher()
		self.systray = QSystemTrayIcon(iconApp, self)
		show_action = QAction("Show", self)
		quit_action = QAction("Exit", self)
		hide_action = QAction("Hide", self)
		show_action.triggered.connect(self.show)
		hide_action.triggered.connect(self.hide)
		quit_action.triggered.connect(qApp.quit)
		tray_menu = QMenu()
		tray_menu.addAction(show_action)
		tray_menu.addAction(hide_action)
		tray_menu.addAction(quit_action)
		self.systray.setContextMenu(tray_menu)
		self.systray.show()
		self.setWindowIcon(iconApp) 
		self.nCarpeta.clicked.connect(self.crearFolder)
		self.saves.clicked.connect(self.save)
		self.negrita.clicked.connect(self.bold)
		self.listaB.clicked.connect(self.lista)
		self.subButton.clicked.connect(self.subra)
		self.treeWidget.itemDoubleClicked.connect(self.openElement)
		self.formar()
		self.treeWidget.expandToDepth(0)
		self.dirCrear=""
		self.nCarpeta.setText("")
		self.nCarpeta.setIcon(iconCar)
		self.nFile.setIcon(iconFil)
		self.saves.setIcon(iconSa)
		self.abierto=""
		self.negrita.setIcon(iconN)
		self.listaB.setIcon(iconL)
		self.subButton.setIcon(iconSub)
		self.negrita.setToolTip('This is an example button')
		self.nFile.clicked.connect(self.crearFich)
		QShortcut(QtGui.QKeySequence("Ctrl+B"), self, self.bold)
		QShortcut(QtGui.QKeySequence("Ctrl+L"), self, self.lista)
		QShortcut(QtGui.QKeySequence("Ctrl+U"), self, self.subra)
		QShortcut(QtGui.QKeySequence("Ctrl+S"), self, self.save)
		QShortcut(QtGui.QKeySequence("Ctrl+T"), self, self.titulo)
		
	#----------------------------------------------------------------------
	def formar(self):
		"""
		Rellenar el arbol de directorios para trabajar con los archivos/ficheros de Dropbox.
		"""
		t=self.drop.listarCarpetas()
		t2=t.getDirectorios()
		self.hijos=t.getHijos()
		header=QTreeWidgetItem(["Droppy"])
		icon=QIcon('home-icon.png')
		icon2=QIcon('text-plain-icon.png')

		self.treeWidget.setHeaderItem(header) 
		root = QTreeWidgetItem(self.treeWidget, ["dropbox"])
		for i in range(len(t2)):
			q=[]
			q.append(t2[i])
			A = QTreeWidgetItem(root,q)
			A.setIcon(0,icon)
			for j in range(len(self.hijos)):
				if ("/"+self.hijos[j].getPadre())==t2[i]:
					q=[]
					q.append(self.hijos[j].getNombre())
					barA = QTreeWidgetItem(A,q)
					barA.setIcon(0,icon2)
	#----------------------------------------------------------------------
	"""###########################################################

				TRABAJO CON DROPBOX

	###########################################################"""
	def crearFolder(self):
		"""
		Función para crear carpetas en Dropbox.
		"""
		value,crear= QInputDialog.getText(self, "crear archivo", "Nombre de la nueva carpeta:")
		if crear and value!='':
			print('Nombre:', value)
			self.drop.crearCarpeta(value)
			self.treeWidget.clear()
			self.formar()
			self.treeWidget.expandToDepth(0)
	#----------------------------------------------------------------------
	def crearFich(self):
		"""
		Función para crear ficheros en Dropbox, a partir de un padre.
		"""
		if(self.dirCrear!=""):
			value,crear= QInputDialog.getText(self, "crear archivo", "Nombre del nuevo fichero:")
			if crear and value!='':
				if not value.endswith(".writer"):
					value=value+".writer"
				self.drop.archivoMod(value,self.dirCrear)
				self.treeWidget.clear()
				self.formar()
				self.treeWidget.expandToDepth(0)
		else:
			print("debes establecer la ruta")
			QMessageBox.warning(self, "WARNING", "Debes establecer una ruta para poder crear un fichero")
		
	#----------------------------------------------------------------------
	def openElement(self):
		"""
		Función para abrir ficheros de Dropbox y extraer el texto para ser editado.
		"""
		item = self.treeWidget.currentItem()
		y=item.parent()
		y=y.text(0)
		n=item.text(0)
		final=y+"/"+n
		if(y=="dropbox"):
			print("ruta establecida ",n)
			self.dirCrear=n
		else:
			self.abierto=final
			if  final.endswith(".enc"):
				value,crear= QInputDialog.getText(self, "CONTRASEÑA", "Dame la contraseña con la que cifrarás el fichero:",QLineEdit.Password)
				if crear and value!='':
					x=self.drop.abrirFichero(final)
					t=str(self.clave.decrypt(value,x),'cp1252')
					self.directorio.setText(t)
			else:
				x=str(self.drop.abrirFichero(final),'cp1252')
				print(type(x))
			#self.directorio.setText(self.drop.abrirFichero(final).decode('UTF-8'))
				self.directorio.setText(x)
	#----------------------------------------------------------------------
	def save(self):
		"""
		Función para salvar el texto editado y subirlo a Dropbox.
		"""
		if(self.abierto!=""):
			if self.encrip.isChecked():
				value,crear= QInputDialog.getText(self, "CONTRASEÑA", "Dame la contraseña con la que cifrarás el fichero:",QLineEdit.Password)
				if crear and value!='':
					if not self.abierto.endswith(".enc"):
						self.drop.saveF(self.clave.encrypt(value,self.directorio.toHtml()),self.abierto+".enc")
						self.drop.borrarF(self.abierto)
						self.treeWidget.clear()
						self.formar()
						self.treeWidget.expandToDepth(0)
					else:
						self.drop.saveF(self.clave.encrypt(value,self.directorio.toHtml()),self.abierto)
				
			else:
				self.drop.saveF(self.directorio.toHtml(),self.abierto)
		else:
			QMessageBox.warning(self, "WARNING", "Debes trabajar con un fichero antes de guardarlo")
		print("se guarda")
	#----------------------------------------------------------------------
	"""###########################################################

			FUNCIONES DE EDICIÖN DE TEXTO

	###########################################################"""
	def bold(self):
		"""
		Función para poner letras en negrita.
		"""
		if self.directorio.fontWeight() == QtGui.QFont.Bold:
			self.directorio.setFontWeight(QtGui.QFont.Normal)
		else:
			self.directorio.setFontWeight(QtGui.QFont.Bold)
	#----------------------------------------------------------------------
	def lista(self):
		"""
		Función para añadir listas.
		"""
		cursor = self.directorio.textCursor()
		cursor.insertList(QtGui.QTextListFormat.ListDisc)
	#----------------------------------------------------------------------
	def subra(self):
		"""
		Función para subrayar texto.
		"""
		state = self.directorio.fontUnderline()

		self.directorio.setFontUnderline(not state)
	#----------------------------------------------------------------------

	def titulo(self):
		"""
		Prueba para añadir h1
		"""
		cursor=self.directorio.textCursor()
		textSelected = cursor.selectedText()
		self.directorio.insertHtml("<h1>"+textSelected+"</h1>")
		self.directorio.insertHtml("<h2>"+textSelected+"</h2>")
		self.directorio.insertHtml("<h3>"+textSelected+"</h3>")
	#----------------------------------------------------------------------
"""

barA = QTreeWidgetItem(A, ["bar", "i"])
bazA = QTreeWidgetItem(A, ["baz", "a"])

self.treeWidget.setEditTriggers(self.treeWidget.NoEditTriggers)

self.treeWidget.itemDoubleClicked.connect(self.checkEdit)
"""
