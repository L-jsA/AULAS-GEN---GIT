# Importar as bibliotecas para o sistema
# Biblioteca de inteligência artificial

from sklearn.linear_model import LinearRegression # É a importação do modelo LinearRegression, usado para criar e treinar modelos de regressão linear no scikit-learn.
# Regressão linear é um método de machine learning que encontra uma linha (ou equação) capaz de prever um valor numérico com base em uma ou mais variáveis
# A inteligência artificial em geral não trabalha sozinha
# Ela depende de ferramentas para tratar os dados

import pandas as pd
# Pandas para ler os daods

import matplotlib.pyplot as plt
# Para mostrar dados

# Entrada de dados - ler os dados 
# Processamento de dados - interpretar eles
# Saída de dados - rxibição das informações

# 1 - LER 
#OBS: Se no meu modelo de IA tiver dados com dualidades, minhas respostas serão imprecisas 
df_dados = pd.read_csv("dados.csv")
print(df_dados) # exibi tudo
print(df_dados.head()) # exibi 5 linhas

# 2 - PROCESSAR OS DADOS
# Var independente - causa, fator, informação usada para prever
x_independente = df_dados[["horas_estudo"]]
# Var dependentes - consequência, resultado, o que você quer prever
y_dependente = df_dados[["nota"]]

# 2.1 - CRIAR UM MODELO DE REGRESSÃO LINEAR
modelo = LinearRegression()

# 2.2 - TREINAR O MODELO
modelo.fit(x_independente, y_dependente)

# 2.3 EXIBIR OS DADOS
print("coeficiente", modelo.coef_[0])
print("interceptação", modelo.intercept_) # onde os pontos se encontram

# 3 SAÍDA DE DADOS
# 3.1 - O que eu quero prever?
nova_hora = [[9]] # anota o que quer prever

# Vou prever
prever = modelo.predict(nova_hora)
# Mostrar a previsão
print("Se você estudaar", nova_hora, "sua nota vai ser de", prever)

# SEMPRE A REGRESSÃO LINEAR, OU SEJA, A PREVISÃO DEVE TER DOIS GRÁFICOS EM UM
# SENDO ELES O GRÁFICO DE DISPERSÁO COM O GRÁFIO DE LINHA

plt.plot(df_dados["horas_estudo"], modelo.predict(x_independente))
plt.scatter(df_dados["horas_estudo"], df_dados["nota"])

plt.show()



