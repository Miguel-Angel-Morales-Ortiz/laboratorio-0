import math

def calcular_bsa(altura_cm, peso_kg):
    """Calcula la superficie corporal usando la fórmula de Mosteller."""
    return math.sqrt((altura_cm * peso_kg) / 3600)

def clasificar_bsa(bsa):
    """Clasifica la BSA en baja, normal o alta según rangos clínicos."""
    if bsa < 1.5:
        return "BSA baja"
    elif bsa <= 2.0:
        return "BSA normal"
    else:
        return "BSA alta"

def main():
    print("Calculadora de Superficie Corporal (BSA) para varias personas")
    n = int(input("¿Cuántas personas desea procesar?: "))
    resumen = {"BSA baja": 0, "BSA normal": 0, "BSA alta": 0}
    resultados = []

    for idx in range(1, n + 1):
        print(f"\nPersona {idx}:")
        altura = float(input("  Altura (cm): "))
        peso = float(input("  Peso (kg): "))
        bsa = calcular_bsa(altura, peso)
        categoria = clasificar_bsa(bsa)
        resumen[categoria] += 1
        resultados.append((idx, bsa, categoria))

    print("\nResultados individuales:")
    for persona, bsa, categoria in resultados:
        print(f"Persona {persona}: BSA={bsa:.2f} m² ({categoria})")

    print("\nPorcentaje por categoría:")
    for cat, cantidad in resumen.items():
        porcentaje = (cantidad / n) * 100
        print(f"{cat}: {porcentaje:.1f}%")

if __name__ == "__main__":
    main()