import tkinter as tk
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

        tk.Button(self, text="Volver a clasificacion", command=self.volver).pack(pady=5)
        tk.Button(self, text="Guardar", command=self.guardar_seleccion).pack(pady=5)

    def mostrar_por_categoria(self, categoria, productos):

        self.productos_visibles = productos

        for widget in self.marco_productos.winfo_children():
            widget.destroy()

        self.selecciones = {}
        self.imagenes = {}

        self.label_titulo.config(text=f"📦 Productos - Categoría: {categoria}")

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

    def guardar_seleccion(self):
        for nombre_producto, var in self.selecciones.items():
            if var.get():
                for prod in self.productos_visibles:
                    if prod["nombre"] == nombre_producto:
                        print(prod["nombre"])
                        nombre = prod["nombre"]
                        precio = float(prod["precio"].replace("$", "").replace(",", "").replace("USD", "").strip())

                        self.controlador.agregar_compra(nombre, precio)
                        break


    def volver(self):
        self.controlador.volver_clasificacion()
