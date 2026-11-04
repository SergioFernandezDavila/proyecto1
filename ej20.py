import numpy as np

def simular_dia_banco(duracion_min=480):
    t = 0
    t_llegadas = []
    while t < duracion_min:
        t += np.random.exponential(4.0)
        if t < duracion_min:
            t_llegadas.append(t)
            
    n_clientes = len(t_llegadas)
    if n_clientes == 0:
        return 0.0
        
    num_tx = np.random.choice([1, 2, 3, 4], size=n_clientes, p=[0.4, 0.3, 0.2, 0.1])
    tiempos_servicio = [np.sum(np.random.exponential(2.2, size=tx)) for tx in num_tx]
    
    t_inicio_serv = 0.0
    tiempos_espera = []
    for arr, serv in zip(t_llegadas, tiempos_servicio):
        t_inicio_serv = max(arr, t_inicio_serv)
        tiempos_espera.append(t_inicio_serv - arr)
        t_inicio_serv += serv
        
    return np.mean(tiempos_espera)

esperas_300 = [simular_dia_banco() for _ in range(300)]
print(f"Tiempo promedio en fila: {np.mean(esperas_300):.2f} minutos")