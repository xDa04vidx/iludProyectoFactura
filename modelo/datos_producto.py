import os

ruta_imagenes = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "imagenes"))

PRODUCTOS_POR_CATEGORIA = {
    "Celulares": [
        {"id":1, "nombre": "iPhone 16 pro max", "precio": "$729.99 USD", "imagen": os.path.join(ruta_imagenes, "iphone16.jpg")},
        {"id":2, "nombre": "iPhone 15", "precio": "$729.99 USD", "imagen": os.path.join(ruta_imagenes, "iphone15.jpg")},
        {"id":3, "nombre": "Samsung S25", "precio": "$1,379.00 USD", "imagen": os.path.join(ruta_imagenes, "samsungs25.jpg")}
    ],
    "Computadores": [
        {"id":1, "nombre": "MacBook Air 2025", "precio": "$815.04 USD", "imagen": os.path.join(ruta_imagenes, "mac.jpeg")},
        {"id":2, "nombre": "Acer predator helios 18 AI", "precio": "$1,799.00 USD", "imagen": os.path.join(ruta_imagenes, "acer.jpeg")},
        {"id":3, "nombre": "HP Elitebook 650 G10 Intel", "precio": "$1,699.00 USD", "imagen": os.path.join(ruta_imagenes, "hp.jpeg")}
    ],
    "Estéreos": [
        {"id":1, "nombre": "Toca discos Victrola Navigator", "precio": "$169.99 USD", "imagen": os.path.join(ruta_imagenes, "toca_discos.jpg")},
        {"id":2, "nombre": "Boombox portatil TechPlay", "precio": "$229.95 USD", "imagen": os.path.join(ruta_imagenes, "stereo.png")}
    ],
    "Auriculares": [
        {"id":1, "nombre": "SONY Walkman WM-F31", "precio": "$349.00 USD", "imagen": os.path.join(ruta_imagenes, "walkman.png")},
        {"id":2, "nombre": "Appel iPod Classic 17th", "precio": "$249.00 USD", "imagen": os.path.join(ruta_imagenes, "ipod.png")}
    ]
}