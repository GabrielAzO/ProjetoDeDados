# using https://www.kaggle.com/datasets/imdevskp/corona-virus-report

from classes import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("imports/full_grouped.csv")

data['Date'] = pd.to_datetime(data['Date'])

data['Date'] = pd.to_numeric(data['Date'])


# inserir classe que deseja ver

dataConfirmedClass(data)

#------------------------------------------------------------------------------------------------#
# dataHeat = data.drop(columns=['State', 'Region', 'Deaths', 'Recovered'])

# plt.plot(dataHeat['Date'],dataHeat['Confirmed'])

# plt.figure(figsize=(9,9))
# pivot_table = data.pivot('Date', 'Confirmed','Deaths','Recovered')
# plt.xlabel('Confirmed', size = 15)
# plt.ylabel('Date', size = 15)
# plt.title('HeatMap Geral', size = 15)
# sns.heatmap(pivot_table, annot=True, fmt=".1f", linewidths=.5, square = True, cmap = 'Blues_r');
# # decidir heatmap
# data['Date'] = data['Date'].map(lambda x:x.date())

# sns.heatmap(dataHeat)

# plt.show()
#------------------------------------------------------------------------------------------------#

