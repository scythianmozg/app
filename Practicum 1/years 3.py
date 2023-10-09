import matplotlib
import seaborn
import pandas

matplotlib.rcParams['figure.figsize'] = [10, 7] # указываем размер графика

data = pandas.read_csv('crops_usa.csv')

acres_2019 = data[data['Year'] == 2019]['Acres']
states_2019 = data[data['Year'] == 2019]['State']

seaborn.barplot(x = acres_2019, y = states_2019)