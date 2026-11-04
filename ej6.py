import numpy as np
import scipy.stats as stats

# a) Periodo
a, c, m, x0 = 121, 553, 177, 23
numeros = []
x = x0
while True:
    x = (a * x + c) % m
    u = x / m
    if u in numeros:
        break
    numeros.append(u)

n = len(numeros)
print(f"Periodo de vida: {n}")

# b) Pruebas estadísticas (alpha = 0.05)
media = np.mean(numeros)
z0 = (media - 0.5) * np.sqrt(12 * n)
print(f"Media: {media:.4f} | Z0 = {z0:.4f} (Acepta si |Z0| <= 1.96): {abs(z0) <= 1.96}")

s2 = np.var(numeros, ddof=1)
chi_var = (n - 1) * s2 * 12
chi_inf = stats.chi2.ppf(0.025, df=n-1)
chi_sup = stats.chi2.ppf(0.975, df=n-1)
print(f"Varianza: {s2:.4f} | Chi2_0 = {chi_var:.4f} in [{chi_inf:.2f}, {chi_sup:.2f}]: {chi_inf <= chi_var <= chi_sup}")

# Uniformidad (5 clases)
k = 5
f_obs, _ = np.histogram(numeros, bins=k, range=(0, 1))
f_esp = n / k
chi_unif = np.sum((f_obs - f_esp)**2 / f_esp)
crit_unif = stats.chi2.ppf(0.95, df=k-1)
print(f"Chi2_unif = {chi_unif:.4f} <= {crit_unif:.4f}: {chi_unif <= crit_unif}")