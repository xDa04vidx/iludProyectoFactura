import tkinter as tk

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
        
        tk.Button(self, text="← Volver", command=self.volver).pack(pady=20)

    def volver(self):
        self.controlador.volver_a_registro()

    def seleccionar(self, categoria):
        self.controlador.mostrar_productos(categoria)

