import hijo
class ficheros:
	def __init__(self):
		self.directorios=[]   
		self.secundarios=[]

	def setNDir(self,dir):
		self.directorios.append(dir)

	def setNSecundario(self,dir):
		d=hijo.Hijo()
		x=dir.split('/')
		d.setPadre(x[1])
		d.setNombre(x[2])
		self.secundarios.append(d)
	def getDirectorios(self):
		return self.directorios

	def getHijos(self):
		return self.secundarios

