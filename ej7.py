import numpy as np
import scipy.stats as stats

datos7 = [
    0.8797, 0.9848, 0.4557, 0.9170, 0.8376, 0.3884, 0.3469, 0.1592, 0.2204, 0.6235, 
    0.6289, 0.7977, 0.8536, 0.5991, 0.3681, 0.8750, 0.5844, 0.8846, 0.5461, 0.2088, 
    0.5999, 0.8147, 0.3410, 0.5739, 0.8589, 0.9996, 0.6431, 0.1492, 0.3254, 0.1525, 
    0.2006, 0.7387, 0.8681, 0.0856, 0.4720, 0.2415, 0.5613, 0.5291, 0.2258, 0.4272, 
    0.3808, 0.0318, 0.3188, 0.4603, 0.6360, 0.9606, 0.7401, 0.5992, 0.5027, 0.0954
]
n = len(datos7)
media = np.mean(datos7)
var = np.var(datos7, ddof=1)

# 1. Media
z0 = (media - 0.5) * np.sqrt(12 * n)
# 2. Varianza
chi_var = (n - 1) * var * 12
c_inf = stats.chi2.ppf(0.025, df=n-1)
c_sup = stats.chi2.ppf(0.975, df=n-1)
# 3. Uniformidad (5 clases)
k = 5
f_obs, _ = np.histogram(datos7, bins=k, range=(0, 1))
f_esp = n / k
chi_u = np.sum((f_obs - f_esp)**2 / f_esp)
c_unif = stats.chi2.ppf(0.95, df=k-1)

print(f"Media = {media:.4f} | Z0 = {z0:.4f} (|Z0| <= 1.96? {abs(z0) <= 1.96})")
print(f"Varianza = {var:.4f} | Chi2 = {chi_var:.4f} in [{c_inf:.2f}, {c_sup:.2f}]? {c_inf <= chi_var <= c_sup}")
print(f"Uniformidad Chi2 = {chi_u:.4f} <= {c_unif:.4f}? {chi_u <= c_unif}")