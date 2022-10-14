class Jugador():
    #Propiedades
    nombre = ""
    posicion = ""
    numero = ""
    #Constructor
    def __init__(self, Nombre, Posicion, Numero):
        self.nombre = Nombre
        self.numero = Numero
        self.posicion = Posicion

class Equipo():
    #Propiedades
    nombre = ""
    jugadores = []
    #Constructor
    def __init__(self, Nombre):
        self.nombre = Nombre
    #Metodos
    def mostrarEquipo(self):
        for jugador in self.jugadores:
            print("Nombre:", jugador.nombre, "-- Posicion:", jugador.posicion, "-- Numero:", jugador.numero)
    def añadirJugadores(self, jugador):
        self.jugadores.append(jugador)

j1 = Jugador("Vinicius Jr", "EI", "20")
j2 = Jugador("Benzema", "DC", "9")
j3 = Jugador("Casemiro", "MCD", "14")

eq1 = Equipo("Real Madrid")
eq1.añadirJugadores(j1)
eq1.añadirJugadores(j2)
eq1.añadirJugadores(j3)

eq1.mostrarEquipo()