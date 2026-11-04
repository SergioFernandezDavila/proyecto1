import numpy as np
import matplotlib.pyplot as plt

N = 10000
R = np.random.uniform(0, 1, N)

# 16a: x = (28*R - 1)**(1/3) - 1  (manejo de signo para raíz cúbica)
arg_a = 28.0 * R - 1.0
x_16a = np.sign(arg_a) * (np.abs(arg_a)**(1.0 / 3.0)) - 1.0

# 16b: x = 9 + 3*sqrt(R)
x_16b = 9.0 + 3.0 * np.sqrt(R)

# 16c: x = 8 - 3*sqrt(1 - R)
x_16c = 8.0 - 3.0 * np.sqrt(1.0 - R)

# 16d: x = 15 - 4*sqrt(1 - R)
x_16d = 15.0 - 4.0 * np.sqrt(1.0 - R)

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# 16a
axs[0, 0].hist(x_16a, bins=35, density=True, color='lightblue', edgecolor='black', alpha=0.6, label='Simulado')
t1 = np.linspace(-2, 2, 200)
axs[0, 0].plot(t1, (3.0 / 28.0) * (t1 + 1)**2, 'r-', lw=2, label='Teórica $f(x)$')
axs[0, 0].set_title('16a) $x = \sqrt[3]{28R - 1} - 1$')
axs[0, 0].legend()

# 16b
axs[0, 1].hist(x_16b, bins=35, density=True, color='lightgreen', edgecolor='black', alpha=0.6, label='Simulado')
t2 = np.linspace(9, 12, 200)
axs[0, 1].plot(t2, (2.0 / 9.0) * (t2 - 9), 'r-', lw=2, label='Teórica $f(x)$')
axs[0, 1].set_title('16b) $x = 9 + 3\sqrt{R}$')
axs[0, 1].legend()

# 16c
axs[1, 0].hist(x_16c, bins=35, density=True, color='wheat', edgecolor='black', alpha=0.6, label='Simulado')
t3 = np.linspace(5, 8, 200)
axs[1, 0].plot(t3, (2.0 / 9.0) * (8 - t3), 'r-', lw=2, label='Teórica $f(x)$')
axs[1, 0].set_title('16c) $x = 8 - 3\sqrt{1-R}$')
axs[1, 0].legend()

# 16d
axs[1, 1].hist(x_16d, bins=35, density=True, color='thistle', edgecolor='black', alpha=0.6, label='Simulado')
t4 = np.linspace(11, 15, 200)
axs[1, 1].plot(t4, (1.0 / 8.0) * (15 - t4), 'r-', lw=2, label='Teórica $f(x)$')
axs[1, 1].set_title('16d) $x = 15 - 4\sqrt{1-R}$')
axs[1, 1].legend()

for row in axs:
    for ax in row:
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.set_xlabel('x')
        ax.set_ylabel('Densidad')

plt.tight_layout()
plt.show()