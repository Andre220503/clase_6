class coordenada:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, coor_x):
        if coor_x >= 0 :
            self.__x = coor_x
        else:
            raise ValueError("No es una coordenada válida.")
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, coor_y):
        if coor_y >= 0 :
            self.__y = coor_y
        else:
            raise ValueError("No es una coordenada válida.")        
    
    def distancia(self, otra_coordenada):
        if isinstance(otra_coordenada, coordenada):
            x_diff = (self.x - otra_coordenada.x) ** 2
            y_diff = (self.y - otra_coordenada.y) ** 2

            distancia = (x_diff + y_diff) ** 0.5
            return distancia

        print("Debes ingresar una coordenada")

coord_1 = coordenada()
coord_1.x = 10
coord_1.y = 20

coord_2 = coordenada()
coord_2.x = 3
coord_2.y = 5

distancia = coord_1.distancia(coord_2)

