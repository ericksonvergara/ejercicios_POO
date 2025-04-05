class SistemaLuces:
    def __init__(self):
        self.estado = True

    def activar_luces(self, hay_movimiento, es_noche):
        if es_noche and hay_movimiento:
            return (f"\n ¿Es de noche?: {es_noche}, 🚶‍♂️ ¿Movimiento detectado?: {hay_movimiento}\n ¡LUCES ENCENDIDAS!")
        else:
            return (f"\n ¿Es de noche?: {es_noche}, 🚶‍♂️ ¿Movimiento detectado?: {hay_movimiento}\n ¡LUCES APAGADAS!")
