import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')
purchase = logs.groupby('source')['purchase'].sum()
print(purchase)