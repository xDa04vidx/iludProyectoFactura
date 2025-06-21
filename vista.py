import tkinter as tk
from tkinter import messagebox

class Vista:
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("Formulario MVC")
        self.root.geometry("400x300")


        tk.Label(root, text="Nombre:").pack(pady=(10, 0))
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        tk.Label(root, text="Correo:").pack(pady=(10, 0))
        self.entry_correo = tk.Entry(root)
        self.entry_correo.pack()

        tk.Label(root, text="Producto:").pack(pady=(10, 0))
        self.producto_var = tk.StringVar(value="Computador")
        productos = ["Computador", "Celular", "Reproductor MP3"]
        self.producto_menu = tk.OptionMenu(root, self.producto_var, *productos)
        self.producto_menu.pack()

        tk.Button(root, text="Guardar Datos", command=self.enviar_datos).pack(pady=20)
        tk.Button(root, text="Enviar Correo", command=self.enviar_correo).pack(pady=10)

    def enviar_datos(self):
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        producto = self.producto_var.get()
        self.controlador.guardar(nombre, correo, producto)

    def enviar_correo(self):
        correo_enviado = self.controlador.enviar_confirmacion_por_correo()
        if correo_enviado:
            messagebox.showinfo("Correo enviado", "✅ El correo fue enviado correctamente.")
        else:
            error = correo_enviado[1] if isinstance(correo_enviado, tuple) else "Error desconocido"
            messagebox.showerror("Error", f"❌ No se pudo enviar el correo:\n{error}")
