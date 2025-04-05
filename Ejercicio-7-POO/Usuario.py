class Usuario:
    def __init__(self):
        pass

    def ingresar_datos(self):
        try:
            temperatura = float(input("\n Introduzca la temperatura del ambiente: "))
            humedad = float(input("Introduzca el nivel de humedad (%): "))
            return temperatura, humedad
        except ValueError:
            print("\n Error: Por favor ingrese valores numéricos válidos.")

    def continuar(self):
        while True:
            opcion = input("\n ¿Desea seguir utilizando el sistema? (s/n): ").strip().lower()
            if opcion == "s":
                return True
            elif opcion == "n":
                print("\n El sistema se ha cerrado correctamente.")
                return False
            else:
                print("\n Opción inválida. Ingrese 's' para sí o 'n' para no.")
