import random
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 1. Generación de 100 números en [0, 1)
random.seed(42)
u = [random.random() for _ in range(100)]
n = len(u)

# --- PRUEBAS ESTADÍSTICAS ---
# Media
media = np.mean(u)
z0 = (media - 0.5) * np.sqrt(12 * n)
pasa_media = abs(z0) <= 1.96

# Varianza
s2 = np.var(u, ddof=1)
chi_var = (n - 1) * s2 * 12
lim_inf = stats.chi2.ppf(0.025, df=n-1)
lim_sup = stats.chi2.ppf(0.975, df=n-1)
pasa_var = lim_inf <= chi_var <= lim_sup

# Uniformidad
k = 10
obs_u, bordes = np.histogram(u, bins=k, range=(0, 1))
chi_unif = np.sum((obs_u - 10)**2 / 10)
crit_unif = stats.chi2.ppf(0.95, df=k-1)
pasa_unif = chi_unif <= crit_unif

# Independencia (Series)
x_par, y_par = u[:-1], u[1:]
H, _, _ = np.histogram2d(x_par, y_par, bins=3, range=[[0, 1], [0, 1]])
chi_ind = np.sum((H - 11)**2 / 11)
crit_ind = stats.chi2.ppf(0.95, df=8)
pasa_ind = chi_ind <= crit_ind

print(f"Media = {media:.4f} | Z0 = {z0:.3f} | Pasa: {pasa_media}")
print(f"Varianza = {s2:.4f} | Chi2 = {chi_var:.3f} en [{lim_inf:.2f}, {lim_sup:.2f}] | Pasa: {pasa_var}")
print(f"Uniformidad Chi2 = {chi_unif:.3f} <= {crit_unif:.3f} | Pasa: {pasa_unif}")
print(f"Independencia Chi2 = {chi_ind:.3f} <= {crit_ind:.3f} | Pasa: {pasa_ind}")

# --- GRÁFICAS ---
plt.figure(figsize=(11, 4))

plt.subplot(1, 2, 1)
plt.hist(u, bins=10, range=(0, 1), edgecolor='black', color='skyblue')
plt.axhline(10, color='red', linestyle='--', label='Esperado (10)')
plt.title('Uniformidad (10 clases)')
plt.xlabel('Intervalo')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.scatter(x_par, y_par, color='darkblue', edgecolors='k', alpha=0.7)
for line in [1/3, 2/3]:
    plt.axvline(line, color='gray', linestyle=':')
    plt.axhline(line, color='gray', linestyle=':')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title('Independencia: Pares $(u_i, u_{i+1})$')
plt.xlabel('$u_i$')
plt.ylabel('$u_{i+1}$')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()