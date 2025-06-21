class Usuario:
    def __init__(self):
        self.nombre = ""
        self.correo = ""
        self.producto = ""

    def guardar_datos(self, nombre, correo, producto):
        self.nombre = nombre
        self.correo = correo
        self.producto = producto
        print("Datos guardados:")
        print(f"Nombre: {nombre}, Correo: {correo}, Producto: {producto}")

