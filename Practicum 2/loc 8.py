import pandas as pd

data = pd.read_csv('/datasets/projects.csv')
print(data.loc[data['Эксперимент'] == '+', 'Имя'])