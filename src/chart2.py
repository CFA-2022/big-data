import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

csv19902000 = pd.read_csv(r'./data/incendies-1990-2000.csv',  sep=';')
csv20002010 = pd.read_csv(r'./data/incendies-2000-2010.csv',  sep=';')
csv20102020 = pd.read_csv(r'./data/incendies-2010-2020.csv',  sep=';')
csv2021 = pd.read_csv(r'./data/incendies-2021.csv',  sep=';')
csv2022 = pd.read_csv(r'./data/incendies-2022.csv',  sep=';')

res = sns.lineplot(x="dep", y="surface", data=csv19902000, color="blue", label="1990-2000")

res = sns.lineplot(x="dep", y="surface", data=csv20002010, color="green", label="2000-2010")

res = sns.lineplot(x="dep", y="surface", data=csv20102020, color="red", label="2010-2020")

res = sns.lineplot(x="dep", y="surface", data=csv2021, color="black", label="2021")

res = sns.lineplot(x="dep", y="surface", data=csv2022, color="purple", label="2022")

res.set_xlabel("Département", fontsize = 10)
res.set_ylabel("Surface", fontsize = 10)
res.set_title("Surface moyenne brulée par dix ans")

plt.show()