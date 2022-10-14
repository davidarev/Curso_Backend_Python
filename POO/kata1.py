class Alumno():
    #Propiedades
    nombre = ""
    apellido = ""
    dni = ""
    edad = 0
    notaMedia = 0
    notas = []
    #Constructor
    def __init__(self, Nombre, Apellido, Dni, Edad):
        self.nombre = Nombre
        self.apellido = Apellido
        self.dni = Dni
        self.edad = Edad
    #Metodos
    def saludar(self):
        print("Hola, me llamo", self.nombre, self.apellido)
    def añadirNota(self, Nota):
        if Nota >= 0 and Nota <= 10:
            self.notas.append(Nota)
            print("Nota añadida:", Nota)
        else:
            print("La nota debe tener un valor entre el 0 y el 10")
    def mostrarNotaMedia(self):
        sum = 0
        for nota in self.notas:
            sum += nota
        self.notaMedia = sum / len(self.notas)
        print("La nota media es:", self.notaMedia)
    def cumplirAños(self):
        self.edad += 1
        print("Ahora la edad del alumno es de", self.edad, "años")

alumno1 = Alumno("David", "Arevalo", "32638151T", 20)
alumno1.saludar()
alumno1.añadirNota(7), alumno1.añadirNota(9), alumno1.añadirNota(8), alumno1.añadirNota(11)
alumno1.mostrarNotaMedia()
alumno1.cumplirAños()