# Mini Proyecto Grupo 4 - Informatorio Etapa 2

Este repositorio contiene el código del mini proyecto realizado, como avance en el cursado de la Etapa 2 del Informatorio.

# Descripción del proyecto:

## Sistema de Cálculo de Densidad de Producto Final (Bolsas Plásticas)

El presente proyecto tiene como objetivo desarrollar un sistema que permita calcular e informar la densidad del producto final, correspondiente a bolsas plásticas producidas a partir de diferentes tipos de materiales.
El sistema recibirá como entrada los datos proporcionados por el usuario, entre los cuales se incluye:
El tipo de plástico utilizado en la producción (por ejemplo: polietileno de baja densidad, polietileno de alta densidad, o polipropileno).

La cantidad de plástico ingresado para el proceso de fabricación.

Con base en estos datos, el sistema realizará el cálculo de la densidad del producto final y, a partir de ella, determinará qué tipo de bolsa plástica puede producir (según tres tipos predefinidos) y la cantidad estimada de unidades resultantes.
En esta primera versión del proyecto, se trabajará con un único tamaño de bolsa, definido previamente, lo que permite simplificar los cálculos y establecer una base sólida para futuras ampliaciones del sistema.
Finalmente, el sistema ofrecerá la posibilidad de emitir un informe en formato PDF, donde se detallará la información del proceso:
* Tipo de plástico utilizado.
* Cantidad de material ingresado.
* Tipo de bolsa que puede producirse.
* Densidad calculada.
* Cantidad estimada de producto final.

Este informe funcionará como un registro completo y descargable del cálculo realizado, permitiendo su almacenamiento, impresión o envío digital.
import tkinter as tk
from tkinter import messagebox

class CalculadoraVolumenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Volumen de Plástico")
        self.root.geometry("400x300")

        # Densidades teóricas (g/cm³)
        self.densidades = {
            "Polietileno Baja Densidad (PEBD)": 0.92,
            "Polietileno Alta Densidad (PEAD)": 0.95
        }

        # Variables
        self.tipo_plastico_var = tk.StringVar(value="Seleccionar Tipo")
        self.masa_total_var = tk.StringVar()

        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="--- Cálculo de Volumen ---", font=("Helvetica", 12, "bold")).pack(pady=10)

        tk.Label(self.root, text="Tipo de plástico:").pack()
        opciones = list(self.densidades.keys())
        tk.OptionMenu(self.root, self.tipo_plastico_var, *opciones).pack(pady=5)

        tk.Label(self.root, text="Cantidad de plástico (kg):").pack()
        tk.Entry(self.root, textvariable=self.masa_total_var).pack(pady=5)

        tk.Button(self.root, text="Calcular Volumen", command=self.calcular_volumen).pack(pady=10)

        self.resultado_label = tk.Label(self.root, text="", font=("Helvetica", 11, "bold"))
        self.resultado_label.pack(pady=10)

    def calcular_volumen(self):
        try:
            tipo = self.tipo_plastico_var.get()
            if tipo == "Seleccionar Tipo":
                messagebox.showwarning("Advertencia", "Seleccione un tipo de plástico.")
                return

            masa_kg = float(self.masa_total_var.get())
            if masa_kg <= 0:
                messagebox.showerror("Error", "La cantidad debe ser positiva.")
                return

            densidad = self.densidades[tipo]
            masa_g = masa_kg * 1000  # Convertir a gramos
            volumen_cm3 = masa_g / densidad

            self.resultado_label.config(
                text=f"Volumen aproximado: {volumen_cm3:,.2f} cm³\n"
                     f"(Usando densidad {densidad} g/cm³)"
            )

        except ValueError:
            messagebox.showerror("Error de entrada", "Ingrese un valor numérico válido para la masa.")

# --- Programa principal ---
if __name__ == "__main__":
    ventana = tk.Tk()
    app = CalculadoraVolumenApp(ventana)
    ventana.mainloop()
    