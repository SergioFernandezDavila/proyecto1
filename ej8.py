import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

datos8 = [
    0.5858, 0.8863, 0.8378, 0.3203, 0.4115, 0.2710, 0.9238, 0.1959, 0.9268, 0.6702, 
    0.6213, 0.4360, 0.6279, 0.8415, 0.5786, 0.0543, 0.3567, 0.1655, 0.3880, 0.8080, 
    0.1931, 0.0843, 0.9152, 0.6093, 0.7587, 0.4515, 0.3203, 0.5139, 0.7070, 0.9123, 
    0.1242, 0.8826, 0.9921, 0.8523, 0.6723, 0.8540, 0.4722, 0.4781, 0.2101, 0.1680, 
    0.8658, 0.4028, 0.6136, 0.8720, 0.1126, 0.5857, 0.9172, 0.8943, 0.8095, 0.6408
]

x = datos8[:-1]
y = datos8[1:]
n_pares = len(x)
m = 3  # rejilla 3x3 = 9 celdas
f_esp = n_pares / (m * m)

H, _, _ = np.histogram2d(x, y, bins=m, range=[[0, 1], [0, 1]])
chi_serie = np.sum((H - f_esp)**2 / f_esp)
critico = stats.chi2.ppf(0.90, df=m*m - 1)

print(f"Chi2 calculado = {chi_serie:.4f} | Crítico (alpha=0.10, df=8) = {critico:.4f}")
print("Independientes?:", chi_serie <= critico)

plt.figure(figsize=(5, 5))
plt.scatter(x, y, color='blue', edgecolors='k')
for l in [1/3, 2/3]:
    plt.axvline(l, color='gray', linestyle='--')
    plt.axhline(l, color='gray', linestyle='--')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title('Prueba de Series (Pares $(u_i, u_{i+1})$)')
plt.show()