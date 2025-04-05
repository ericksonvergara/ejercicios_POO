class Usuario:
    def __init__(self):
        self.nombre_usuario = ""
        self.apellido_usuario = ""
        self.asientos_a_reservar = 0
    
    def ingresar_datos(self):
        self.nombre_usuario = input("\n📝 Ingresa tu nombre: ")
        self.apellido_usuario = input("📝 Ingresa tu apellido: ")
    
    def ingresar_reserva(self):
        while True:
            try:
                self.asientos_a_reservar = int(input("\n🎫 ¿Cuántos asientos deseas reservar?: "))
                if self.asientos_a_reservar >= 0:
                    break
                else:
                    print("⚠️ Por favor, ingresa un número válido mayor o igual a 0.")
            except ValueError:
                print("❌ Error: solo se permiten números enteros.")
    
    def obtener_nombre_completo(self):
        return f"{self.nombre_usuario} {self.apellido_usuario}"
