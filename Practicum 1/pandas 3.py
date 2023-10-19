import pandas as pd

df = pd.read_csv('music_log.csv')
shape_table = df.shape
print('Размер таблицы:',shape_table)