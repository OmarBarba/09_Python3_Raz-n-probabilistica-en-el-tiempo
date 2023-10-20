# Modelos Ocultos de Markov (HMMs)
import numpy as np

# Definir el modelo HMM
estados = ['S', 'N']
observaciones = ['Alta', 'Media', 'Baja']

# Matriz de transición
transicion = np.array([[0.7, 0.3],
                      [0.4, 0.6]])

# Matriz de emisión
emision = np.array([[0.2, 0.4, 0.4],
                   [0.5, 0.4, 0.1]])

# Distribución inicial
inicial = np.array([0.6, 0.4])

# Secuencia de observaciones (índices de observaciones)
secuencia_observaciones = [1, 0, 2, 1]

# Algoritmo de Viterbi para decodificar la secuencia de estados
def decodificar(secuencia_observaciones):
    longitud = len(secuencia_observaciones)
    tallas = np.zeros((len(estados), longitud))
    caminos = np.zeros((len(estados), longitud), dtype=int)

    # Inicialización
    for i in range(len(estados)):
        tallas[i, 0] = inicial[i] * emision[i, secuencia_observaciones[0]]
        caminos[i, 0] = 0

    # Recursión
    for t in range(1, longitud):
        for j in range(len(estados)):
            maximo = 0
            indice_maximo = 0
            for i in range(len(estados)):
                prob_transicion = tallas[i, t - 1] * transicion[i, j]
                if prob_transicion > maximo:
                    maximo = prob_transicion
                    indice_maximo = i
            tallas[j, t] = maximo * emision[j, secuencia_observaciones[t]]
            caminos[j, t] = indice_maximo

    # Termination step
    estado_final = np.argmax(tallas[:, -1])
    estado_decodificado = [estado_final]

    # Backtrack para encontrar la secuencia de estados
    for t in range(longitud - 1, 0, -1):
        estado_final = caminos[estado_final, t]
        estado_decodificado.insert(0, estado_final)

    return estado_decodificado

# Decodificar la secuencia de observaciones
secuencia_estados = decodificar(secuencia_observaciones)

# Mapear los índices de estados a los nombres reales
estados_decodificados = [estados[i] for i in secuencia_estados]

# Imprimir la secuencia de estados decodificada
print("Secuencia de Estados Decodificada:", estados_decodificados)
