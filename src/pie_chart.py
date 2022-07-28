import matplotlib.pyplot as plt
import pandas
import seaborn as sns

csv = pandas.read_csv(r'./data/incendies-total.csv',  sep=';')

#define data
labels = csv['dep'].tolist()
data = csv['total'].tolist()

#define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:len(labels)]

#create pie chart
plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')

plt.title("Fréquence d'incendies par déparetment")

plt.show()
