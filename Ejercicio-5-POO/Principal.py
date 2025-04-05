from Detector import Detector
from Alarma import Alarma
import time

detector_sensores = Detector()
sistema_alarma = Alarma()

while True:
    try:
        sistema_alarma.activar_modo_manual()
        s1, s2, s3, noche = detector_sensores.obtener_lecturas()
        sistema_alarma.activar_modo_automatico(s1, s2, s3, noche)

        seguir = input("🔄 ¿Deseas seguir con el monitoreo? (s/n): ").lower()
        if seguir != "s":
            print("🛑 Sistema finalizado. ¡Hasta luego!")
            break
        time.sleep(3)
    except ValueError:
        print("❌ Entrada inválida. Por favor elige una opción correcta.")
