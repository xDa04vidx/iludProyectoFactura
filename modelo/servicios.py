import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

def enviar_correo(nombre, correo, productos):
    remitente = os.getenv("EMAIL_REMITENTE")
    contrasena = os.getenv("EMAIL_PASSWORD")

    asunto = "Confirmación de producto"

    # Ruta al archivo HTML
    ruta_html = os.path.join(os.path.dirname(__file__), "plantillas", "plantilla_correo.html")

    try:
        filas = ""
        total = 0
        for prod in productos:
            filas += f"<tr><td>{prod['nombre']}</td><td>${prod['precio']:,.2f} USD</td></tr>"
            total += prod['precio']

        total_str = f"${total:,.2f} USD"
        with open(ruta_html, "r", encoding="utf-8") as f:
            html_template = f.read()

        # Reemplazar variables del HTML
        html_con_datos = (
            html_template
            .replace("{{ nombre }}", nombre)
            .replace("{{ filas }}", filas)
            .replace("{{ total }}", total_str)
        )

        # Crear mensaje
        msg = MIMEMultipart("alternative")
        msg['From'] = remitente
        msg['To'] = correo
        msg['Subject'] = asunto

        parte_html = MIMEText(html_con_datos, 'html')
        msg.attach(parte_html)

        # Envío
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
