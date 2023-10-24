import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dados = pd.read_csv('daily-minimum-temperatures.csv')
print(dados.describe())
T = dados['Daily minimum temperatures'].values
plt.plot(T)
plt.show()
dados['Date'] = pd.to_datetime(dados['Date'], format='%m/%d/%Y')
dados['Year'] = dados['Date'].dt.year
# print(dados.describe())

for i in range(1981, 1991):
    new_column = str(i)
    dados[new_column] = dados.apply(lambda row: row['Date'].strftime('%m-%d') if row['Year'] == i else None, axis=1)

dados_Campo = dados.drop(['Year'],axis =1)

# dados_Campo.to_csv('dados.csv',index= False)
# Substitua os valores None por NaN (valores ausentes)

for i in range(1981,1991):
    j = str(i)
    dados[j] = dados[j].replace({None: np.nan})
    dados[j] = dados[j].replace({np.nan: '0'})
    y = dados['1981']
    print(y)
    plt.plot( y,T)
    plt.show()


