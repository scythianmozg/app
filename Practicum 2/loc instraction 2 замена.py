import pandas as pd

data = pd.read_csv('/datasets/projects.csv')

data.loc[data['Эксперимент'] == '+', 'Роль'] = 'экспериментатор'
print(data)