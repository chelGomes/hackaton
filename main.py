import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

dados = pd.read_csv('daily-minimum-temperatures.csv')
print(dados.describe())
dados['Daily minimum temperatures'] = dados['Daily minimum temperatures'].astype(float)
T = dados['Daily minimum temperatures'].values
plt.plot(T)
plt.show()
dados['Date'] = pd.to_datetime(dados['Date'], format='%m/%d/%Y')
dados['Year'] = dados['Date'].dt.year.astype(int)

for i in range(1981, 1991):
    new_column = str(i)
    dados[new_column] = dados.apply(lambda row: row['Date'].strftime('%m-%d') if row['Year'] == i else None, axis=1)

dados = dados.drop(['Year'],axis =1)


for i in range(1981,1991):
    j = str(i)
    dados[j] = dados[j].replace({None: np.nan})
    dados[j] = dados[j].replace({np.nan: '0'})
    y = dados['1981']
    print(y)
    plt.plot(y,T)
    plt.show()

probabilidade_ruido = 0.1
dados_temp = dados['Daily minimum temperatures'].copy()

# Adicione valores nulos aleatoriamente na coluna alvo
for i in range(1981,1991):
    j = str(i)
    for index in range(len(dados_temp)):
        if random.random() < probabilidade_ruido:
            dados_temp[index] += np.random.normal(scale= 1)
        # if random.random() < probabilidade_ruido:
        #     dados.at[index, j] += np.random.normal(scale= 30)
# dados_Campo.to_csv('dados.csv',index= False)
dados['Daily minimum temperatures'] = dados_temp
T = dados_temp

for i in range(1981,1991):
    j = str(i)
    y = dados[j].values
    # plt.plot(y,T)
    # plt.show()
    
