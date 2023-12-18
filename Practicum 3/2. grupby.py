import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')
logs['email'] = logs['email'].fillna(value='')
print(logs)