from Sistema_aire import Sistema_aire
from Usuario import Usuario
import time 

usuario = Usuario()
sistema = Sistema_aire()

while True: 
    datos = usuario.ingresar_datos()
    if datos:
        temperatura, humedad = datos
        sistema.Encender_aire(temperatura, humedad)
        time.sleep(3)

        if not usuario.continuar():
            break
