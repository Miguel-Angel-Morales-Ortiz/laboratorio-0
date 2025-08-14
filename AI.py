import math

def calcular_bsa(peso, altura):
    """
    Calcula la superficie corporal (BSA) usando la fórmula de Mosteller.
    """
    return math.sqrt((altura * peso) / 3600)

def obtener_clasificacion_bsa(bsa):
    """
    Devuelve la clasificación clínica de la BSA.
    """
    if bsa < 1.4:
        return "Muy baja"
    elif bsa < 1.7:
        return "Baja"
    elif bsa < 2.1:
        return "Normal"
    else:
        return "Alta"

def main():
    print("Calculadora de Superficie Corporal (BSA)")
    altura = float(input("Ingrese su altura en centímetros: "))
    peso = float(input("Ingrese su peso en kilogramos: "))
    resultado_bsa = calcular_bsa(peso, altura)
    categoria = obtener_clasificacion_bsa(resultado_bsa)
    print(f"\nSu BSA es: {resultado_bsa:.2f} m²")
    print(f"Clasificación clínica: {categoria}")

if __name__ == "__main__":
    main()