class Animal():
    #Propiedaes
    especie = ""
    peso = 0
    altura = 0

    #Constructor
    def __init__(self, especie, peso, altura):
        self.especie = especie
        self.peso = peso
        self.altura = altura

    #Metodos
    def cazar(self):
        print("Soy un", self.especie, "y estoy cazando")
    def comer(self):
        print("Soy un", self.especie, "y estoy comiendo")
    def dormir(self):
        print("Soy un", self.especie, "y estoy durmiendo")

class Mascota():
    #Propiedaes
    nombre = ""
    amo = ""

    #Constructor
    def __init__(self, nombre, amo):
        self.nombre = nombre
        self.amo = amo

    #Metodos
    def sentarse(self):
        print("Soy", self.nombre, "y estoy sentado")
    def tumbarse(self):
        print("Soy", self.nombre, "y estoy tumbado")

class Perro(Animal, Mascota):
    #Constructor
    def __init__(self, nombre, amo, peso, altura):
        Animal.__init__(self, "Perro", peso, altura)
        Mascota.__init__(self, nombre, amo)

class Leon(Animal):
    #Constructor
    def __init__(self, peso, altura):
        super().__init__("Leon", peso, altura)

flami = Perro("Flami", "David", 7, 0.5)
flami.comer()
flami.dormir()
flami.sentarse()

simba = Leon(100, 1.2)
simba.cazar()
simba.comer()