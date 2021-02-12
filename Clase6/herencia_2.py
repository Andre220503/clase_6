class Terrestre:
    def desplazar(self):
        print("El animal esta caminando.")

class Acuatico:
    def desplazar(self):
        print("El animal está nadando.")

    def saludar(self):
        print("Animal saluda.")

class Cocodrilo(Terrestre, Acuatico):
    pass


cocodrilo = Cocodrilo()
cocodrilo.desplazar()
cocodrilo.saludar()

#perro = Terrestre()
#perro.desplazar()

#pez = Acuatico()
#pez.desplazar()

