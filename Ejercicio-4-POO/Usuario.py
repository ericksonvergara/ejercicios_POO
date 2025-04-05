class Usuario:
    def __init__(self):
        self.temperatura_actual = ""

    def solicitar_temperatura(self):
        while True:
            try:
                return int(input("\n Ingresa la temperatura actual del invernadero: "))
            except ValueError:
                print(" Error: Por favor, introduce un número válido.")
