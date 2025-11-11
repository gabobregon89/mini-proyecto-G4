from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import os

class GeneradorPDF:
  def __init__(self, nombre_base="mini_proyecto_G4"):
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.nombre_archivo = f"{nombre_base}_{fecha_actual}.pdf"
        self.estilos = getSampleStyleSheet()
        self.elementos = []


def  agregar_titulo(self, texto):
        """Agrega un título grande al PDF"""
        estilo = self.estilos['Heading1']
        estilo.textColor = colors.darkgreen
        self.elementos.append(Paragraph(texto, estilo))
        self.elementos.append(Spacer(1, 12))

def agregar_parrafo(self, texto):
        """Agrega un párrafo al PDF"""
        estilo = self.estilos['Normal']
        self.elementos.append(Paragraph(texto, estilo))
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

def guardar_pdf(self):
        """Guarda el PDF con todos los elementos agregados"""
        doc = SimpleDocTemplate(self.nombre_archivo, pagesize=A4)
        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self.agregar_parrafo(f"<b>Fecha de generación:</b> {fecha}")
        doc.build(self.elementos)

        ruta_absoluta = os.path.abspath(self.nombre_archivo)
        print(f"✅ PDF generado correctamente en:\n{ruta_absoluta} - generadorenpdf.py:54")

# 🧾 Bloque principal: se ejecuta solo si abrís el script directamente
if __name__ == "__main__":
    pdf = GeneradorPDF()
    pdf.agregar_titulo("📊 Reporte de Volumen")
    pdf.agregar_parrafo("Este documento fue generado automáticamente con ReportLab.")
    pdf.agregar_tabla(
        datos=[[10, 20], [30, 40], [50, 60]],
        encabezados=["Columna A", "Columna B"]
    )
    pdf.guardar_pdf()
