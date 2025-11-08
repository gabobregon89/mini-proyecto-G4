from formula_produccion import Produccion
from formula_densidad import CalculadoraVolumen

# Este archivo solo para probar por separado la clase Produccion

def main():
    print("Cálculo de producción de bolsas plásticas")
    
    try:
        kilos_plastico = float(input("Ingrese la cantidad de kilos de plástico disponibles: "))
        tipo_plastico = input("Ingrese el tipo de plastico (LDPE, LLDPE, HDPE, PP, PET, PVC): ").strip().upper()

        if tipo_plastico not in ["LDPE", "LLDPE", "HDPE", "PP", "PET", "PVC"]:
            print("Tipo de plástico inválido. Por favor ingrese alguno de los valores antes mencionados.")
            return

        densidad = CalculadoraVolumen(tipo_plastico, kilos_plastico)
        densidad_final = densidad.clasificar_densidad()

        print(f"Densidad final clasificada como: {densidad_final}")        

        # Calcular y mostrar el número de bolsas producidas
        produccion = Produccion(kilos_plastico, densidad_final)
        numero_bolsas = produccion.calcular_bolsas()

        print(f"Número de bolsas producidas: {numero_bolsas}")

    except ValueError:
        print("Entrada inválida. Por favor ingrese un número válido para los kilos de plástico.")

if __name__ == "__main__":
    main()