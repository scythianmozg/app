import pandas as pd

data = pd.read_csv('/datasets/projects.csv')

data['Новая функция'] = data.loc[:,'Новая функция'].fillna('+')

print(data)