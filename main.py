#using https://www.kaggle.com/datasets/imdevskp/corona-virus-report

import pandas as pnds
import seaborn as sns
import matplotlib.pyplot as plt

data = pnds.read_csv("4. covid_19_data.csv")

# sns.heatmap(data.isnull())

# plt.show()


print (data.groupby("Region")['Confirmed', 'Recovered'].sum())