import os

ruta_imagenes = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imagenes"))

PRODUCTOS_POR_CATEGORIA = {
    "Celulares": [
        {"nombre": "iPhone 16 pro max", "precio": "$729.99 USD", "imagen": os.path.join(ruta_imagenes, "iphone16.jpg")},
        {"nombre": "iPhone 15", "precio": "$729.99 USD", "imagen": os.path.join(ruta_imagenes, "iphone15.jpg")},
        {"nombre": "Samsung S25", "precio": "$1,379.00 USD", "imagen": os.path.join(ruta_imagenes, "samsungs25.jpg")}
    ],
    "Computadores": [
        {"nombre": "MacBook Air 2025", "precio": "$815.04 USD", "imagen": os.path.join(ruta_imagenes, "mac.jpeg")},
        {"nombre": "Acer predator helios 18 AI", "precio": "$1,799.00 USD", "imagen": os.path.join(ruta_imagenes, "acer.jpeg")},
        {"nombre": "HP Elitebook 650 G10 Intel", "precio": "$1,699.00 USD", "imagen": os.path.join(ruta_imagenes, "hp.jpeg")}
    ],
    "Estéreos": [
        {"nombre": "Toca discos Victrola Navigator", "precio": "$169.99 USD", "imagen": os.path.join(ruta_imagenes, "toca_discos.jpg")},
        {"nombre": "Boombox portatil TechPlay", "precio": "$229.95 USD", "imagen": os.path.join(ruta_imagenes, "stereo.png")}
    ],
    "Auriculares": [
        {"nombre": "SONY Walkman WM-F31", "precio": "$349.00 USD", "imagen": os.path.join(ruta_imagenes, "walkman.png")},
        {"nombre": "Appel iPod Classic 17th", "precio": "$249.00 USD", "imagen": os.path.join(ruta_imagenes, "ipod.png")}
    ]
}