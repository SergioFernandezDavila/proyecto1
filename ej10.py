import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

datos10 = [
    17.392, 4.078, 3.151, 3.528, 2.440, 5.924, 3.461, 2.052, 10.369, 3.690, 10.870, 4.793, 2.498, 0.569,
    8.281, 0.154, 5.959, 3.384, 12.877, 13.602, 5.244, 16.677, 5.977, 4.313, 4.767, 2.381, 6.443, 1.392,
    1.578, 8.115, 4.891, 6.720, 7.728, 2.717, 10.451, 5.901, 0.818, 7.088, 2.637, 4.714, 3.032, 1.495,
    15.733, 7.768, 2.333, 7.822, 3.708, 6.412, 1.290, 3.957, 5.285, 7.094, 3.078, 1.264, 2.630, 10.177,
    2.155, 2.945, 7.552, 11.094, 4.772, 7.281, 14.344, 19.867, 0.119, 2.072, 1.486, 3.791, 4.214, 1.611,
    1.781, 1.530, 3.280, 4.301, 0.202, 7.489, 1.422, 1.453, 0.022, 6.001, 9.269, 8.477, 3.043, 0.877,
    6.966, 2.103, 1.816, 0.433, 2.547, 0.843, 1.182, 8.121, 2.007, 1.395, 4.661, 7.378, 5.300, 17.066, 12.171
]
n = len(datos10)

# Ajuste Gamma (loc fijo en 0)
a_fit, loc_fit, scale_fit = stats.gamma.fit(datos10, floc=0)
dist = stats.gamma(a_fit, loc=0, scale=scale_fit)

# Clases equiprobables para asegurar E_i >= 5
k_clases = 8
cuantiles = [dist.ppf(i / k_clases) for i in range(k_clases + 1)]
cuantiles[0] = 0.0
cuantiles[-1] = np.inf

obs, _ = np.histogram(datos10, bins=cuantiles)
esp = np.full(k_clases, n / k_clases)

chi_0 = np.sum((obs - esp)**2 / esp)
df = k_clases - 1 - 2  # 2 parámetros: a y scale
critico = stats.chi2.ppf(0.90, df=df)

print(f"Parámetros Gamma: alpha = {a_fit:.3f}, beta = {scale_fit:.3f}")
print(f"Chi2 calculado = {chi_0:.4f} | Chi2 crítico (0.10, df={df}) = {critico:.4f}")
print("¿Ajusta a la distribución Gamma al 90%?:", chi_0 <= critico)

# Gráfica
plt.figure(figsize=(7, 4))
plt.hist(datos10, bins=12, density=True, alpha=0.6, color='seagreen', edgecolor='black', label='Datos observados')
x_vals = np.linspace(0, max(datos10), 200)
plt.plot(x_vals, dist.pdf(x_vals), 'r-', lw=2, label=f'Gamma Ajustada (a={a_fit:.2f})')
plt.title('Ejercicio 10: Ajuste de Distribución Gamma')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()