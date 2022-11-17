class Serie():
    #Propiedades
    titulo = ""
    temporadas = 3
    entregado = False
    genero = ""
    creador = ""

    #Constructor
    def __init__(self, titulo, temporadas, genero, creador):
        self.titulo = titulo
        self.temporadas = temporadas
        self.genero = genero
        self.creador = creador

    def get_titulo(self): return self.titulo
    def set_titulo(self, titulo): self.titulo = titulo
    def get_temporadas(self): return self.temporadas
    def set_temporadas(self, temporadas): self.temporadas = temporadas
    def get_genero(self): return self.genero
    def set_genero(self, genero): self.genero = genero
    def get_creador(self): return self.creador
    def set_creador(self, creador): self.creador = creador

    def __str__(self):
        return "Titulo: " + self.titulo + " Temporadas: " + str(self.temporadas) \
               + " Genero: " + self.genero + " Creador: " + self.creador



class Videojuego():
    #Propiedades
    titulo = ""
    horasJuagads = 10
    entregado = False
    genero = ""
    compañia = ""

    #Constructor
    def __init__(self, titulo, horasJuagads, genero, compañia):
        self.titulo = titulo
        self.horasJuagads = horasJuagads
        self.genero = genero
        self.compañia = compañia

    def get_titulo(self): return self.titulo
    def set_titulo(self, titulo): self.titulo = titulo
    def get_horasJuagads(self): return self.horasJuagads
    def set_horasJuagads(self, horasJuagads): self.horasJuagads = horasJuagads
    def get_genero(self): return self.genero
    def set_genero(self, genero): self.genero = genero
    def get_compañia(self): return self.compañia
    def set_compañia(self, compañia): self.compañia = compañia

    def __str__(self):
        return "Titulo: " + self.titulo + " Horas jugadas: " + \
               str(self.horasJuagads) + " Genero: " + self.genero \
               + " Compañia: " + self.compañia + " Entregado: " + str(self.entregado)



class Entregable():
    def entregar(self): self.entregado = True
    def devolver(self): self.entregado = False
    def isEntregado(self): return self.entregado
    def compareTo(self, horasJuagads): return self.horasJuagads - horasJuagads



class Main():
    #Array de 5 objetos de la clase Serie
    series = [Serie("Serie1", 1), Serie("Serie2", 2), Serie("Serie3", 3), Serie("Serie4", 4), Serie("Serie5", 5)]
    #Array de 5 objetos de la clase Videojuego
    videojuegos = [Videojuego("Videojuego1", 1), Videojuego("Videojuego2", 2), Videojuego("Videojuego3", 3),
                   Videojuego("Videojuego4", 4), Videojuego("Videojuego5", 5)]

    #Entrega videojuegos y series con el metodo entregar().
    for serie in series:
        serie.entregar()
    for videojuego in videojuegos:
        videojuego.entregar()

    #Cuenta cuantos videojuegos y series hay entregados y devuélvelos.
    entregados = 0
    for serie in series:
        if serie.isEntregado():
            entregados += 1
    print("Series entregadas: " + str(entregados))
    entregados = 0
    for videojuego in videojuegos:
        if videojuego.isEntregado():
            entregados += 1
    print("Videojuegos entregados: " + str(entregados))

    #Devuelve el videojuego o serie con más horas estimadas. Mostrarlos con todos sus atributos con el método __str__().
    horas = 0
    for serie in series:
        if serie.get_temporadas() > horas:
            horas = serie.get_temporadas()
    print("Serie con mas temporadas: " + str(horas))
    horas = 0
    for videojuego in videojuegos:
        if videojuego.get_horasJuagads() > horas:
            horas = videojuego.get_horasJuagads()
    print("Videojuego con mas horas jugadas: " + str(horas))

if __name__ == "__main__":
    Main()
