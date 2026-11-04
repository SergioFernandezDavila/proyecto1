import numpy as np
import scipy.stats as stats

precios = [125.50, 132.75, 120.80, 138.20, 127.50]
n = len(precios)
media = np.mean(precios)
s = np.std(precios, ddof=1)

# a) Exactitud lograda (h) al 95%
t_val = stats.t.ppf(0.975, df=n-1)
exactitud = t_val * (s / np.sqrt(n))
print(f"a) Media = {media:.2f}, s = {s:.2f}")
print(f"   Exactitud actual (+- h): +- {exactitud:.2f} USD")

# b) Réplicas para error e = +-0.35 con 90% de confianza
z = stats.norm.ppf(0.95)
n_requerido = (z * s / 0.35)**2
print(f"b) Réplicas necesarias: {int(np.ceil(n_requerido))} réplicas")