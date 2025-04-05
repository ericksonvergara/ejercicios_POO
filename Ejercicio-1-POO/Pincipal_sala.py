from UsuariosCine import Usuario
from salacine import Sala

sala_cine = Sala()
cliente = Usuario()
cliente.ingresar_datos()

while not sala_cine.esta_llena():
    cliente.ingresar_reserva()

    if sala_cine.reservar_asientos(cliente.asientos_a_reservar):
        print(f"\n {cliente.obtener_nombre_completo()}, tu reserva se ha realizado correctamente.")
        
    if sala_cine.esta_llena():
        print("\n La sala está completa. No se pueden realizar más reservas.")
        break

    desea_continuar = input("\n¿Quieres hacer otra reserva? (s/n): ").strip().lower()
    if desea_continuar != "s":
        print("\n Gracias por usar el sistema de reservas. ¡Hasta la próxima!")
        break
