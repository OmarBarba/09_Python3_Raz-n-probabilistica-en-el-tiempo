import numpy as np

# Parámetros del sistema
# Modelo de estado: [posición, velocidad]
A = np.array([[1, 1],
              [0, 1]])  # Matriz de transición del estado
H = np.array([[1, 0]])  # Matriz de observación (medida)
Q = np.array([[0.1, 0],
              [0, 0.01]])  # Covarianza del proceso
R = np.array([[1]])  # Covarianza de la medida

# Estimación inicial
x = np.array([[0],
              [0]])  # [posición inicial, velocidad inicial]
P = np.array([[1, 0],
              [0, 1]])  # Covarianza inicial

# Simulación de observaciones ruidosas
num_pasos = 50
verdadera_posicion = np.linspace(0, 5, num_pasos)
observaciones = verdadera_posicion + np.random.normal(0, 0.5, num_pasos)  # Observaciones ruidosas

# Filtro de Kalman
posiciones_estimadas = []

for z in observaciones:
    # Predicción
    x = np.dot(A, x)
    P = np.dot(np.dot(A, P), A.T) + Q

    # Actualización (corrección) basada en la observación
    K = np.dot(np.dot(P, H.T), np.linalg.inv(np.dot(np.dot(H, P), H.T) + R))
    x = x + np.dot(K, (z - np.dot(H, x)))
    P = P - np.dot(np.dot(K, H), P)

    # Estimar la posición y agregarla a la lista de estimaciones
    posicion_estimada = x[0, 0]
    posiciones_estimadas.append(posicion_estimada)

# Imprimir las estimaciones
print("Estimaciones de Posición:", posiciones_estimadas)
