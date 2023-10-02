import pandas
import seaborn

data = pandas.read_csv('app_stats.csv')
seaborn.heatmap(data) 