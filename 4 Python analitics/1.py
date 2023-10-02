import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (4, 8) # указываем размер визуализации

import pandas

data = pandas.read_csv('polomki.csv', index_col='Магазин')

import seaborn
seaborn.heatmap(data)