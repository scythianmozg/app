import pandas as pd

data = pd.read_csv('/datasets/projects.csv')
rows = data['Роль'] != 'менеджер'
print(rows)