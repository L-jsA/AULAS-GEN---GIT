import numpy as np # NumPy serve para fazer cálculos numéricos de forma rápida, eficiente e simples em Python.
vendas = np.array([20, 25, 19, 28, 23, 30 ]) # Cria um array NumPy contendo os valores de vendas.
media = np.mean(vendas) # np.mean() é exatamente a função que calcula a média (média aritmética) de um conjunto de valores no NumPy.
# Calcula a média de um conjunto de dados

desvio = np.std(vendas) #np.std() calcula exatamente o desvio padrão de um conjunto de dados no NumPy.
print(media)
print(desvio)

# OBS: O std já calcula a média internamente para poder calcular o desvio padrão, nào é obrigatório usar o mean antes