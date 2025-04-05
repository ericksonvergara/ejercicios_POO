class Usuario:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.signo_operacion = ""

    def ingresar_datos(self):
        while True:
            try:
                self.valor1 = float(input("\n🔢 Ingresa el primer número: "))
                self.valor2 = float(input("🔢 Ingresa el segundo número: "))
                break
            except ValueError:
                print("❗ Error: Solo se permiten valores numéricos.")

        while True:
            self.signo_operacion = input("✏️ Ingresa la operación (+, -, *, /): ").strip()
            if self.signo_operacion in ["+", "-", "*", "/"]:
                break
            else:
                print("⚠️ Operación no válida. Intenta de nuevo.")

        return self.valor1, self.valor2, self.signo_operacion
