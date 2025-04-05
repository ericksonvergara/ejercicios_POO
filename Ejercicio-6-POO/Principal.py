from Alarma import SistemaLuces
from Sistema import ControlHabitacion
import time 

habitacion = ControlHabitacion()
luces_auto = SistemaLuces()

while True:
    mov_detectado, es_turno_noche = habitacion.obtener_datos_sensor()
    luces_auto.activar_luces(mov_detectado, es_turno_noche)
    habitacion.gestionar_luces(mov_detectado, es_turno_noche)

    continuar = input("\n🔁 ¿Desea continuar usando el sistema? (s/n): ").strip().lower()
    if continuar != "s":
        print("\n🛑 El sistema ha terminado su ejecución.")
        break
    time.sleep(3)
