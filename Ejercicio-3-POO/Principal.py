from Calculadora import Calculadora
from Usuario import Usuario

calculadora_main = Calculadora()

while True:
    cliente = Usuario()
    cliente.ingresar_datos()

    resultado = calculadora_main.calcular(cliente)
    print(resultado)

    continuar = input("\n ¿Quieres hacer otro cálculo? (s/n): ").strip().lower()
    if continuar != "s":
        print("Gracias por usar la calculadora. ¡Hasta la próxima!")
        break
