import numpy as np
import matplotlib.pyplot as plt

# Modelo simple de movimiento lineal
def movimiento_lineal(posicion_anterior, velocidad, ruido_proceso):
    nueva_posicion = posicion_anterior + velocidad + np.random.normal(0, ruido_proceso)
    return nueva_posicion

# Parámetros del modelo
velocidad_real = 1.0
ruido_proceso = 0.1
ruido_medida = 0.2

# Número de pasos de tiempo
n_pasos = 50

# Simulación del movimiento y mediciones
posiciones_reales = []
mediciones = []

posicion_actual = 0
for _ in range(n_pasos):
    # Realizar el movimiento
    posicion_actual = movimiento_lineal(posicion_actual, velocidad_real, ruido_proceso)
    posiciones_reales.append(posicion_actual)
    
    # Simular la medición con ruido
    medicion = posicion_actual + np.random.normal(0, ruido_medida)
    mediciones.append(medicion)

# Filtrado: Estimar la posición actual en función de todas las mediciones hasta ahora
posiciones_filtradas = []
posicion_estimada = 0
for medicion in mediciones:
    # Usar una estimación bayesiana simple
    posicion_estimada = (posicion_estimada + medicion) / 2
    posiciones_filtradas.append(posicion_estimada)

# Predicción: Estimar la posición futura en función de la última estimación
n_pasos_prediccion = 10
posiciones_predichas = []
for _ in range(n_pasos_prediccion):
    posicion_estimada = movimiento_lineal(posicion_estimada, velocidad_real, ruido_proceso)
    posiciones_predichas.append(posicion_estimada)

# Ajustar la longitud de posiciones_predichas para que coincida con n_pasos
posiciones_predichas.extend([None] * (n_pasos - n_pasos_prediccion))

# Suavizado: Estimar la posición pasada en función de todas las mediciones y predicciones
posiciones_suavizadas = []

for t in range(n_pasos):
    suma_posiciones = sum([p for p in posiciones_predichas[:t + 1] if p is not None])
    estimacion_suavizada = suma_posiciones / (t + 1) if suma_posiciones != 0 else 0
    posiciones_suavizadas.append(estimacion_suavizada)


# Explicación: Comparar las mediciones con las estimaciones
plt.plot(range(n_pasos), posiciones_reales, label="Posición Real", linestyle="--")
plt.plot(range(n_pasos), mediciones, label="Mediciones", marker="o")
plt.plot(range(n_pasos), posiciones_filtradas, label="Filtrado", marker="x")
plt.plot(range(n_pasos), posiciones_predichas, label="Predicción", linestyle="--", marker="s")
plt.plot(range(n_pasos), posiciones_suavizadas, label="Suavizado", marker="v")
plt.legend()
plt.title("Filtrado, Predicción, Suavizado y Explicación")
plt.xlabel("Tiempo")
plt.ylabel("Posición")
plt.show()
