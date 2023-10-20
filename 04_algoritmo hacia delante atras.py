import numpy as np

# Definir el modelo HMM
# - Estados: S1, S2
# - Observaciones: O1, O2, O3
# - Matriz de transición
# - Matriz de emisión
# - Distribución inicial
num_estados = 2
num_observaciones = 3

# Matriz de transición
transicion = np.array([[0.7, 0.3],
                      [0.4, 0.6]])

# Matriz de emisión
emision = np.array([[0.1, 0.4, 0.5],
                   [0.7, 0.2, 0.1]])

# Distribución inicial
inicial = np.array([0.6, 0.4])

# Observaciones (secuencia de índices)
observaciones = [0, 1, 2]

# Algoritmo hacia adelante
forward = np.zeros((num_estados, len(observaciones)))
for t in range(len(observaciones)):
    if t == 0:
        forward[:, t] = inicial * emision[:, observaciones[t]]
    else:
        for j in range(num_estados):
            forward[j, t] = sum(forward[i, t - 1] * transicion[i, j] * emision[j, observaciones[t]] for i in range(num_estados))

# Algoritmo hacia atrás
backward = np.zeros((num_estados, len(observaciones)))
for t in range(len(observaciones) - 1, -1, -1):
    if t == len(observaciones) - 1:
        backward[:, t] = 1
    else:
        for i in range(num_estados):
            backward[i, t] = sum(transicion[i, j] * emision[j, observaciones[t + 1]] * backward[j, t + 1] for j in range(num_estados))

# Calcular la probabilidad de la secuencia de observaciones
probabilidad = sum(inicial[i] * emision[i, observaciones[0]] * backward[i, 0] for i in range(num_estados))

print("Probabilidad de la secuencia de observaciones:", probabilidad)
