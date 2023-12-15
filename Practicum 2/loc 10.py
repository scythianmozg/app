import pandas as pd

data = pd.read_csv('/datasets/projects.csv')

rows = (data['Новая функция'] == '+') & (data['Роль'] == 'разработчик')
data.loc[rows, "Роль"] = "улучшатель"

print(data)