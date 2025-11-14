from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import os

class GeneradorPDF:
    def __init__(self, carpeta_destino, tipo_plastico, kilos_plastico, densidad_final, numero_bolsas, nombre_base="Reporte Sistema de Gestion de Densidad"):
        self.carpeta_destino = carpeta_destino
        self.nombre_base = nombre_base
        self.tipo_plastico = tipo_plastico
        self.kilos_plastico = kilos_plastico
        self.densidad_final = densidad_final
        self.numero_bolsas = numero_bolsas

        # 🎨 Estilos y elementos
        self.estilos = getSampleStyleSheet()
        self.elementos = []

    def agregar_titulo(self, texto):
        """Agrega un título grande al PDF"""
        estilo = self.estilos['Heading1']
        estilo.textColor = colors.darkgreen
        self.elementos.append(Paragraph(texto, estilo))
        self.elementos.append(Spacer(1, 12))

        imagen = Image("./images/fondo_reporte.jpg", width=150, height=100)
        imagen.hAlign = 'CENTER'  # Centra la imagen horizontalmente
        self.elementos.append(imagen)
        self.elementos.append(Spacer(1, 12))  # Agrega un pequeño espacio debajo

    def agregar_parrafo(self, fecha):
        """Agrega un párrafo al PDF"""
        estilo = self.estilos['Normal']

        # Armar el texto combinando los 4 parámetros
        texto = (
            f"<b>Tipo de Plastico:</b> {self.tipo_plastico}<br/>"
            f"<b>Cantidad ingresada (en kg):</b> {self.kilos_plastico}<br/>"
            f"<b>Densidad final de las bolsas:</b> {self.densidad_final}<br/>"
            f"<b>Produccion de bolsas (en unidades):</b> {self.numero_bolsas}"
        )

        self.elementos.append(Paragraph(texto, estilo))
        self.elementos.append(Spacer(1, 8))

        registro_fecha = (f"<b>Fecha de generación:</b> {fecha}")
        self.elementos.append(Paragraph(registro_fecha, estilo))
        self.elementos.append(Spacer(1, 8))

    def agregar_tabla(self, datos, encabezados=None):
        """Agrega una tabla con estilo básico"""
        if encabezados:
            datos = [encabezados] + datos

        tabla = Table(datos, colWidths=[6*cm, 6*cm])
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.lightgreen),
            ('TEXTCOLOR', (0,0), (-1,0), colors.black),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.gray),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ]))
        self.elementos.append(tabla)
        self.elementos.append(Spacer(1, 12))


    def guardar_pdf(self, ruta_destino):
        """Guarda el PDF en la ruta indicada por el usuario"""
        # Une la ruta destino con el nombre del archivo (si self.nombre_archivo es solo el nombre)
        fecha = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
        
        ruta_pdf = os.path.join(ruta_destino, f"{self.nombre_base}_{fecha}.pdf")

        # Crear el documento PDF
        doc = SimpleDocTemplate(ruta_pdf, pagesize=A4)
        doc.build(self.elementos)

        # Obtener ruta absoluta para mostrar en consola
        ruta_absoluta = os.path.abspath(ruta_pdf)
        print(f"PDF generado correctamente en:\n{ruta_absoluta}")

    def generarPDF(self):

        self.agregar_titulo(self.nombre_base)
        fecha = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        self.agregar_parrafo(fecha)

        """Método para generar el PDF completo"""
        self.guardar_pdf(self.carpeta_destino)
