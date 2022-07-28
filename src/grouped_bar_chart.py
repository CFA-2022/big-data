import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

csv_med = pd.read_csv(r'./data/incendies-year-med.csv',  sep=';')
csv_horsmed = pd.read_csv(r'./data/incendies-year-horsmed.csv',  sep=';')
df = pd.merge(csv_med, csv_horsmed, on='year', suffixes=('_med', '_horsmed'))
df = pd.melt(df, id_vars="year", var_name="type", value_name="surface")

sns.catplot(x='year', y='surface', hue='type', data=df, kind='bar')

#plt.legend(loc='upper left')

plt.show()

