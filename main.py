# using https://www.kaggle.com/datasets/imdevskp/corona-virus-report

import pandas as pnds
import seaborn as sns
import matplotlib.pyplot as plt

data = pnds.read_csv("imports/4. covid_19_data.csv")

# decidir heatmap


# sns.heatmap(data.isnull())

# plt.show()



# mostrar os casos confirmados e recuperados de cada região/país 

print (data.groupby("Region")['Confirmed', 'Recovered'].sum())

#--------------------------------------------#


# Remover todos os casos em que os confirmados são <10

print (data = data[~(data.Confirmed < 10)])


# Saber qual região temos o maior número de casos, organizar de forma ascendente o top 20

print (data.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(20))


# Menor número de mortes, top 50

print (data.groupby('Region').Deaths.sum().sort_values(ascending = True).head(50))


# Quantos casos reportados no Brasil até 29/04/2020? 
# US temos por estado

print (data[data.Region == 'Brazil'])

print (data[data.Region == 'US'])


# Maior número de casos confirmados forma ascendente

print (data.sort_values( by = ['Confirmed'] , ascending = True).head(50))