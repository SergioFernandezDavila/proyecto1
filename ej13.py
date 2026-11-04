import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 1. Datos del histograma
intervalos_etiquetas = ['0-2', '2-4', '4-6', '6-8', '8-10', '10-12', '12-14', '14-16', '16-18', '18-20', '20-22']
obs = np.array([39, 57, 47, 23, 18, 9, 2, 3, 1, 1, 0])
limites = np.arange(0, 24, 2)
mids = (limites[:-1] + limites[1:]) / 2.0
N = np.sum(obs)

# 2. Estimación de parámetros de la distribución Gamma
media = np.sum(obs * mids) / N
var = np.sum(obs * (mids - media)**2) / (N - 1)
a_param = media**2 / var
escala_param = var / media

dist_gamma = stats.gamma(a=a_param, scale=escala_param)

# 3. Frecuencias esperadas
prob_clases = np.diff(dist_gamma.cdf(limites))
prob_clases[-1] += 1.0 - dist_gamma.cdf(limites[-1])
esp = N * prob_clases

# 4. Agrupamiento para clases con E_i >= 5
o_agrup, e_agrup = [], []
o_temp, e_temp = 0, 0
for o_i, e_i in zip(obs, esp):
    o_temp += o_i
    e_temp += e_i
    if e_temp >= 5:
        o_agrup.append(o_temp)
        e_agrup.append(e_temp)
        o_temp, e_temp = 0, 0
if e_temp > 0:
    o_agrup[-1] += o_temp
    e_agrup[-1] += e_temp

o_agrup = np.array(o_agrup)
e_agrup = np.array(e_agrup)

# 5. Estadístico Chi-cuadrada
chi2_calc = np.sum((o_agrup - e_agrup)**2 / e_agrup)
df = len(o_agrup) - 1 - 2  # 2 parámetros estimados
chi2_crit = stats.chi2.ppf(0.90, df=df)
p_valor = 1 - stats.chi2.cdf(chi2_calc, df=df)

print(f"Parámetros Gamma: alpha = {a_param:.3f}, beta = {escala_param:.3f}")
print(f"Chi2 calculado = {chi2_calc:.4f}")
print(f"Chi2 crítico (0.10, df={df}) = {chi2_crit:.4f}")
print(f"P-valor = {p_valor:.4f}")
print(f"¿Ajusta a la distribución Gamma?: {chi2_calc <= chi2_crit}")

# 6. Gráfica comparativa
plt.figure(figsize=(10, 5))
x_pos = np.arange(len(obs))

plt.bar(x_pos - 0.2, obs, width=0.4, color='skyblue', edgecolor='black', label='Observado ($O_i$)')
plt.bar(x_pos + 0.2, esp, width=0.4, color='salmon', edgecolor='black', label='Esperado Gamma')

plt.xticks(x_pos, intervalos_etiquetas, rotation=45)
plt.xlabel('Intervalos')
plt.ylabel('Frecuencia')
plt.title(f'Ejercicio 13: Prueba Chi-cuadrada (Distribución Gamma, $\\chi^2={chi2_calc:.2f} < {chi2_crit:.2f}$)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()