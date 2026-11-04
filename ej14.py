import random
import math
import numpy as np
import matplotlib.pyplot as plt

random.seed(123)
N = 100

# a) Geométrica p = 0.2 (x >= 1)
x_a = [math.ceil(math.log(1.0 - random.random()) / math.log(0.8)) for _ in range(N)]

# b) Geométrica (x >= 0)
x_b = [math.floor(-math.log(1.0 - random.random()) / math.log(2.0)) for _ in range(N)]

# c) p(x) = (20 + 10x)/200
cdf_c = np.cumsum([0.10, 0.15, 0.20, 0.25, 0.30])
x_c = [int(np.searchsorted(cdf_c, random.random())) for _ in range(N)]

# d) p(x) = (18 - 4x)/50
cdf_d = np.cumsum([0.36, 0.28, 0.20, 0.12, 0.04])
x_d = [int(np.searchsorted(cdf_d, random.random())) for _ in range(N)]

# e) p(x) = (3x + 8)/100, x in [2, 6]
valores_e = [2, 3, 4, 5, 6]
cdf_e = np.cumsum([(3*x + 8)/100 for x in valores_e])
x_e = [valores_e[int(np.searchsorted(cdf_e, random.random()))] for _ in range(N)]

# f) Uniforme discreta [6, 11]
x_f = [6 + math.floor(6 * random.random()) for _ in range(N)]

# g) Geométrica truncada (ejemplo: p=0.3, n=10)
p_g, n_g = 0.3, 10
denom_g = 1.0 - (1.0 - p_g)**n_g
x_g = [math.ceil(math.log(1.0 - random.random() * denom_g) / math.log(1.0 - p_g)) for _ in range(N)]

# Gráficas
fig, axs = plt.subplots(2, 4, figsize=(15, 7))
listas = [(x_a, 'a) Geométrica (x>=1)'), (x_b, 'b) Geométrica (x>=0)'),
          (x_c, 'c) Lineal creciente'), (x_d, 'd) Lineal decreciente'),
          (x_e, 'e) Lineal [2, 6]'), (x_f, 'f) Uniforme [6, 11]'),
          (x_g, 'g) Geom. Truncada (n=10)')]

for i, (datos, titulo) in enumerate(listas):
    ax = axs[i // 4, i % 4]
    bins = np.arange(min(datos) - 0.5, max(datos) + 1.5, 1)
    ax.hist(datos, bins=bins, rwidth=0.8, color='steelblue', edgecolor='black')
    ax.set_title(titulo, fontsize=10)
    ax.set_xlabel('Valor de x')
    ax.set_ylabel('Frecuencia')
    ax.grid(axis='y', linestyle='--', alpha=0.5)

axs[1, 3].axis('off')  # Ocultar celda sobrante
plt.tight_layout()
plt.show()