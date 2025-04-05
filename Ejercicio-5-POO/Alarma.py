from Detector import Detector

class Alarma:
    def __init__(self):
        pass 

    def activar_modo_automatico(self, sensor_a, sensor_b, sensor_c, es_noche):
        print(f"\n ¿Es de noche?: {'Sí' if es_noche else 'No'}")
        print(f" Movimiento detectado -> Sensor 1: {'Sí' if sensor_a else 'No'}, Sensor 2: {'Sí' if sensor_b else 'No'}, Sensor 3: {'Sí' if sensor_c else 'No'}")
        
        if (es_noche and sensor_a and sensor_b) or \
           (es_noche and sensor_b and sensor_c) or \
           (es_noche and sensor_a and sensor_c):
            print("¡ALERTA! La alarma ha sido activada.\n")
        else:
            print("La alarma permanece desactivada.\n")

    def activar_modo_manual(self):
        print("\n Configuración manual de la alarma:")
        print("1️. Encender la alarma")
        print("2️. Apagar la alarma")
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            print("Alarma activada manualmente.")
        elif opcion == 2:
            print("Alarma desactivada manualmente.")
        else:
            print("Opción inválida. Intenta de nuevo.")
