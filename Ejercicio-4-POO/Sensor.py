class Sensor:
    def __init__(self):
        pass

    def evaluar_temperatura(self, valor_temp):
        if valor_temp < 10:
            return "Calefactor encendido"
        elif 10 <= valor_temp < 25:
            return "Temperatura óptima del invernadero"
        elif valor_temp >= 25:
            return "Ventilador activado"
