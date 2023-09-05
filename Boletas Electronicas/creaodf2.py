import jinja2
import pdfkit
from datetime import datetime

date = datetime.today().strftime("%d %b, %Y")
codigo = "1234"
name = input('Nombre del Cliente: ')
phone = input('Telefono del Cliente: ')
email = input('Correo del Cliente: ')
tipocomputador = input('Tipo de Computador (Escritorio o Portatil): ')
marca = input('Marca del Equipo: ')
tipomantenimiento = input('Tipo de Mantenimiento (Correctivo o Preventivo): ')
asunto = input('Describa el Trabajo a Realizar: ')
rutacss = 'styles.css'

context = {'date':date,
           'codigo':codigo,
           'name':name,'phone'
           :phone,'email':email,
           'tipocomputador':tipocomputador,
           'marca':marca,
           'tipomantenimiento': tipomantenimiento,
           'asunto':asunto}

options = {'page-size': 'letter',
                'margin-top' : '0.05in',
                'margin-bottom': '0.05in',
                'margin-left': '0.05in',
                'margin-right': '0.05in',
                'encoding': 'UTF-8'}

template_loader = jinja2.FileSystemLoader('./')

template_env = jinja2.Environment(loader=template_loader)

html_template = 'index.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
output_pdf = 'Ficha de Reparacion.pdf'

pdfkit.from_string(output_text, output_pdf, configuration=config,options=options,css=rutacss)