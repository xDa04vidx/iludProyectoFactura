from modelo.usuario import Usuario
from vista.vista_registro import VistaRegistro
from vista.vista_productos import VistaProductos
from vista.vista_clasificacion import VistaClasificacion
from modelo.servicios import enviar_correo
from modelo.datos_producto import PRODUCTOS_POR_CATEGORIA
import tkinter as tk

class Controlador:
    def __init__(self):
        self.usuario = Usuario()
        self.root = tk.Tk()
        self.root.title("Aplicación MVC")
        self.root.geometry("500x400")

        self.vista_registro = VistaRegistro(self.root, self)
        self.vista_productos = VistaProductos(self.root, self)
        self.vista_clasificacion = VistaClasificacion(self.root,self)

        self.vista_registro.pack()  # Mostrar solo la vista de registro

    def guardar_y_mostrar_clasificacion(self, nombre, correo, producto):
        # Guarda los datos del usuario
        self.usuario.guardar_datos(nombre, correo, producto)

        # Cambia de vista
        self.vista_registro.pack_forget()
        self.vista_clasificacion.pack()

    def mostrar_productos(self, categoria):
        self.vista_clasificacion.pack_forget()
        productos = PRODUCTOS_POR_CATEGORIA.get(categoria,[])
        self.vista_productos.mostrar_por_categoria(categoria,productos)
        self.vista_productos.pack()

    def volver_clasificacion(self):
        # Cambia de vista
        self.vista_productos.pack_forget()
        self.vista_clasificacion.pack()

    def volver_a_registro(self):
        self.vista_clasificacion.pack_forget()
        self.vista_registro.pack()

    def enviar_confirmacion_por_correo(self):
        nombre = self.usuario.nombre
        correo = self.usuario.correo
        producto = self.usuario.producto
        return enviar_correo(nombre, correo, producto)

    def run(self):
        self.root.mainloop()
