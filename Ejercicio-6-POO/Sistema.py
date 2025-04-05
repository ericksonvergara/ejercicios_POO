from Alarma import SistemaLuces
import random

class ControlHabitacion:
    def __init__(self):
        pass

    def obtener_datos_sensor(self):
        movimiento = random.choice([True, False])
        noche = random.choice([True, False])
        return movimiento, noche

    def gestionar_luces(self, movimiento, noche):
        luces = SistemaLuces()
        estado = luces.activar_luces(movimiento, noche)
        print(estado)
