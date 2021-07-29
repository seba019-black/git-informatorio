

class Contacto():
	def __init__(self,nombre,telefono,email):
		self.__nombre = nombre
		self.__telefono = telefono
		self.__email = email

	def getNombre(self):
		return f'Mi nombre es:{self.__nombre}'

	def setNombre(self,nuevoNombre):
		self.__nombre = nuevoNombre

	def getTelefono(self):
		return f'Mi telefono es:{self.__telefono}'

	def setTelefono(self,nuevoTelefono):
		self.__telefono = nuevoTelefono

	def getEmail(self):
		return f'Mi Email es:{self.__email}'

	def setEmail(self,nuevoEmail):
		self.__email = nuevoEmail

	def soyYO(self,nombre):
		if self.__nombre == nombre:
			return True
		else:
			return False


class Agenda():
	def __init__(self,nombre):
		self.__nombre = nombre
		self.__contactos = list()

	def agregarContacto(self, c):
		self.__contactos.append(c)

	def mostrarContactos(self):
		print('----------INICIO------------')
		for c in self.__contactos:
			print(f'Contaco: \n {c.getNombre()} \n {c.getTelefono()} \n {c.getEmail()}')
		print('----------FIN------------')

	def buscarContacto(self,nombre):
		for c in self.__contactos:
			if c.soyYO(nombre):
				return c