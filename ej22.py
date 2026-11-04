import numpy as np
import scipy.stats as stats

demandas = [
    99, 94, 80, 73, 86, 95, 90, 70, 92, 83, 89, 93, 62, 94, 86, 62, 77, 72, 63, 88, 96,
    99, 98, 77, 96, 74, 86, 81, 94, 81, 70, 98, 78, 86, 74, 94, 95, 77, 79, 89, 65, 94,
    88, 72, 71, 70, 76, 95, 92, 96, 93, 72, 97, 75, 97, 72, 76, 69, 61, 69, 99, 83, 83,
    61, 64, 95, 80, 70, 79, 65, 80, 85, 72, 68, 83, 78, 84, 64, 72, 67, 94, 100, 78, 93,
    66, 99, 97, 74, 93, 95, 70, 93, 64, 86, 72, 80, 83, 65, 66, 96, 95, 84, 88, 68, 65,
    70, 88, 90, 85, 92, 81, 68, 92, 64, 84, 69, 73, 71, 98, 66, 68, 74, 93, 94, 86, 69,
    82, 71, 79, 100, 84, 65, 99, 100, 61, 78, 73, 80, 72, 100, 100, 98, 82, 60, 93, 75,
    84, 75, 76, 71, 94, 74, 84, 72, 71, 71, 85, 69, 88, 97, 93, 63, 91, 89, 89, 99, 93,
    62, 99, 77, 69, 82, 66, 91, 73, 88, 61, 63, 67, 76, 100, 93, 82, 72, 75, 92, 87, 74,
    60, 93, 77, 60, 84, 64, 83, 75, 68, 64, 97, 78
]

inspecciones = [
    4, 2, 3, 0, 0, 2, 4, 1, 2, 0, 2, 2, 3, 3, 2, 1, 1, 1, 4, 2, 1, 0, 3, 1, 2,
    3, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 0, 0, 2, 1, 1, 1, 3, 1, 0, 3, 0, 1, 0, 1,
    2, 0, 1, 2, 0, 1, 2, 1, 3, 1, 2, 1, 1, 2, 1, 1, 1, 1, 3, 1, 0, 0, 1, 1, 2,
    0, 0, 0, 1, 0, 2, 0, 2, 1, 2, 0, 1, 1, 2, 0, 1, 2, 1, 2, 3, 0, 0, 0, 2, 2
]

politicas = [60, 70, 80, 90, 100]
dias_sim = 1000

for Q in politicas:
    costos = []
    inv = 0
    for _ in range(dias_sim):
        dem = np.random.choice(demandas)
        # 1. Defectuosos en fábrica (3%)
        def_fabrica = np.random.binomial(Q, 0.03)
        q_buenos = Q - def_fabrica
        c_rechazo = def_fabrica * 90.0
        
        # 2. Balance de inventario
        disp = inv + q_buenos
        if disp >= dem:
            inv = disp - dem
            c_inv = inv * 20.0
            c_falt = 0.0
        else:
            c_falt = (dem - disp) * 40.0
            inv = 0
            c_inv = 0.0
            
        # 3. Proceso de inspección del cliente
        n_insp = np.random.choice(inspecciones)
        def_cliente = np.random.binomial(n_insp, 0.05)
        c_cliente = def_cliente * 120.0
        
        costo_total_dia = c_rechazo + c_inv + c_falt + c_cliente
        costos.append(costo_total_dia)
        
    m_costo = np.mean(costos)
    s_costo = np.std(costos, ddof=1)
    ic = stats.t.ppf(0.975, df=dias_sim-1) * (s_costo / np.sqrt(dias_sim))
    print(f"Política Q = {Q:3d} | Costo Medio Diario: ${m_costo:7.2f} +- ${ic:.2f}")