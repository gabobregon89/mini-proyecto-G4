class Produccion:
    def __init__(self, kilos_plastico, tipo_densidad):
        self.kilos_plastico = kilos_plastico
        self.tipo_densidad = tipo_densidad
    
    # Espesores en micrones(µm) según el tipo de densidad
    espesor = {
        "BD": 15,
        "MD": 30,
        "AD": 50
    }

    # Densidades finales en g/cm³ según el tipo de densidad
    densidad_final = {
        "BD": 0.92,
        "MD": 1,
        "AD": 1.20
    }

    # Dimensiones de la bolsa en cm
    ancho = 50
    alto = 70

    # Método para calcular la masa por bolsa en kg
    def masa_por_bolsa(self):
        area_bolsa = self.ancho * self.alto  # Área en c²
        espesor = self.espesor[self.tipo_densidad] / 10000  # Convertir micras a cm

        masa_bolsa = self.densidad_final[self.tipo_densidad] * area_bolsa * espesor  # Masa en g
        masa_bolsa_kg = masa_bolsa / 1000  # Convertir a kg

        return masa_bolsa_kg
    
    # Método para calcular el número de bolsas producidas
    def calcular_bolsas(self):
        masa_bolsa_kg = self.masa_por_bolsa()
        numero_bolsas = self.kilos_plastico / masa_bolsa_kg

        return int(numero_bolsas)

