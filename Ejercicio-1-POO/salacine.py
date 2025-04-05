class Sala:
    def __init__(self, capacidad_total=50):
        self.asientos_disponibles = capacidad_total
    
    def verificar_disponibilidad(self, cantidad):
        return cantidad <= self.asientos_disponibles
    
    def reservar_asientos(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.asientos_disponibles -= cantidad
            print("\n ¡Reserva confirmada!")
            print(f"🪑 Asientos disponibles restantes: {self.asientos_disponibles}")
            return True
        else:
            print(f"\n No hay suficientes asientos disponibles. Solo quedan {self.asientos_disponibles}.")
            return False
    
    def esta_llena(self):
        return self.asientos_disponibles == 0
