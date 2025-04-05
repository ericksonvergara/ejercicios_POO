import random

class Detector:
    def __init__(self):
        self.sensor1 = True
        self.sensor2 = True
        self.sensor3 = True
        self.turno_noche = True

    def obtener_lecturas(self):
        sensor1 = random.choice([True, False])
        sensor2 = random.choice([True, False])
        sensor3 = random.choice([True, False])
        turno_noche = random.choice([True, False])
        return sensor1, sensor2, sensor3, turno_noche
