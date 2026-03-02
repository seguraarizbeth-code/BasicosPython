from Enemigo import *
import random
class Zombie(Enemigo):
    def _init_(self,puntos_energia=10, ataque=1):
        super()._init_(tipo_enemigo='ZOMBIE',puntos_energia=puntos_energia,ataque=ataque)

    def habla (self):
        print("Hummm...*")

    def propagar_enfermedad(self):
        print("El zombie esta tratando de propagar la enfermedad!")


    def ataque_especial(self):
        print("zombie ataqueb especial")
        funciona_ataque_especial = random.random () < 0.50
        if funciona_ataque_especial:
            self. puntos_energia += 2
            print("zombie ha regenarado su energia con 2HP!!")
