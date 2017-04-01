######################################################################## 
class Hijo:
	"""Recipiente que recoge un fichero y su directorio padre"""
	def __init__(self):
		"""Constructor"""
		self.__nombre=''
		self.__padre=''
		self.__etiqueta=[]
	def setPadre(self,dir):
		"""
		Función que modifica el valor de la variable padre

		Parámetros:
		padre -- nueva dirección
		
		"""
		self.__padre=dir
	#----------------------------------------------------------------------
	def setNombre(self,dir):
		"""
		Función que modifica el valor de la variable nombre, la cual es el hijo

		Parámetros:
		padre -- nueva dirección
		
		"""
		self.__nombre=dir
	#----------------------------------------------------------------------
	def getPadre(self):
		"""
		Función que modifica el valor de la variable padre

		Devuelve:
		padre 
		
		"""
		return self.__padre
	#----------------------------------------------------------------------
	def getNombre(self):
		"""
		Función que modifica el valor de la variable padre

		Devuelve:
		nombre 
		
		"""
		return self.__nombre
	#----------------------------------------------------------------------
	def convertir(self,cad):
		"""
		Función que actualiza las etiquetas
		
		"""
		lista=cad.split(",")
		for x in lista:
			if not x in self.__etiqueta:
				self.setEtiqueta(x)
	#----------------------------------------------------------------------
	def setEtiqueta(self,x):
		"""
		Función que añade etiquetas al final
		
		"""
		self.__etiqueta.append(x)		
	#----------------------------------------------------------------------		__
	def getEtiqueta(self):
		"""
		Función que devuelve las etiquetas
		
		"""
		return self.__etiqueta		
	#----------------------------------------------------------------------		
