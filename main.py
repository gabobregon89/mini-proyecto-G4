from formula_produccion import Produccion

# Este archivo solo para probar por separado la clase Produccion

def main():
    print("Cálculo de producción de bolsas plásticas")
    
    try:
        kilos_plastico = float(input("Ingrese la cantidad de kilos de plástico disponibles: "))
        tipo_densidad = input("Ingrese el tipo de densidad (BD, MD, AD): ").strip().upper()

        if tipo_densidad not in ["BD", "MD", "AD"]:
            print("Tipo de densidad inválido. Por favor ingrese BD, MD o AD.")
            return

        produccion = Produccion(kilos_plastico, tipo_densidad)
        numero_bolsas = produccion.calcular_bolsas()

        print(f"Número de bolsas producidas: {numero_bolsas}")

    except ValueError:
        print("Entrada inválida. Por favor ingrese un número válido para los kilos de plástico.")

if __name__ == "__main__":
    main()