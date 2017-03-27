class Hijo:
	"""Recipiente que recoge un fichero y su directorio padre"""
	def __init__(self):
		"""Constructor"""
		self.__nombre=''
		self.__padre=''
	def setPadre(self,dir):
		"""Cambiar valor de la variable padre.

		Función que modifica el valor de la variable padre

		Parámetros:
		padre -- nueva dirección
		
		"""
		self.__padre=dir

	def setNombre(self,dir):
		"""Cambiar valor de la variable nombre.

		Función que modifica el valor de la variable nombre, la cual es el hijo

		Parámetros:
		padre -- nueva dirección
		
		"""
		self.__nombre=dir

	def getPadre(self):
		"""Devuelve el  valor de la variable padre.

		Función que modifica el valor de la variable padre

		Devuelve:
		padre 
		
		"""
		return self.__padre

	def getNombre(self):
		"""Devuelve el  valor de la variable nombre.

		Función que modifica el valor de la variable padre

		Devuelve:
		nombre 
		
		"""
		return self.__nombre

