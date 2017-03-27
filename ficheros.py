import hijo
########################################################################
class ficheros:
	"""Clase para recoger los directorios y ficheros de la carpeta de dropbox"""
	def __init__(self):
		"""Constructor"""
		self.__directorios=[]   
		self.__secundarios=[]
	#----------------------------------------------------------------------
	def setNDir(self,dir):
		"""Añade la nueva dirección a la lista"""
		self.__directorios.append(dir)
	#----------------------------------------------------------------------
	def setNSecundario(self,dir):
		"""Organización de ficheros y directorios.

		Función que recorre los distintos directorios separando y relacionando los padres con los hijos.

			Parámetros:
		dir -- dirección a analizar
	
		"""
		d=hijo.Hijo()
		x=dir.split('/')
		d.setPadre(x[1])
		d.setNombre(x[2])
		self.__secundarios.append(d)
	#----------------------------------------------------------------------
	def getDirectorios(self):
		"""Devuelve la lista de directorios padres"""
		return self.__directorios
	#----------------------------------------------------------------------
	def getHijos(self):
		"""Devuelve la lista de ficheros"""
		return self.__secundarios
	#----------------------------------------------------------------------
