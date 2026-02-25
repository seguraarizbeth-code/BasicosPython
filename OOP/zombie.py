from Enemigo import *

class Zombie(Enemigo):
    def _init_(self,puntos_energia=10, ataque=1):
        super()._init_(tipo_enemigo='ZOMBIE',puntos_energia=puntos_energia,ataque=ataque)

    def habla (sel):
        print("Hummm...*")

    def propagar_enfermedad(self):
        print("El zombie esta tratando de propagar la enfermedad!")


