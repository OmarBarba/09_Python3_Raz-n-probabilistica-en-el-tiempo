import numpy as np
import matplotlib.pyplot as plt

# Generar una serie temporal estacionaria
np.random.seed(0)
media = 0
desviacion_estandar = 1
serie_temporal = np.random.normal(media, desviacion_estandar, 100)

# Graficar la serie temporal
plt.plot(serie_temporal)
plt.title("Serie Temporal Estacionaria")
plt.show()
