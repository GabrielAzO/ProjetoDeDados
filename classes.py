import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# mostrar os casos confirmados e recuperados de cada região/país

class dataRegionClass:
    def __init__(self, data):
        dataRegion = data.groupby("Region")['Confirmed', 'Recovered'].sum()
        print(dataRegion)


# Remover todos os casos em que os confirmados são <10

class dataConfirmedClass:
    def __init__(self, data):
        dataConfirmed = data[~(data.Confirmed < 10)]
        print(dataConfirmed)


# Saber qual região temos o maior número de casos, organizar de forma ascendente o top 20
# atualmente não funciona

class dataMostCasesClass:
    def __init__(self, data):
        # dataMostCases =  data.groupby('Country/Region').Confirmed.sum().sort_values(ascending = False).head(20)
        X = data['Country/Region'].head(20)
        Y = data['Confirmed'].head(20)
        plt.bar(X, Y)
        plt.show()


# Menor número de mortes, top 50

class dataLessDeathsClass:
    def __init__(self, data):
        dataLessDeaths =  data.groupby('Region').Deaths.sum().sort_values(ascending = True).head(50)
        print(dataLessDeaths)


# Quantos casos reportados no Brasil até 29/04/2020? 
# US temos por estado

class dataBrazilClass:
    def __init__(self, data):
        dataBrazil =  data[data.Region == 'Brazil']
        print(dataBrazil)

class dataBrazilClass:
    def __init__(self, data):
        dataUSA =  data[data.Region == 'US']
        print(dataUSA)

        
# Maior número de casos confirmados forma ascendente

class dataBrazilClass:
    def __init__(self, data):
        dataConfirmedASC =  data.sort_values( by = ['Confirmed'] , ascending = True).head(50)
        print(dataConfirmedASC)