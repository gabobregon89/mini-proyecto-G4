import tkinter
from tkinter import messagebox, ttk
import json
import os
from PIL import Image, ImageTk

# Archivos
archivo_sesiones = "sesiones.json"
imagen_fondo = "images/background.jpg"

# Contador de sesiones
contador_sesiones = 0

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

# Guardado de sesión
def guardar_sesion(registro):
    if os.path.exists(archivo_sesiones):
        with open(archivo_sesiones, "r") as f:
            datos = json.load(f)
    else:
        datos = []
    datos.append(registro)
    with open(archivo_sesiones, "w") as f:
        json.dump(datos, f, indent=4)

# Ventana de resultados
def mostrar_resultado(resultado, ventana_anterior):
    ventana_resultado, _ = crear_ventana("Resultado")
    frame = tkinter.Frame(ventana_resultado)
    frame.grid(row=0, column=0, padx=50, pady=20)

    # Mostrar resultados
    for i, (clave, valor) in enumerate(resultado.items()):
        tkinter.Label(frame, text=f"{clave}: {valor}", bg="#f0f0f0", font=("Helvetica", 10)).grid(row=i, column=0, pady=5)

    # Botón exportar
    crear_boton(frame, "Exportar JSON", lambda: exportar_json(resultado)).grid(row=len(resultado), column=0, pady=10)
    # Botón volver al menú
    crear_boton(frame, "Volver al Menú", lambda: [ventana_resultado.destroy(), abrir_menu()]).grid(row=len(resultado)+1, column=0, pady=5)

    ventana_resultado.mainloop()

def exportar_json(registro):
    with open("resultado_exportado.json", "w") as f:
        json.dump(registro, f, indent=4)
    messagebox.showinfo("Exportar", "Resultado exportado a resultado_exportado.json")

# Funciones de cálculo (simuladas, reemplazar con tus funciones reales)
def calcular_densidad(kg_a, kg_b):
    return {"baja": kg_a*0.5, "media": kg_a*0.7, "alta": kg_a*0.9}

def calcular_cantidad_bolsas(kg_a, kg_b):
    return kg_a + kg_b

def calcular_necesidad_producto(cantidad):
    return {"baja": cantidad*1.1, "media": cantidad*1.2, "alta": cantidad*1.3}

# Abrir menú principal
def abrir_menu():
    global contador_sesiones
    ventana_menu, _ = crear_ventana("Menú de cálculo")
    frame = tkinter.Frame(ventana_menu)
    frame.grid(row=0, column=0, padx=50, pady=20)

    # Entradas
    tkinter.Label(frame, text="Producto Kg:", bg="#f0f0f0", font=("Helvetica", 8)).grid(row=0, column=1, sticky="e", pady=5)
    entry_a = tkinter.Entry(frame)
    entry_a.grid(row=0, column=2, pady=5)

    tkinter.Label(frame, text="Tipo de Plástico:", bg="#f0f0f0", font=("Helvetica", 8)).grid(row=1, column=1, sticky="e", pady=5)
    entry_b = tkinter.Entry(frame)
    entry_b.grid(row=1, column=2, pady=5)

    tkinter.Label(frame, text="Cantidad de bolsas:", bg="#f0f0f0", font=("Helvetica", 8)).grid(row=2, column=1, sticky="e", pady=5)
    entry_cant = tkinter.Entry(frame)
    entry_cant.grid(row=2, column=2, pady=5)

    
    
    
    
    # Función para manejar el cálculo y mostrar resultados
    def ejecutar_calculo(tipo):
        global contador_sesiones
        try:
            kg_a = float(entry_a.get())
            kg_b = float(entry_b.get())
            cant = float(entry_cant.get()) if entry_cant.get() else None
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
            return

        contador_sesiones += 1
        sesion = f"Sesion {contador_sesiones}"
        resultado = {}

        if tipo == "densidad":
            dens = calcular_densidad(kg_a, kg_b)
            resultado = {"sesion": sesion, **dens}
        elif tipo == "cantidad":
            cantidad = calcular_cantidad_bolsas(kg_a, kg_b)
            resultado = {"sesion": sesion, "cantidad_bolsas": cantidad}
        elif tipo == "necesidad":
            if not cant:
                messagebox.showerror("Error", "Ingrese la cantidad de bolsas deseada")
                return
            necesidad = calcular_necesidad_producto(cant)
            resultado = {"sesion": sesion, **necesidad}

        # Guardar
        guardar_sesion(resultado)
        ventana_menu.destroy()
        mostrar_resultado(resultado, ventana_menu)

    # Botones
    crear_boton(frame, "Densidad", lambda: ejecutar_calculo("densidad")).grid(row=0, column=0, padx=10, pady=5)
    crear_boton(frame, "Cant. Est. de bolsas", lambda: ejecutar_calculo("cantidad")).grid(row=1, column=0, padx=10, pady=5)
    crear_boton(frame, "Necesidad de productos", lambda: ejecutar_calculo("necesidad")).grid(row=2, column=0, padx=10, pady=5)
    crear_boton(frame, "Cerrar Aplicación", lambda: ventana_menu.destroy()).grid(row=3, column=0, padx=10, pady=5)

    ventana_menu.mainloop()

abrir_menu()
