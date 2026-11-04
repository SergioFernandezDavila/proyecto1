import numpy as np
import matplotlib.pyplot as plt

N = 10000
R = np.random.uniform(0, 1, N)

# Fórmulas de la transformada inversa
x_15a = np.sqrt(-10.0 * np.log(1.0 - R))
x_15b = (-np.log(1.0 - R) / 12.0)**(1.0 / 3.0)
x_15c = (-np.log(1.0 - R))**(1.0 / 4.0)

fig, axs = plt.subplots(1, 3, figsize=(14, 4))

# 15a
axs[0].hist(x_15a, bins=40, density=True, color='skyblue', edgecolor='black', alpha=0.6, label='Simulado')
t1 = np.linspace(0, 7, 200)
axs[0].plot(t1, (t1 / 5.0) * np.exp(-t1**2 / 10.0), 'r-', lw=2, label='Teórica $f(x)$')
axs[0].set_title('15a) $x = \sqrt{-10\ln(1-R)}$')
axs[0].legend()

# 15b
axs[1].hist(x_15b, bins=40, density=True, color='salmon', edgecolor='black', alpha=0.6, label='Simulado')
t2 = np.linspace(0, 0.8, 200)
axs[1].plot(t2, 36.0 * t2**2 * np.exp(-12.0 * t2**3), 'b-', lw=2, label='Teórica $f(x)$')
axs[1].set_title('15b) $x = \sqrt[3]{-\ln(1-R)/12}$')
axs[1].legend()

# 15c
axs[2].hist(x_15c, bins=40, density=True, color='lightgreen', edgecolor='black', alpha=0.6, label='Simulado')
t3 = np.linspace(0, 1.8, 200)
axs[2].plot(t3, 4.0 * t3**3 * np.exp(-t3**4), 'm-', lw=2, label='Teórica $f(x)$')
axs[2].set_title('15c) $x = \sqrt[4]{-\ln(1-R)}$')
axs[2].legend()

for ax in axs:
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('Densidad')

plt.tight_layout()
plt.show()