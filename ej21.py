import numpy as np

dias = 300
prod_diaria = []
util_diaria = []

for _ in range(dias):
    if np.random.random() < 0.80:
        # Ocurre falla
        tipo = np.random.choice(['L', 'M', 'G', 'F'], p=[10/85, 15/85, 25/85, 35/85])
        if tipo == 'L':
            t_rep = np.random.gamma(shape=4, scale=1.0)
        elif tipo == 'M':
            t_rep = max(0, np.random.normal(3.5, 1.1))
        elif tipo == 'G':
            # f(t) = t - 6 en [6, 6 + sqrt(2)] => F(t) = (t-6)^2 / 2 => t = 6 + sqrt(2*R)
            t_rep = 6.0 + np.sqrt(2.0 * np.random.random())
        else: # F
            t_rep = np.random.exponential(1.0 / 0.2)
            
        t_rep = min(t_rep, 24.0)
    else:
        t_rep = 0.0
        
    piezas = 1000.0 * (1.0 - t_rep / 24.0)
    utilidad = piezas * 100.0 - t_rep * 11.0
    
    prod_diaria.append(piezas)
    util_diaria.append(utilidad)

print(f"Producción promedio diaria: {np.mean(prod_diaria):.2f} piezas/día")
print(f"Utilidad promedio diaria: ${np.mean(util_diaria):.2f}/día")