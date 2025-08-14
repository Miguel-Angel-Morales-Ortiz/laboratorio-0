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
    npersonas= int(input("ingrese el numero de personas: "))
    resultados = []
    conteo = {"BSA baja": 0, "BSA normal": 0, "BSA alta": 0}
    for i in range(npersonas):
        print(f"\nPersona {i+1}:")
        h = float(input("Altura (cm): "))
        w = float(input("Peso (kg): "))
        area = bsa(h, w)
        clasificacion = clasificar_bsa(area)
        conteo[clasificacion] += 1
        resultados.append({
            "persona": i+1,
            "altura": h,
            "peso": w,
            "bsa": area,
            "clasificacion": clasificacion
        })

    print("\nResultados finales:")
    for r in resultados:
        print(f"Persona {r['persona']}: BSA={r['bsa']:.2f} m² ({r['clasificacion']})")
    print("\nPorcentaje de personas en cada categoría:")
    for categoria, cantidad in conteo.items():
        porcentaje = (cantidad / npersonas) * 100
        print(f"{categoria}: {porcentaje:.1f}%")