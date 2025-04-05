from datetime import datetime
from Usuario import Usuario 

class SistemaAcceso:
    def __init__(self):
        self.horario_atencion = (7, 20)  # Horario permitido: de 7 AM a 8 PM

    def dentro_horario(self):
        hora_actual = datetime.now().hour
        return self.horario_atencion[0] <= hora_actual < self.horario_atencion[1]

    def validar_entrada(self, usuario):
        acceso_habilitado = self.dentro_horario()
        if usuario.membresia == "si" and acceso_habilitado or usuario.empleado == "si":
            print(f"ACCESO CONCEDIDO: Bienvenid@ {usuario.nombre} al sistema.")
        else:
            print(f"ACCESO RESTRINGIDO: Lo sentimos, {usuario.nombre}. No puedes ingresar en este momento.")
