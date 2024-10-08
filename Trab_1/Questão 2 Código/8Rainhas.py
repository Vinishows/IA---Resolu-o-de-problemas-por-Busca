import numpy as np
import matplotlib.pyplot as plt
import time

def perturb_parcimonioso(x):
    i, j = np.random.randint(0, 7, size = 2)
    x[i], x[j] = x[j], x[i]
    return x

def F_Apt(posicoes):
    n = len(posicoes)
    ataques = 0
    # Verifica o numero de pares que se atacam
    for i in range(n):
        for j in range(i + 1, n):
        # As rainhas estao na mesma linha ou na diagonal
            if posicoes[i] == posicoes[j] or abs(posicoes[i] - posicoes[j]) == abs(i - j):
                ataques += 1
    return 28 - ataques

def tempera(T: float = 1, max_iters: int = 100) -> np.ndarray:
    i = 0
    T0 = T
    x_otm = np.random.permutation([0,1,2,3,4,5,6,7])
    f_otm = F_Apt(x_otm)

    while i < max_iters:
        if f_otm == 28:
            break

        x_cand = perturb_parcimonioso(x_otm)
        f_cand = F_Apt(x_cand)
        p_ij = np.exp(-(f_otm - f_cand) / T)

        if (f_cand > f_otm) or (p_ij >= np.random.uniform(0,1)):
            
            x_otm = x_cand
            f_otm = f_cand

        #Escalonamento Exponencial
        T = T * .99
        
        #Escalonamento Baseado em Raiz Quadrada
        #T/(1+0.99*np.sqrt(T))
        
        #Escalonamento Linear
        #T - ((T0 - 0.1)/max_iters)

    return x_otm

start_time = time.time()

todas_solucoes = set()
while True:

    if len(todas_solucoes) >= 92:
        break
    solucao = tempera()
    string = "".join([str(digito) for digito in solucao])
    todas_solucoes.add(string)
    
end_time = time.time()
execution_time = end_time - start_time

print(todas_solucoes)
print(f"Tempo total de execução: {execution_time:.4f} segundos")