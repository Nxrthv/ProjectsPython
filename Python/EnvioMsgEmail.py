#Librerias Usadas
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

#Cargar la Variable de Contraseña que esta en el Archcivo .env
load_dotenv()

email_sender = 'vargasesquivelandres@gmail.com'     #Correo Emisor
password = os.getenv("password")      #Contraseña Emisor
email_reciver = input('Ingrese el Correo del Cliente: ')    #Correo del Receptor
ruta_pdf = 'Ficha de Reparacion.pdf'    #Ruta del PDF

#Contenido del Correo
mensaje = MIMEMultipart()
mensaje['From'] = email_sender
mensaje['To'] = email_reciver
mensaje['Subject'] = 'Ficha de Recepcion y Reparacion - Dr.Laptop'
body = """Con esta Ficha puede Venir a Recoger su Equipo ;)"""
mensaje.attach(MIMEText(body, 'plain'))

    #Union del Correo y el Archivo PDF
with open(ruta_pdf, 'rb') as pdf_file:
    adjunto_pdf = MIMEApplication(pdf_file.read(), _subtype='pdf')
    adjunto_pdf.add_header('content-disposition', 'attachment', filename=ruta_pdf)
    mensaje.attach(adjunto_pdf)

#Conexion
servidor_smtp = 'smtp.gmail.com'
puerto_smtp = 587
conexion_smtp = smtplib.SMTP(servidor_smtp, puerto_smtp)

#Registro
conexion_smtp.starttls()
conexion_smtp.login(email_sender, password)

#Recibe el correo del Emisor y Receptor asi como el contenido del Correo
conexion_smtp.sendmail(email_sender, email_reciver, mensaje.as_string())

conexion_smtp.quit()    #Cierra la Conexion

print("Correo Enviado Exitosamente")    #Alerta de envio Exitoso