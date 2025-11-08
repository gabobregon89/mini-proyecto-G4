class CalculadoraVolumen:
    def __init__(self, tipo_plastico, cantidad_kilos):
        self.tipo_plastico = tipo_plastico
        self.cantidad_kilos = cantidad_kilos

    # Densidades base (g/cm³)
    densidades = {
        "LDPE": 0.92,
        "LLDPE": 0.93,
        "HDPE": 0.96,
        "PP": 0.91,
        "PET": 1.38,
        "PVC": 1.35
    }

    # Combinaciones permitidas por tipo de bolsa
    tipos_bolsa = {
        "baja": ["LDPE", "LLDPE"],
        "media": ["LDPE", "HDPE", "PP"],
        "alta": ["HDPE", "PET"]
    }

    # Rangos de densidad para clasificación
    tipos_densidad = {
        "BD": [0.90, 0.94],
        "MD": [0.95, 1.10],
        "AD": [1.20, 1.40]
    }

    # Calcula densidad final en g/cm³
    def calcular_densidad(self):

        densidad = self.densidades[self.tipo_plastico]
        masa_g = self.cantidad_kilos * 1000  # Convertir a gramos
        volumen_cm3 = masa_g / densidad

        densidad_final = masa_g / volumen_cm3

        return densidad_final

    # Clasifica la densidad en BD, MD o AD
    def clasificar_densidad(self):
        densidad = self.calcular_densidad()
        rangos = self.tipos_densidad.items()

        for tipo, (min_d, max_d) in rangos:
            if min_d <= densidad <= max_d:
                return tipo
            return "Fuera de rango"