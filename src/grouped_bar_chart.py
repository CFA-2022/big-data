import seaborn as sns
import pandas
import matplotlib.pyplot as plt

csv_med = pandas.read_csv(r'./data/incendies-year-med.csv',  sep=';')
csv_horsmed = pandas.read_csv(r'./data/incendies-year-horsmed.csv',  sep=';')
df = pandas.merge(csv_med, csv_horsmed, on='year')

df.plot.bar(x='year',logy=True, figsize=(12, 8))
plt.legend(loc='upper left')

plt.show()
