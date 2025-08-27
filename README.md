# Laboratorio 0, Analizador de Superficie Corporal (BSA)
Este repositorio contiene una serie de scripts en Python para calcular y clasificar la Superficie Corporal (BSA) de las personas utilizando la **fórmula de Mosteller**.

Cada archivo representa una versión mejorada, añadiendo nuevas funcionalidades que van desde el cálculo simple para una persona hasta el análisis de múltiples individuos con rangos de peso recomendados.

---

### **`bsa_cat.py`**
El script más básico de la colección. Diseñado para un solo uso, calcula la BSA y clasifica el resultado.

**Características:**
* Calcula la BSA para **una sola persona**.
* Clasifica la BSA en: `BSA baja`, `BSA normal`, o `BSA alta`.
* Requiere que el usuario ingrese la altura (cm) y el peso (kg).

**Uso:**
```bash
python bsa_cat.py
