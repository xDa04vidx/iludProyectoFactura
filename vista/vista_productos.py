import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

ruta_imagenes = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imagenes"))

class VistaProductos(tk.Frame):
    def __init__(self, root, controlador):
        super().__init__(root)
        self.controlador = controlador

        self.selecciones = {}
        self.imagenes = {}

        self.label_titulo = tk.Label(self, text="", font=("Arial", 14, "bold"))
        self.label_titulo.pack(pady=10)

        self.marco_productos = tk.Frame(self)
        self.marco_productos.pack()

        tk.Button(self, text="Enviar correo", command=self.enviar_correo).pack(pady=5)
        tk.Button(self, text="Volver al registro", command=self.volver).pack(pady=5)

    def mostrar_por_categoria(self, categoria):
        # Limpiar productos anteriores
        for widget in self.marco_productos.winfo_children():
            widget.destroy()

        self.selecciones = {}
        self.imagenes = {}

        self.label_titulo.config(text=f"📦 Productos - Categoría: {categoria}")

        # Puedes definir distintos sets de productos por categoría:
        productos_por_categoria = {
            "Celulares": [
                {"nombre": "iPhone 16 pro max", "precio": "$1,199.00 USD", "imagen": os.path.join(ruta_imagenes, "iphone15.jpg")},
                {"nombre": "iPhone 15", "precio": "$729.99 USD", "imagen": os.path.join(ruta_imagenes, "iphone15.jpg")},
                {"nombre": "Samsung S25", "precio": "$1,379.00 USD", "imagen": os.path.join(ruta_imagenes, "samsungs25.jpg")}
            ],
            "Computadores": [
                {"nombre": "MacBook Pro", "precio": "$2,399.00 USD", "imagen": os.path.join(ruta_imagenes, "macbook.jpg")},
                {"nombre": "Asus ROG", "precio": "$1,799.00 USD", "imagen": os.path.join(ruta_imagenes, "asus.jpg")}
            ],
            "Estéreos": [
                {"nombre": "Sony Vintage", "precio": "$299.99 USD", "imagen": os.path.join(ruta_imagenes, "sony.jpg")}
            ],
            "Auriculares": [
                {"nombre": "AirPods Pro", "precio": "$249.00 USD", "imagen": os.path.join(ruta_imagenes, "airpods.jpg")}
            ]
        }

        productos = productos_por_categoria.get(categoria, [])

        for producto in productos:
            frame = tk.Frame(self.marco_productos, borderwidth=2, relief="ridge", padx=10, pady=10)
            frame.pack(pady=5, padx=5, fill="x")

            try:
                img = Image.open(producto["imagen"]).resize((60, 60))
                img_tk = ImageTk.PhotoImage(img)
                self.imagenes[producto["nombre"]] = img_tk
            except:
                img_tk = None

            if img_tk:
                label_img = tk.Label(frame, image=img_tk)
                label_img.pack(side="left")

            nombre_precio = f"{producto['nombre']} - {producto['precio']}"
            var = tk.BooleanVar()
            chk = tk.Checkbutton(frame, text=nombre_precio, variable=var)
            chk.pack(side="left", padx=10)

            self.selecciones[producto["nombre"]] = var

    def enviar_correo(self):
        resultado = self.controlador.enviar_confirmacion_por_correo()
        if resultado is True:
            messagebox.showinfo("Correo", "✅ Correo enviado correctamente.")
        else:
            error = resultado[1] if isinstance(resultado, tuple) else "Error desconocido"
            messagebox.showerror("Error", f"❌ No se pudo enviar el correo:\n{error}")

    def volver(self):
        self.controlador.volver_clasificacion()
