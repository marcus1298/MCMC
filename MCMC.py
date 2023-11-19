import pandas as pd
from numpy.random import random, choice
import numpy as np

# Leitura do CSV
file_path = 'C:/Users/marco/Documents/2023-1/OSIM/Tarefa7-MMC/USD_BRL Historical Data.csv'
data = pd.read_csv(file_path)

# Definição dos estados
estados = [
    'baixa agressiva',
    'baixa',
    'mantém',
    'alta',
    'alta agressiva',
]

# Função para obter o índice de um estado
def index(estado):
    return estados.index(estado)

# Inicialização da matriz de probabilidades de transição
probs = np.zeros(shape=[len(estados)]*2)

# Definição das probabilidades (ajuste conforme sua análise)
probs[index('baixa agressiva'), index('baixa agressiva')] = 0.85
probs[index('baixa agressiva'), index('baixa')] = 0.01
probs[index('baixa agressiva'), index('mantém')] = 0.14
probs[index('baixa'), index('baixa agressiva')] = 0.15
probs[index('baixa'), index('baixa')] = 0.45
probs[index('baixa'), index('mantém')] = 0.4
probs[index('mantém'), index('baixa agressiva')] = 0.35
probs[index('mantém'), index('baixa')] = 0.25
probs[index('mantém'), index('mantém')] = 0.4
probs[index('alta'), index('alta agressiva')] = 0.35
probs[index('alta'), index('alta')] = 0.25
probs[index('alta'), index('mantém')] = 0.4
probs[index('alta agressiva'), index('alta agressiva')] = 0.85
probs[index('alta agressiva'), index('alta')] = 0.01
probs[index('alta agressiva'), index('mantém')] = 0.14

# Definição do número de dias
N = 5

# Simulação
situacao = list()
for _ in range(10000):
    estado = 'mantém'  # estado inicial
    aolongododia = [estado]
    for _ in range(N):
        estado = choice(estados, p=probs[index(estado), :])
        aolongododia.append(estado)
    if aolongododia.count('baixa') == 0 and aolongododia.count('baixa agressiva') == 0:
        situacao.append(True)
    else:
        situacao.append(False)

print("Último dia simulado:")
for i, e in enumerate(aolongododia):
    print(f"{i+1}º dia -> {e}")

print(f"Probabilidade de 5 dias sem baixa: {situacao.count(True)/len(situacao)*100:.02f}%")

# A probabilidade é sempre menor que 2%
