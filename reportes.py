from flask import Flask, render_template, Response
import pymysql
import pandas as pd
from xlsxwriter import Workbook
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Conexión a la base de datos MySQL
conn = pymysql.connect(host='localhost', user='root', password='', db='senasoft')
cursor = conn.cursor()

# Consulta SQL para obtener datos de la tabla
consulta_sql = "SELECT * FROM establecimientos"

# Ejecutar la consulta
cursor.execute(consulta_sql)

# Obtener los resultados en un DataFrame de pandas
df = pd.read_sql(consulta_sql, conn)

# Cerrar la conexión a la base de datos
conn.close()

# Generar archivo Excel
excel_file = "establecimientos_reporte.xlsx"
writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Establecimientos', index=False)

# Añadir formato al archivo Excel (opcional)
workbook = writer.book
worksheet = writer.sheets['Establecimientos']
formato = workbook.add_format({'text_wrap': True})
worksheet.set_column('B:D', 20, formato)

# Guardar el archivo Excel
writer.close()

# Generar archivo PDF
pdf_file = "establecimientos_reporte.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)
tabla = Table([df.columns] + df.values.tolist())
tabla.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0, 0.7, 0.7)),
                           ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),
                           ('GRID', (0, 0), (-1, -1), 0.5, (0, 0, 0, 0.5))]))
doc.build([tabla])





app = Flask(__name__)

@app.route('/')
def index():
    # Lee el archivo Excel generado previamente
    excel_file = "establecimientos_reporte.xlsx"
    df = pd.read_excel(excel_file, sheet_name='Establecimientos')

    # Convierte el DataFrame a formato HTML
    table_html = df.to_html(classes="table table-striped")

    return render_template('reportes.html', table=table_html)

@app.route('/descargar_excel')
def descargar_excel():
    # Nombre del archivo Excel
    excel_file = "establecimientos_reporte.xlsx"

    # Configura la respuesta para enviar el archivo Excel como una descarga
    response = Response(open(excel_file, 'rb').read())
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = 'attachment; filename=establecimientos_reporte.xlsx'

    return response

if __name__ == '__main__':
    app.run(debug=True)