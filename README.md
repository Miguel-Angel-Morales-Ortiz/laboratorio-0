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
    BSA = sqrt((height_cm * weight_kg) / 3600)
\]

Solicita la altura en centímetros y el peso en kilogramos.

###  Salida
Proporciona un único valor numérico: la BSA estimada. No incluye interpretación ni clasificación.


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

---

### 🔹 `BSA_CAT3.py`

Versión más avanzada y completa del script. Incorpora todas las funcionalidades de `BSA_CAT2.py` y añade una característica clínica muy útil: calcula el rango de peso ideal para alcanzar una BSA "normal" (entre 1.5 y 2.0 m²).

#### Funcionalidad
- Incluye todas las funciones de `BSA_CAT2.py`.
- Añade la función `peso_para_bsa`, que calcula el peso necesario para alcanzar un valor de BSA objetivo (entre 1.5 y 2.0 m²), dada una altura.
- Para cada persona, muestra el rango de peso ideal para alcanzar una BSA normal.
- Proporciona retroalimentación clínica sobre cómo el peso actual se compara con un rango saludable.

## 2️⃣ Versiones Modificadas y Expandidas (Generadas por IA)

Las siguientes versiones representan mejoras incrementales sobre el código base, añadiendo funcionalidades clínicas y estadísticas para una evaluación más completa.

---

### 🔹 `AI.py` (Versión 1)

Modificación del código base que introduce una clasificación clínica del valor de BSA.

#### Funcionalidad Añadida
- La función `obtener_clasificacion_bsa` interpreta el valor calculado de la BSA.

####  Clasificación
El resultado se clasifica en cuatro rangos:
- Muy baja
- Baja
- Normal
- Alta

---

### 🔹 `AI2.py` (Versión 2)

Representa una evolución significativa del proyecto, orientada al análisis de datos poblacionales.

####  Capacidad de Procesamiento
- Solicita la cantidad de individuos a evaluar.
- Itera sobre cada uno para calcular su BSA y categoría.

####  Recopilación de Datos
- Almacena los resultados individuales (BSA y categoría) en una lista.

####  Análisis Sumarizado
- Muestra un resumen final con:
  - Resultados individuales.
  - Porcentaje de personas en cada categoría de BSA.

---


```bash
python BSA_CAT2.py
