class Coche():
    #Propiedades
    marca = ""
    vel = 0
    vel_max = 0
    matricula = ""
    #Constructor
    def __init__(self, Marca, Vel, Vel_max, Matricula):
        self.marca = Marca
        self.vel = Vel
        self.vel_max = Vel_max
        self.matricula = Matricula
    #Metodos
    def darCaracteristicas(self, nombre):
        print("Nombre:", nombre)
        print("Marca:", self.marca)
        print("Velocidad:", self.vel)
        print("Velocidad Maxima:", self.vel_max)
        print("Matricula:", self.matricula, "\n")
    def arrancar(self):
        print("El coche", self.marca, "está arrancado")
    def frenar(self):
        print("El coche", self.marca, "está frenando")
        self.vel = 0
    def acelerar(self, velocidad):
        max = self.vel + velocidad
        if(max < self.vel_max): self.vel = max
        else: self.vel = self.vel_max

coche = Coche("BMW", 64, 260, "4989KKT")
coche.darCaracteristicas("Coche 1")
coche = Coche("Ferrari", 120, 300, "5298DXV")
coche.darCaracteristicas("Coche 2")
coche = Coche("Ford", 30, 200, "5728FNK")
coche.darCaracteristicas("Coche 3")
