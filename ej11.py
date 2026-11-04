import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

datos11 = [
    12.561, 2.695, 12.082, 10.335, 13.260, 2.549, 4.594, 2.500, 24.930, 7.805, 8.322, 7.422, 11.143, 20.599,
    7.508, 4.367, 1.544, 3.706, 8.185, 14.405, 4.057, 15.584, 9.049, 6.265, 10.663, 10.257, 11.475, 4.688,
    16.256, 4.688, 11.963, 5.599, 19.204, 1.784, 25.998, 12.299, 10.317, 3.779, 18.993, 7.419, 15.154,
    9.579, 8.423, 6.934, 2.005, 13.234, 5.542, 5.271, 12.831, 8.231, 15.330, 7.958, 7.103, 16.134, 0.189,
    10.165, 14.624, 15.696, 10.212, 0.891, 3.186, 9.051, 11.118, 4.449, 17.901, 15.497, 6.645, 5.078,
    11.555, 3.724, 21.500, 7.160, 13.528, 3.372, 15.334, 7.603, 31.066, 1.992, 21.127, 10.784, 3.643,
    27.334, 3.178, 1.313, 10.962, 6.936, 3.140, 16.877, 19.171, 6.620, 3.775, 16.675, 1.368, 17.583, 1.669,
    11.157, 16.432, 2.831, 7.844, 10.745
]
n = len(datos11)

# Ajuste Weibull mínimo (floc=0)
c_fit, loc_fit, scale_fit = stats.weibull_min.fit(datos11, floc=0)
dist_w = stats.weibull_min(c_fit, loc=0, scale=scale_fit)

# Clases equiprobables
k_clases = 10
cuantiles = [dist_w.ppf(i / k_clases) for i in range(k_clases + 1)]
cuantiles[0] = 0.0
cuantiles[-1] = np.inf

obs, _ = np.histogram(datos11, bins=cuantiles)
esp = np.full(k_clases, n / k_clases)

chi_0 = np.sum((obs - esp)**2 / esp)
df = k_clases - 1 - 2  # 2 parámetros estimados
critico = stats.chi2.ppf(0.95, df=df)

print(f"Parámetros Weibull: c = {c_fit:.3f}, escala = {scale_fit:.3f}")
print(f"Chi2 calculado = {chi_0:.4f} | Chi2 crítico (0.05, df={df}) = {critico:.4f}")
print("¿Ajusta a la distribución Weibull al 95%?:", chi_0 <= critico)

# Gráfica
plt.figure(figsize=(7, 4))
plt.hist(datos11, bins=14, density=True, alpha=0.6, color='coral', edgecolor='black', label='Datos observados')
x_vals = np.linspace(0, max(datos11), 200)
plt.plot(x_vals, dist_w.pdf(x_vals), 'b-', lw=2, label=f'Weibull Ajustada (c={c_fit:.2f})')
plt.title('Ejercicio 11: Ajuste de Distribución Weibull')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()