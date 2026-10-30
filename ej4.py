import random
import math
import matplotlib.pyplot as plt

def generar_datos(n=2000):
    x1, x2, x3 = [], [], []
    for _ in range(n):
        # a) 2 variables uniformes
        v1 = -20 * math.log(random.random() * random.random())
        # b) 4 variables uniformes
        prod_b = random.random() * random.random() * random.random() * random.random()
        v2 = -10 * math.log(prod_b)
        # c) 8 variables uniformes
        prod_c = 1.0
        for _ in range(8):
            prod_c *= random.random()
        v3 = -5 * math.log(prod_c)
        
        x1.append(v1)
        x2.append(v2)
        x3.append(v3)
    return x1, x2, x3

def promedio_movil(serie):
    pm = []
    acumulado = 0.0
    for i, val in enumerate(serie, 1):
        acumulado += val
        pm.append(acumulado / i)
    return pm

x1, x2, x3 = generar_datos(2000)
pm1, pm2, pm3 = promedio_movil(x1), promedio_movil(x2), promedio_movil(x3)

plt.figure(figsize=(10, 5))
plt.plot(pm1, label='a) $x_1 = -20\ln(r_1 r_2)$', alpha=0.8)
plt.plot(pm2, label='b) $x_2 = -10\ln(r_1..r_4)$', alpha=0.8)
plt.plot(pm3, label='c) $x_3 = -5\ln(r_1..r_8)$', alpha=0.8)
plt.axhline(40, color='red', linestyle='--', label='Convergencia teórica (40)')
plt.xlabel('Mantenimientos realizados')
plt.ylabel('Promedio móvil del tiempo')
plt.title('Estabilización de tiempos de reparación')
plt.legend()
plt.grid(True)
plt.show()