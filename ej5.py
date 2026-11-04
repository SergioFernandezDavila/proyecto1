def ciclo_congruencial(a, c, m, x0):
    historial = {}
    x = x0
    paso = 0
    while x not in historial:
        historial[x] = paso
        x = (a * x + c) % m
        paso += 1
    return paso - historial[x]

# a) x_{i+1} = (21*x_i + 15) mod 31, x0 = 21
print("Ciclo 5a:", ciclo_congruencial(21, 15, 31, 21))

# b) x_{i+1} = (13*x_i + 9) mod 128, x0 = 7
print("Ciclo 5b:", ciclo_congruencial(13, 9, 128, 7))

# c) x_{i+1} = (17*x_i) mod 31, x0 = 23
print("Ciclo 5c:", ciclo_congruencial(17, 0, 31, 23))

# d) x_{i+1} = (x_i + 121) mod 256, x0 = 17
print("Ciclo 5d:", ciclo_congruencial(1, 121, 256, 17))

# e) x_{i+1} = (21*x_i + 15*x_{i-1}) mod 64, x0 = 21, x1 = 43
def ciclo_segundo_orden():
    visto = {}
    x_prev, x_act = 21, 43
    paso = 0
    while (x_prev, x_act) not in visto:
        visto[(x_prev, x_act)] = paso
        x_sig = (21 * x_act + 15 * x_prev) % 64
        x_prev, x_act = x_act, x_sig
        paso += 1
    return paso - visto[(x_prev, x_act)]

print("Ciclo 5e:", ciclo_segundo_orden())