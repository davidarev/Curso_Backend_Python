class Persona():
    #Propiedades
    nombre = ""
    edad = 0

    #Constructor / Metodos magicos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __add__(self, persona):
        pareja = Pareja(self, persona)
        return pareja

class Pareja():
    #Propiedades
    relacion = []

    #Constructor
    def __init__(self, persona1, persona2):
        self.relacion.append(persona1)
        self.relacion.append(persona2)
    def __add__(self, persona):
        familia = Familia()
        familia.añadir_miembro(persona)
        familia.añadir_miembro(self.relacion[0])
        familia.añadir_miembro(self.relacion[1])
        return familia

    #Metodos
    def mostrar(self):
        for persona in self.relacion:
            print(persona.nombre)

class Familia():
    #Propiedades
    miembros = []

    #Metodos
    def añadir_miembro(self, persona):
        self.miembros.append(persona)
    def mostrar(self):
        for persona in self.miembros:
            print(persona.nombre)


persona1 = Persona("David", 20)
persona2 = Persona("Santi", 21)
persona3 = Persona("Jorge", 45)
persona4 = Persona("Rut", 45)
persona5 = Persona("Kerit", 18)

pareja = persona3 + persona4
pareja.mostrar()
print("------------------")
familia = pareja + persona1
familia.mostrar()