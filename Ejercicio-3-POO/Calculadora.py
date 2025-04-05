from Usuario import Usuario

class Calculadora:
    def __init__(self):
        pass

    def calcular(self, cliente):
        if cliente.signo_operacion == "+":
            resultado = cliente.valor1 + cliente.valor2
        elif cliente.signo_operacion == "-":
            resultado = cliente.valor1 - cliente.valor2
        elif cliente.signo_operacion == "*":
            resultado = cliente.valor1 * cliente.valor2
        elif cliente.signo_operacion == "/":
            if cliente.valor2 == 0:
                return "\n Error: No se puede dividir entre cero."
            resultado = cliente.valor1 / cliente.valor2

        return f"\n Resultado: {cliente.valor1} {cliente.signo_operacion} {cliente.valor2} = {resultado:.2f}"
