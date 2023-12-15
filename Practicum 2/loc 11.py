import pandas as pd

data = pd.read_csv('/datasets/projects.csv')

rows = (data['Эксперимент'] == '+') & (data['Статья'] == '+')
print(data.loc[rows])