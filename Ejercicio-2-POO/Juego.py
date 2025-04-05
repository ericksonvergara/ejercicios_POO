from Numero import Numero

class Juego:
    def __init__(self):
        self.objeto_numero = Numero()
        
    def tomar_dato(self):
        numero = self.objeto_numero.tomar_numero() 
        return numero
        
    def operar(self, numero):
        res1 = numero % 3
        res2 = numero % 5
        if res1 == 0 and res2 == 0:
            print("Resultado: FizzBuzz")
        elif res1 == 0 and res2 != 0:
            print("Resultado: Fizz")
        elif res1 != 0 and res2 == 0:
            print("Resultado: Buzz")
        else:
            print(f"Resultado: {numero}")
    
    def mostrar(self):
        while True:
            opcion = self.continuar()
            if opcion == 1:
                numero = self.tomar_dato()
                self.operar(numero)
            else:
                print("🔚 El programa ha terminado. ¡Gracias por participar!")
                break

    def continuar(self):
        try:
            print("\n Menú de opciones:")
            print("1. Ingresar un número")
            print("2. Salir del programa")
            opcion = int(input("Selecciona una opción: "))
            return opcion
        except ValueError:
            print("\n Entrada inválida. Por favor, ingresa 1 o 2.")
            return self.continuar()
