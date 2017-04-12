import dropbox
import os
import sys
import webbrowser
from colores import bcolors
import ficheros
########################################################################
class DropObj(object):
	"""
	Dropbox object that can access your dropbox folder,
	as well as download and upload files to dropbox
	"""

	#----------------------------------------------------------------------
	def __init__(self, filename=None, path='/'):
		"""Constructor"""
		self.base_path = os.path.dirname(os.path.abspath(__file__))
		self.filename = filename
		self.path= path
		self.app_key= 'wemujp1ue1ljmui'
		self.app_secret= 'xny3h4yajvwkcb6'
		self.app_type = 'app_folder'
		self.flow = dropbox.client.DropboxOAuth2FlowNoRedirect(self.app_key, self.app_secret)
		self.authorize_url= self.flow.start()
		self.client = None


	#----------------------------------------------------------------------
	def nuevoToken(self,code):
		"""
		Connect and authenticate with dropbox
		"""
		self.access_token, user_id = self.flow.finish(code)
		self.client = dropbox.client.DropboxClient(self.access_token)
		outfile = open('.token.txt', 'w') # Indicamos el valor 'w'.
		outfile.write(self.access_token)
		outfile.close()

	#----------------------------------------------------------------------
	def autoiden(self):
		"""
		Connect and authenticate with dropbox
		"""
		infile = open('.token.txt', 'r')
		x=infile.read()
		infile.close()
		self.client = dropbox.client.DropboxClient(x)

		#----------------------------------------------------------------------
	def getAutorize(self):

		return self.authorize_url

		#----------------------------------------------------------------------
	def download_file(self, filename=None, outDir=None):
		"""
		Download either the file passed to the class or the file passed
		to the method
		"""

		if filename:
			fname = filename
			f, metadata = self.client.get_file_and_metadata("/" + fname)
		else:
			fname = self.filename
			f, metadata = self.client.get_file_and_metadata("/" + fname)

		if outDir:
			dst = os.path.join(outDir, fname)
		else:
			dst = fname

		with open(fname, "w") as fh:
			fh.write(f.read())

		return dst, metadata

	#----------------------------------------------------------------------
	def get_account_info(self):

		return self.client.account_info()

	#----------------------------------------------------------------------
	def crearCarpeta(self,carpeta):

		self.client.file_create_folder('/'+carpeta)

	#----------------------------------------------------------------------

	def upload_file(self,ruta="/"):
		"""
		Subida de fichero a dropbox con ruta opcional
		"""
		try:
			with open(self.filename) as fh:
				path = os.path.join(self.path, self.filename)
				res = self.client.put_file(ruta+self.filename, fh,True)
				print ("uploaded: ",self.filename)
		except Exception:
			print ("ERROR: ")

		return res

	#----------------------------------------------------------------------
	def listarCarpetas(self):
		a=ficheros.ficheros()
		metadata = self.client.metadata('/')
		for x in metadata["contents"]:
			print(bcolors.nuevo+x['path']+bcolors.ENDC)
			if x['is_dir']==True:
				a.setNDir(x['path'])
				metadata2 = self.client.metadata(x['path'])
				for x2 in metadata2["contents"]:
					a.setNSecundario(x2['path'])
					print("\t"+bcolors.morado+x2['path']+bcolors.ENDC)
		return a
	#----------------------------------------------------------------------
	def abrirFichero(self,fich):
		f = self.client.get_file(fich)#abrimos el fichero con el que vamos a trabajar
		x=f.read()
		
		f.close()
		return x
	#----------------------------------------------------------------------
	def archivoMod(self,nomb,dir):
		respuesta = self.client.put_file(dir+"/"+nomb, "",1)
	#----------------------------------------------------------------------
	def saveF(self,contenido,dir):
		respuesta = self.client.put_file(dir, contenido,1)
	#----------------------------------------------------------------------
	def borrarF(self,dir):
		respuesta = self.client.file_delete(dir)
		print(bcolors.WARNING+"se ha borrado:"+bcolors.ENDC+bcolors.nuevo+dir+bcolors.ENDC)
	#----------------------------------------------------------------------
	def buscar(self):
		respuesta = self.client.search("","etiquetas.txt")
		if(respuesta==[]):
		
			self.saveF("","etiquetas.txt")
			print(bcolors.WARNING+"El fichero de etiquetas ha sido creado"+bcolors.ENDC)
		else:
			print(bcolors.WARNING+"El fichero de etiquetas ya existe"+bcolors.ENDC)
	#----------------------------------------------------------------------
#if __name__ == "__main__":
#	drop = DropObj("config.ini")
#	drop.listarCarpetas()
#	drop.upload_file("prueba/")
