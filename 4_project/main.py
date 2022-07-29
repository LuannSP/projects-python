"""
    Projeto 4: Ciência de dados - Previsão de Vendas
    
    Passo 1: Entendimento do desafio
    Passo 2: Entendimento da Área/Empresa
    Passo 3: Extração/Obtenção da base de dados
    Passo 4: Ajuste dos dados(Tratamento)
    Passo 5: Ánalise exploratória
    Passo 6: Modelagem + Algoritmos (IA)
    Passo 7: Interpretação dos resultados
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# TV, Jornal e Rádio, estão em milhares de reais
# Vendas estão em milhões
table = pd.read_csv('database//advertising.csv')

# Verificando se tem algum tipo de dado incorreto
# print(table.info())

# Visualizando a correlação em relação a venda
# print(table.corr())

# Criando o gráfico
sns.heatmap(table.corr(), cmap='Wistia', annot=True)

# Exibindo o gráfico
# plt.show()

# IA (Regressão Linear | RandomForest (Árvore de decisão))

# x -> Dado que será usado para previsão (resto da tabela)
# y -> Quem você quer prever (Vendas)

x = table[['TV', 'Radio', 'Jornal']]
y = table['Vendas']

xTraining, xTest, yTraining, yTest = train_test_split(x, y, test_size=0.3)

modelLinearRegression = LinearRegression()
modelRandomForest = RandomForestRegressor()

modelLinearRegression.fit(xTraining, yTraining)
modelRandomForest.fit(xTraining, yTraining)

predictionLinear = modelLinearRegression.predict(xTest)
predictionRandomForest = modelRandomForest.predict(xTest)

# R^2

print(
    r2_score(yTest, predictionLinear),
    r2_score(yTest, predictionRandomForest), sep=' | '
)

# Usando a IA

newTest = pd.read_csv('database//Test.csv')

print(modelRandomForest.predict(newTest))
