import tkinter as tk

class VistaRegistro(tk.Frame):
    def __init__(self, root, controlador):
        super().__init__(root)
        self.controlador = controlador

        tk.Label(self, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        tk.Label(self, text="Correo:").pack()
        self.entry_correo = tk.Entry(self)
        self.entry_correo.pack()

        tk.Button(self, text="Guardar y continuar", command=self.guardar).pack(pady=10)

    def guardar(self):
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        self.controlador.guardar_y_mostrar_clasificacion(nombre, correo)
