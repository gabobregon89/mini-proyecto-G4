import tkinter
from tkinter import messagebox, ttk
import json
import os
from PIL import Image, ImageTk
from formula_densidad import CalculadoraVolumen  # Importamos la clase del otro archivo
from formula_produccion import Produccion 
from generador_pdf import GeneradorPDF
from tkinter import Tk, filedialog




imagen_fondo = "images/background.jpg"


# Estilo de botones
button_style = {
    'bg': '#4CAF50',
    'fg': 'white',
    'font': ('Helvetica', 12),
    'activebackground': '#45a049',
    'relief': 'raised'
}

# Funciones auxiliares
def cargar_fondo(ventana, canvas):
    try:
        img = Image.open(imagen_fondo).resize((ventana.winfo_width(), ventana.winfo_height()), Image.LANCZOS)
        imagen_cargada = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=imagen_cargada)
        canvas.image = imagen_cargada
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {str(e)}")

def crear_ventana(titulo, ancho=800, alto=500):
    ventana = tkinter.Tk()
    ventana.title(titulo)
    x_pos = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y_pos = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x_pos}+{y_pos}")
    ventana.minsize(ancho, alto)
    ventana.resizable(False, False)
    ventana.config(bg="#f0f0f0")
    canvas = tkinter.Canvas(ventana, width=ancho, height=alto, bg="#f0f0f0", highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="nsew")
    cargar_fondo(ventana, canvas)
    ventana.bind("<Configure>", lambda event: cargar_fondo(ventana, canvas))
    return ventana, canvas

def crear_boton(frame, texto, comando):
    boton = tkinter.Button(frame, text=texto, command=comando, width=20, **button_style)
    boton.bind("<Enter>", lambda e: boton.config(bg="#45a049"))
    boton.bind("<Leave>", lambda e: boton.config(bg="#4CAF50"))
    return boton
##########

def calcular(entrada_kilos, tipo_de_plastico):
        try:
            kilos = float(entrada_kilos.get())
            plastico = tipo_de_plastico.get()

            v = CalculadoraVolumen(plastico, kilos)
            densidad = v.calcular_densidad()
            clasificacion = v.clasificar_densidad()
            
            messagebox.showinfo(
                "Resultado",
                f"Tipo de plástico: {plastico}\n"
                f"Cantidad: {kilos} kg\n"
                f"Densidad calculada: {densidad:.3f} g/cm³\n"
                f"Clasificación: {clasificacion}"
            )

            #entrada_kilos.delete(0, tkinter.END)  # Borra el contenido del entry
            #tipo_de_plastico.current(0)  # Vuelve al valor por defecto (LDPE)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido para los kilogramos.")

def calcular_produccion(entrada_kilos, tipo_de_plastico):
        try:
            kilos = float(entrada_kilos.get())
            plastico = tipo_de_plastico.get()

            v = CalculadoraVolumen(plastico, kilos)
            densidad = v.clasificar_densidad()
            n = Produccion(kilos, densidad)
            masa=n.masa_por_bolsa()
            q_bolsas=n.calcular_bolsas()   

            messagebox.showinfo(
                "Resultado",
                f"Tipo de plástico: {plastico}\n"
                f"Cantidad: {kilos} kg\n"
                f"Densidad calculada: {densidad:.3f} g/cm³\n"
                f"Masa por Bolsa: {masa:.3f} Kg\n"
                f"Cantidad de bolsas a producir: {q_bolsas:} Unidades\n"
            )

            #entrada_kilos.delete(0, tkinter.END)  # Borra el contenido del entry
            #tipo_de_plastico.current(0)  # Vuelve al valor por defecto (LDPE)

        except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido para los kilogramos.")

def Generar_PDF(entrada_kilos, tipo_de_plastico): #self, carpeta_destino, tipo_plastico, kilos_plastico, densidad_final, numero_bolsas, nombre_base="Reporte Sistema de Gestion de Densidad"
        root = Tk()
        root.withdraw()
        try:
            kilos = float(entrada_kilos.get())
            plastico = tipo_de_plastico.get()
            destino = filedialog.askdirectory(title="Seleccione carpeta destino del PDF")
            if not destino:
                return  # Usuario canceló

            nombre_base="Reporte Sistema de Gestion de Densidad"
            v = CalculadoraVolumen(plastico, kilos)
            densidad = v.clasificar_densidad()
            n = Produccion(kilos, densidad)
            q_bolsas=n.calcular_bolsas()   

            pdf=GeneradorPDF(destino, plastico, kilos, densidad, q_bolsas,nombre_base)  
            pdf.generarPDF()
            
            entrada_kilos.delete(0, tkinter.END)  # Borra el contenido del entry
            tipo_de_plastico.current(0)  # Vuelve al valor por defecto (LDPE)
        
        except ValueError:
               messagebox.showerror("Error", "Ingrese un numero")


def abrir_menu():
    global contador_sesiones
    ventana_menu, _ = crear_ventana("Menú de cálculo")
    frame = tkinter.Frame(ventana_menu)
    frame.grid(row=0, column=0, padx=50, pady=20)

    # Entradas
    tkinter.Label(frame, text="Producto Kg:", bg="#f0f0f0", font=("Helvetica", 8)).grid(row=0, column=0, sticky="e", pady=5)
    entrada_kilos = tkinter.Entry(frame)
    entrada_kilos.grid(row=0, column=1, pady=5)

    # Un desplegable  para seleccionar el tipo de plastico
    tkinter.Label(frame, text="Tipo de Plástico:", bg="#f0f0f0", font=("Helvetica", 8)).grid(row=1, column=0, sticky="e", pady=5)

    materiales = ["LDPE", "LLDPE", "HDPE", "PP", "PET", "PVC"]
    tipo_de_plastico = ttk.Combobox(frame, values=materiales, state="readonly")
    tipo_de_plastico.current(0)  # Valor por defecto
    tipo_de_plastico.grid(row=1, column=1, pady=5)


  
    


 # Botones
    crear_boton(frame, "Calcular Densidad", lambda: calcular(entrada_kilos, tipo_de_plastico)).grid(row=0, column=2, padx=10, pady=5)
    crear_boton(frame, "Calcular Producción", lambda: calcular_produccion(entrada_kilos, tipo_de_plastico)).grid(row=1, column=2, padx=10, pady=5)
    crear_boton(frame, "Generar Reporte", lambda: Generar_PDF(entrada_kilos, tipo_de_plastico)).grid(row=2, column=2, padx=10, pady=5)
    crear_boton(frame, "Cerrar Aplicación", lambda: ventana_menu.destroy()).grid(row=3, column=2, padx=10, pady=5)

    ventana_menu.mainloop()

abrir_menu()