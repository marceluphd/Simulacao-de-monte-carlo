#IMPORTANDO BIBLIOTECAS
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#EU IA FAZER O TREM PARA FICAR RELENDO OS DIAS ATUAIS SEMPRE MAIS VOU DEIXR PRO PROXIMO
#start = dt.datetime(2012, 01, 01)
#end = dt.datetime(2020, 02, 26)

precos = web.DataReader('ITUB4.SA', data_source='yahoo', start='2012-01-01', end='2020-02-26')['Close']
returns = precos.pct_change()

ultimo_preco = precos[-1]

#Numero de simulações
num_simulacoes = 1000
num_dias = 252

simulacao_df = pd.DataFrame()

for x in range(num_simulacoes):
    count = 0
    daily_vol = returns.std()
    
    preco_series = []
    
    preco = ultimo_preco * (1 + np.random.normal(0, daily_vol))
    preco_series.append(preco)
    
    for y in range(num_dias):
        if count == 251:
            break
        preco = preco_series[count] * (1 + np.random.normal(0, daily_vol))
        preco_series.append(preco)
        count += 1
    
    simulacao_df[x] = preco_series
    
fig = plt.figure()
plt.figure(figsize=(18,8))
plt.title('Simulação de Monte Carlo : ITUB4.SA ')
plt.plot(simulacao_df)
plt.axhline(y = ultimo_preco, color = 'r', linestyle = '-')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.show()

