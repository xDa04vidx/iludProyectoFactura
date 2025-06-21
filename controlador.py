from modelo import Usuario
from vista import Vista
from servicios import enviar_correo
import tkinter as tk

class Controlador:
    def __init__(self):
        self.usuario = Usuario()
        self.root = tk.Tk()
        self.vista = Vista(self.root, self)

    def guardar(self, nombre, correo, producto):
        self.usuario.guardar_datos(nombre, correo, producto)

    def enviar_confirmacion_por_correo(self):
        nombre = self.usuario.nombre
        correo = self.usuario.correo
        producto = self.usuario.producto
        return enviar_correo(nombre, correo, producto)

    def run(self):
        self.root.mainloop()
