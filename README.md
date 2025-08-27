# Laboratorio 0, Analizador de Superficie Corporal (BSA)
Este repositorio contiene una serie de scripts en Python para calcular y clasificar la Superficie Corporal (BSA) de las personas utilizando la **fórmula de Mosteller**.

Cada archivo representa una versión mejorada, añadiendo nuevas funcionalidades que van desde el cálculo simple para una persona hasta el análisis de múltiples individuos con rangos de peso recomendados.

## Código Base: `bsa.py`

Este archivo constituye el punto de partida del proyecto. Su funcionalidad es simple y directa: calcular la BSA de un único individuo.

### Objetivo Principal
Determinar el valor numérico de la BSA para una persona.

### Método
Utiliza la fórmula de Mosteller:

\[
\text{BSA} = \sqrt{\frac{\text{altura (cm)} \times \text{peso (kg)}}{3600}}
\]

Solicita la altura en centímetros y el peso en kilogramos.

### 📤 Salida
Proporciona un único valor numérico: la BSA estimada. No incluye interpretación ni clasificación.

---

---

### **`bsa_cat.py`**
El script más básico de la colección. Diseñado para un solo uso, calcula la BSA y clasifica el resultado.

**Características:**
* Calcula la BSA para **una sola persona**.
* Clasifica la BSA en: `BSA baja`, `BSA normal`, o `BSA alta`.
* Requiere que el usuario ingrese la altura (cm) y el peso (kg).

---

### `BSA_CAT2.py`

Versión mejorada que permite procesar datos de un grupo de personas. Además de los cálculos individuales, mantiene un conteo y presenta un resumen de los resultados de todo el grupo.

#### Funcionalidad
- Solicita el número de personas a evaluar.
- En un bucle, pide la altura y el peso de cada persona.
- Almacena los resultados individuales en una lista.
- Mantiene un contador por categoría de BSA.
- Al finalizar, muestra un resumen con los resultados individuales y el porcentaje total por categoría.

### 🔹 `BSA_CAT3.py`

Versión más avanzada y completa del script. Incorpora todas las funcionalidades de `BSA_CAT2.py` y añade una característica clínica muy útil: calcula el rango de peso ideal para alcanzar una BSA "normal" (entre 1.5 y 2.0 m²).

#### Funcionalidad
- Incluye todas las funciones de `BSA_CAT2.py`.
- Añade la función `peso_para_bsa`, que calcula el peso necesario para alcanzar un valor de BSA objetivo (entre 1.5 y 2.0 m²), dada una altura.
- Para cada persona, muestra el rango de peso ideal para alcanzar una BSA normal.
- Proporciona retroalimentación clínica sobre cómo el peso actual se compara con un rango saludable.



```bash
python BSA_CAT2.py
