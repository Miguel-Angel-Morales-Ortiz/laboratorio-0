import math

def bsa(height_cm, weight_kg):
    """
    BSA = sqrt((height_cm * weight_kg) / 3600)
    """
    return math.sqrt((height_cm * weight_kg) / 3600)

def clasificar_bsa(area):
    if area < 1.5:
        return "BSA baja"
    elif area <= 2.0:
        return "BSA normal"
    else:
        return "BSA alta"

if __name__ == "__main__":
    h = float(input("Altura (cm): "))
    w = float(input("Peso (kg): "))
    area = bsa(h, w)
    clasificacion = clasificar_bsa(area)
    print(f"BSA estimada: {area:.2f} m² ({clasificacion})")