import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')
logs['email'] = logs['email'].fillna(value='')

logs.loc[logs['source'] == 'None', 'source'] = 'email' 
print(logs['source'].value_counts())