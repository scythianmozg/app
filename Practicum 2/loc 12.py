import pandas as pd

data = pd.read_csv('/datasets/projects.csv')
data.loc[(data['Новая функция'] == '+') & (data['Роль'] == 'разработчик'), 'Новая функция'] = '-'
print(data)