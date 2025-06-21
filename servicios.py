import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

def enviar_correo(nombre, correo, producto):
    remitente = os.getenv("EMAIL_REMITENTE")
    contrasena = os.getenv("EMAIL_PASSWORD")

    asunto = "Confirmación de producto"
    mensaje = f"Hola {nombre}, has elegido: {producto}"

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = correo
    msg['Subject'] = asunto
    msg.attach(MIMEText(mensaje, 'plain'))

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, contrasena)
        servidor.send_message(msg)
        servidor.quit()
        print("✅ Correo enviado correctamente.")
        return True
    except Exception as e:
        print("❌ Error al enviar el correo:", e)
        return False, str(e)
