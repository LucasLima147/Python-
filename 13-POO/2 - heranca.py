#super classe ou classe mãe
class Animal:

    def __init__(self):
        print("Animal criado")

    def identif(self):
        print("Classe Animal")

    def comer(self):
        print("Comendo")

#sub-classe ou classe filha
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado")

    def identif(self):
        print("Classe Cachorro")

    def latir(self):
        print("latindo")


dog = Cachorro()
dog.identif()
dog.comer()
dog.latir()