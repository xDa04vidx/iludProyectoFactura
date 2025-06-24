import tkinter as tk
from tkinter import messagebox


class VistaClasificacion(tk.Frame):
    def __init__(self, root, controlador):
        super().__init__(root)
        self.controlador = controlador

        tk.Label(self, text="Clasificación de productos", font=("Arial", 14, "bold")).pack(pady=10)

        # Sección NUEVO
        tk.Label(self, text="🔹 NUEVO", font=("Arial", 12, "bold")).pack(pady=(15, 5))

        frame_nuevo = tk.Frame(self)
        frame_nuevo.pack()

        tk.Button(frame_nuevo, text="Celulares", width=20, command=lambda: self.seleccionar("Celulares")).pack(padx=10, side="left")
        tk.Button(frame_nuevo, text="Computadores", width=20, command=lambda: self.seleccionar("Computadores")).pack(padx=10, side="left")

        # Sección VIEJO
        tk.Label(self, text="🔸 VIEJO", font=("Arial", 12, "bold")).pack(pady=(20, 5))

        frame_viejo = tk.Frame(self)
        frame_viejo.pack()

        tk.Button(frame_viejo, text="Estéreos", width=20, command=lambda: self.seleccionar("Estéreos")).pack(padx=10, side="left")
        tk.Button(frame_viejo, text="Auriculares", width=20, command=lambda: self.seleccionar("Auriculares")).pack(padx=10, side="left")

        tk.Button(self, text="Limpiar", command=self.limpiar_productos).pack(pady=5)
        tk.Button(self, text="Pagar", command=self.enviar_correo).pack(pady=5)
        tk.Button(self, text="← Volver", command=self.volver).pack(pady=20)
        

    def volver(self):
        self.controlador.volver_a_registro()

    def seleccionar(self, categoria):
        self.controlador.mostrar_productos(categoria)

    def enviar_correo(self):
        resultado = self.controlador.enviar_confirmacion_por_correo()
        if resultado is True:
            messagebox.showinfo("Correo", "✅ Correo enviado correctamente.")
        else:
            error = resultado[1] if isinstance(resultado, tuple) else "Error desconocido"
            messagebox.showerror("Error", f"❌ No se pudo enviar el correo:\n{error}")

    def limpiar_productos(self):
        self.controlador.limpiar_arreglo()
    
    def actualizar(self):
        for widget in self.winfo_children():
            if hasattr(widget, "es_dinamico") and widget.es_dinamico:
                widget.destroy()

        productos_seleccionados = self.productos()

        if len(productos_seleccionados) > 0:
            label = tk.Label(self, text="Productos seleccionados", font=("Arial", 12, "bold"))
            label.pack(pady=5)
            label.es_dinamico = True

            for item in productos_seleccionados:
                texto = f"{item['nombre']} - ${item['precio']}"
                label_item = tk.Label(self, text=texto, font=("Arial", 12))
                label_item.pack()
                label_item.es_dinamico = True

    
    def productos(self):
        return self.controlador.productos_seleccionados()
        

