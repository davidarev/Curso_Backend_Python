class Punto2D():
    #Propiedades
    nombre = ""
    x = 0
    y = 0

    #Constructor
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.x = x
        self.y = y

    #Metodos
    def darCordenadas2D(self):
        print("Las cordenadas de", self.nombre, "son:", [self.x, self.y])

class Punto3D(Punto2D): #Aplicamos herencia
    #Propiedades
    z = 0

    #Constructor
    def __init__(self, nombre, x, y, z):
        super().__init__(nombre, x, y) #'super()' ejecuta codigo de la clase padre, en este caso el constructor
        self.z = z

    #Metodos
    def darCordenadas3D(self):
        print("Las cordenadas de", self.nombre, "son:", [self.x, self.y, self.z])


pt1 = Punto2D("Punto 1", 10, 20)
pt2 = Punto3D("Punto 2", 15, 30, 45)
pt1.darCordenadas2D()
pt2.darCordenadas2D()
pt2.darCordenadas3D()