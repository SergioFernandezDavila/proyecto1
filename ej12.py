import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

intervalos = ['150-151', '151-152', '152-153', '153-154', '154-155', 
              '155-156', '156-157', '157-158', '158-159', '159-160']
obs = np.array([13, 8, 11, 15, 7, 8, 9, 11, 10, 8])
n = np.sum(obs)
k = len(obs)

# Frecuencia esperada
esp = np.full(k, n / k)

# Chi-cuadrada
chi_0 = np.sum((obs - esp)**2 / esp)
critico = stats.chi2.ppf(0.95, df=k-1)
p_valor = 1 - stats.chi2.cdf(chi_0, df=k-1)

print(f"Chi2 calculado = {chi_0:.4f}")
print(f"Chi2 crítico (alpha=0.05, df=9) = {critico:.4f}")
print(f"P-valor = {p_valor:.4f}")
print("¿Se acepta la distribución Uniforme?:", chi_0 < critico)

# Gráfica
plt.figure(figsize=(9, 4.5))
x_pos = np.arange(k)
plt.bar(x_pos, obs, color='lightblue', edgecolor='black', label='Observado ($O_i$)')
plt.axhline(10, color='red', linestyle='--', linewidth=2, label='Esperado Uniforme ($E_i = 10$)')

plt.xticks(x_pos, intervalos, rotation=45)
plt.ylim(0, 18)
plt.title('Ejercicio 12: Prueba de Bondad de Ajuste Uniforme $U(150, 160)$')
plt.xlabel('Intervalos')
plt.ylabel('Frecuencia')
for i, v in enumerate(obs):
    plt.text(i, v + 0.3, str(v), ha='center', fontweight='bold')
plt.legend()
plt.tight_layout()
plt.grid(axis='y', alpha=0.3)
plt.show()