import pandas as pd

df = pd.read_csv('music_log.csv') 
shape_table = df.shape

observations_table = df.shape[0]
print('Количество наблюдений:',observations_table)