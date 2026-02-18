# Investigación 1 - Programación Orientada a Objetos (POO) en Python
class Celular:
    marca = ""
    bateria = 0

    def llamar(self):
        print("Llamando...")

mi_celular = Celular()
mi_celular.marca = "Samsung"
mi_celular.bateria = 80

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

persona1 = Persona("Ana")


class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Hola, soy", self.nombre)


class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo



class Animal:
    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    pass

class Gato(Animal):
    pass

    
    
class Perro:
    def sonido(self):
        print("Guau")

class Gato:
    def sonido(self):
        print("Miau")



class Motor:
    def encender(self):
        print("Motor encendido")

class Auto:
    def __init__(self):
        self.motor = Motor()



class Foco:
    def __init__(self):
        self.encendido = False

    def prender(self):
        self.encendido = True

# Codigos de la Investigacion.