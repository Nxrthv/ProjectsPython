import jinja2
import pdfkit

def creapdf(ruta_index, info, rutacss=''):
    nombre_index = ruta_index.split('/')[-1]
    ruta_index = ruta_index.replace(nombre_index, '')

    env=jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_index))
    index = env.get_template(nombre_index)
    html = index.render(info)

    options = {'page-size': 'letter',
                'margin-top' : '0.05in',
                'margin-bottom': '0.05in',
                'margin-left': '0.05in',
                'margin-right': '0.05in',
                'encoding': 'UTF-8'}
    
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\uninstall.exe')
    ruta_salida = 'C:/Users/Hxruo/OneDrive/Documentos/Python/Boleta.pdf'
    pdfkit.from_string(html, ruta_salida, css=rutacss, options=options, configuration=config)

if __name__ == "__main__":
    ruta_index = 'C:/Users/Hxruo/OneDrive/Documentos/Python/index.html'
    info = {"asunto":input("Describa el problema: ")}
    creapdf(ruta_index, info)