import time
from Sensor import Sensor
from Usuario import Usuario

persona = Usuario()
dispositivo = Sensor()

while True:
    lectura = persona.solicitar_temperatura()
    estado_ambiente = dispositivo.evaluar_temperatura(lectura) 
    print(f"🔎 Estado actual del sistema: {estado_ambiente}")
    
    continuar = input("\n¿Deseas seguir monitoreando la temperatura? (s/n): ").lower()
    if continuar != "s":
        print("🚪 El sistema se ha cerrado. ¡Hasta pronto!")
        break
    time.sleep(5)
