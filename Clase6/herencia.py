class Rectangulo:
    def __init__(self, base , altura):
        self.base = base 
        self.altura = altura

    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return self.base * 2 + self.altura * 2

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


rectangulo = Rectangulo(10, 2)
area = rectangulo.area()
print(area)


cuadrado = Cuadrado(10)
area = cuadrado.area()
print(area)