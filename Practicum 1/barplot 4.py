import matplotlib
import pandas
import seaborn

matplotlib.rcParams['figure.figsize'] = [15, 7] # указываем размер графика

data = pandas.read_csv('app_stats.csv')

seaborn.barplot(x =data['week_number'], y =data['payments'])