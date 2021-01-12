class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, name, edad, tipo):
        if str(tipo)=='leon':
            self.animals.append(Leones(name, edad))
        elif str(tipo)=='tigre':
            self.animals.append(Tigres(name, edad))
        elif str(tipo) == 'oso':
            self.animals.append(Osos(name, edad))
        else:
            print('tipo no implementado')
        return self.animals[len(self.animals)-1]

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animals(Zoo):
    def __init__(self, name, edad, salud, felicidad):
        self.name = name
        self.edad =edad
        self.nivel_salud=salud
        self.nivel_felicidad=felicidad

    def display_info(self):
        print('\nNombre:\t', self.name, '\nEdad:\t', self.edad, '\nNivel de salud:\t', self.nivel_salud, '\nNivel de felicidad:\t', self.nivel_felicidad)
        return self

    def alimentacion(self):
        self.nivel_salud += 10
        self.nivel_felicidad += 10

class Leones(Animals):
    def __init__(self, name, edad, liderazgo=100):
        self.liderazgo = liderazgo
        super().__init__(name, edad, 1000, 1000)

    def display_info(self):
        print('\nNombre:\t', self.name, '\nEdad:\t', self.edad, '\nNivel de salud:\t', self.nivel_salud, '\nNivel de felicidad:\t', self.nivel_felicidad, '\nNivel de liderazgo:\t', self.liderazgo)
        return self

    def alimentacion(self):
        self.nivel_salud += 200
        self.nivel_felicidad += 1000

class Tigres(Animals):
    def __init__(self, name, edad):
        super().__init__(name, edad, 1000, 600)

    def alimentacion(self):
        self.nivel_salud += 500
        self.nivel_felicidad += 100

class Osos(Animals):
    def __init__(self, name, edad):
        super().__init__(name, edad, 800, 1000)



zoologico=Zoo('Buin Zoo')
zoologico.add_animal('Simba',30,'leon').alimentacion()
zoologico.add_animal('tiger',20, 'tigre')
zoologico.print_all_info()



