class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f"{self.nombre} caminando.")


class Ciclista(Persona):
    def avanza(self):
        print(f"{self.nombre} está andando en bicicleta.")



c = Ciclista("Alvaro")
c.avanza()