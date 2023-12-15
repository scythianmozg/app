import pandas as pd

data = pd.read_csv('/datasets/projects.csv')

rows = data['Новая функция'] == '+'
print(data.loc[rows])