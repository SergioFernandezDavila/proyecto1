import numpy as np

np.random.seed(42)
n_barras = 300
x1 = np.random.normal(loc=30.0, scale=0.9, size=n_barras)
x2 = np.random.gamma(shape=10, scale=1.45, size=n_barras)
longitud = x1 + x2

fuera_espec = np.mean((longitud < 40) | (longitud > 50))
mu_est = np.mean(longitud)
sigma_est = np.std(longitud, ddof=1)

cp = (50 - 40) / (6 * sigma_est)
cpk = min((50 - mu_est) / (3 * sigma_est), (mu_est - 40) / (3 * sigma_est))

print(f"Probabilidad fuera de especificación: {fuera_espec * 100:.2f}%")
print(f"Cp  = {cp:.3f}")
print(f"Cpk = {cpk:.3f}")