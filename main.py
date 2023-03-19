# using https://www.kaggle.com/datasets/imdevskp/corona-virus-report

import pandas as pnds
import seaborn as sns
import matplotlib.pyplot as plt

data = pnds.read_csv("imports/4. covid_19_data.csv")

# decidir heatmap


# sns.heatmap(data.isnull())

# plt.show()



# mostrar os casos confirmados e recuperados de cada região/país 

dataRegion =  data.groupby("Region")['Confirmed', 'Recovered'].sum()

#--------------------------------------------#


# Remover todos os casos em que os confirmados são <10

dataConfirmed = data = data[~(data.Confirmed < 10)]


# Saber qual região temos o maior número de casos, organizar de forma ascendente o top 20

dataMostCases =  data.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(20)


# Menor número de mortes, top 50

dataLessDeaths =  data.groupby('Region').Deaths.sum().sort_values(ascending = True).head(50)


# Quantos casos reportados no Brasil até 29/04/2020? 
# US temos por estado

dataBrazil =  data[data.Region == 'Brazil']

dataUSA =  data[data.Region == 'US']


# Maior número de casos confirmados forma ascendente

dataConfirmedASC =  data.sort_values( by = ['Confirmed'] , ascending = True).head(50)


# inserir variável que deseja ver

print (dataBrazil)