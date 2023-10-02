import matplotlib.pyplot as plt
import pandas
import seaborn

plt.rcParams['figure.figsize'] = (4, 8) # указываем размер визуализации
data = pandas.read_csv('polomki.csv', index_col='Магазин')
data['Неделя 14'] = data['Неделя 14']*100
seaborn.heatmap(data)