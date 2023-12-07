import pandas as pd

data = pd.read_csv('/datasets/projects.csv')
data.head()
rows = [True, False, True, False, False, False, True, False]
print(data.loc[rows])