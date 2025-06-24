class Usuario:
    def __init__(self):
        self.nombre = ""
        self.correo = ""
        self.compras = []

    def guardar_datos(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        print("Datos guardados:")
        print(f"Nombre: {nombre}, Correo: {correo}")

    def agregar_compra(self, nombre_producto, precio):
        self.compras.append({"nombre":nombre_producto, "precio":precio})
    
    def limpiar_compras(self):
        self.compras = []

    def obtener_total(self):
        return sum(compra.precio for compra in self.compras)

    def listar_compras(self):
        return [str(c) for c in self.compras]

