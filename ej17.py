import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

demandas = [0, 1, 2, 3, 4, 5, 6]
probabilidades = [0.10, 0.15, 0.25, 0.20, 0.15, 0.08, 0.07]
n_horas = 100
n_replicas = 5

plt.figure(figsize=(10, 5))
promedios_finales = []

for replica in range(n_replicas):
    d = np.random.choice(demandas, size=n_horas, p=probabilidades)
    utilidad = d * (6.0 - 3.5)
    prom_movil = np.cumsum(utilidad) / np.arange(1, n_horas + 1)
    promedios_finales.append(prom_movil[-1])
    plt.plot(prom_movil, label=f'Corrida {replica + 1}')

plt.axhline(np.dot(demandas, probabilidades) * 2.5, color='black', linestyle='--', label='Esperanza matemática ($6.125)')
plt.xlabel('Hora')
plt.ylabel('Utilidad promedio acumulada ($/hr)')
plt.title('Gráfica de estabilización de la utilidad (5 réplicas)')
plt.legend()
plt.grid(True)
plt.show()

# Intervalo global de las 5 réplicas
media_global = np.mean(promedios_finales)
s_global = np.std(promedios_finales, ddof=1)
h = stats.t.ppf(0.975, df=n_replicas-1) * (s_global / np.sqrt(n_replicas))
print(f"IC 95% Global: [{media_global - h:.3f}, {media_global + h:.3f}] $/hora")