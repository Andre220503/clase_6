class Lavadora:
    def __init__(self):
        pass
    def lavar(self, temperatura="fria"):
        self.llenar_tanque_agua(temperatura)
        self.añadir_detergente()
        self.lavar_ropa()
        self.centrifugar()

        print("FIN.")

    def llenar_tanque_agua(self,temperatura):    
        print(f"Llenando el tanque con agua a {temperatura}")
    def añadir_detergente(self):
        print("Añadiendo detergente.")
    def lavar_ropa(self):
        print("Lavadora lavando ropa...")
    def centrifugar(self):
        print("Centrifugando")

l1 = Lavadora()
l1.lavar("caliente")

l2 = Lavadora()
l2.lavar()               