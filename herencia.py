class Persona:
    _siguiente = 0

    def __init__(self, nombre='Invitado', activo=True):
        self._codigo = self.siguiente()
        self.__nombre = self.__nombre_mayuscula(nombre)
        self.activo = activo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nomb):
        self.__nombre = nomb

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codi):
        self._codigo = codi

    def siguiente(self):
        Persona._siguiente = Persona._siguiente+1
        return Persona._siguiente

    def __nombre_mayuscula(self, nombre):
        return nombre.upper()
    
    def mostrar(self):
        return 'Código: {} - Nombre: {} - Activo: {}'.format(self.codigo, self.nombre, self.activo)


class Empleado(Persona):
    def __init__(self, nomb='Invitado', activo=True, sala=400):
        Persona.__init__(self, nomb, activo)
        self.salario = sala
    
    def mostrar(self):
        return Persona.mostrar_datos(self) + ' - Sueldo: ' + str(self.salario)


obj_person1 = Persona()
print(obj_person1.mostrar())
obj_person2 = Persona('Daniel', False)
print(obj_person2.mostrar_datos())
print(Empleado().mostrar())