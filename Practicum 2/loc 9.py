import pandas as pd

data = pd.read_csv('/datasets/projects.csv')

data.loc[data['Новая функция'] != '+', 'Новая функция'] = '-'
print(data)