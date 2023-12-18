import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')

visits = logs.groupby('source')['purchase'].count()
purchase = logs.groupby('source')['purchase'].sum()

conversion = purchase / visits
print(conversion)