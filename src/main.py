import seaborn as sns
import pandas
import matplotlib.pyplot as plt

csv = pandas.read_csv(r'./data/incendies-moyen.csv',  sep=';')

fig, ax1 = plt.subplots(figsize=(20,16))

res = sns.barplot(x="dep", y="surface", data=csv, ax=ax1)

res.set_xlabel("Département", fontsize = 10)
res.set_ylabel("Surface(ha)", fontsize = 10)


ax2 = ax1.twinx()

res = sns.lineplot(x="dep", y="total", data=csv, ax=ax2)

plt.show()