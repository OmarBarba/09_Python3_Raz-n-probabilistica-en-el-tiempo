import random

# Función para simular un lanzamiento de moneda
def lanzamiento_de_moneda():
    return random.choice(["cara", "cruz"])

# Número de lanzamientos
n_lanzamientos = 1000

# Simulación de lanzamientos y cálculo de la probabilidad en el tiempo
contador_caras = 0
probabilidad_en_el_tiempo = []

for _ in range(n_lanzamientos):
    resultado = lanzamiento_de_moneda()
    if resultado == "cara":
        contador_caras += 1
    probabilidad = contador_caras / (n_lanzamientos - 1)  # Se excluye el lanzamiento actual
    probabilidad_en_el_tiempo.append(probabilidad)

# Imprimir las probabilidades en el tiempo
print("Probabilidad de caer cara en el tiempo:")
for t, prob in enumerate(probabilidad_en_el_tiempo):
    print(f"Lanzamiento {t + 1}: {prob:.4f}")
