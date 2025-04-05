class Usuario:
    def __init__(self):
        self.nombre = ""
        self.membresia = ""
        self.empleado = ""

    def tomar_datos(self):
        self.nombre = input("\n🧑 Por favor, ingresa tu nombre: ").capitalize()
        self.membresia = input("🏷️ ¿Cuentas con membresía? (si/no): ").strip().lower()
        self.empleado = input("🛠️ ¿Eres parte del personal? (si/no): ").strip().lower()
