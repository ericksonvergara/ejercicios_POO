class Numero:
    def __init__(self):
        self.numero_ingresado = ""
        
    def tomar_numero(self):
        self.numero_ingresado = int(input("\n Ingresa un número: "))
        return self.numero_ingresado
        
    def mostrar_numero(self):
        print(self.numero_ingresado)
