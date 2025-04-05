class Sistema_aire:
    def __init__(self):
        self.estado = ""

    def Encender_aire(self, temperatura, humedad):
        if (temperatura > 28 and humedad > 60) or temperatura > 30:
            print(f"\n🔵 Aire acondicionado ENCENDIDO debido a condiciones climáticas.")
        else:
            print(f"\n⚪ Aire acondicionado APAGADO. Condiciones normales.")
