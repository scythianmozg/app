import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')

visits = logs.groupby('source')['user_id'].count() # количество визитов
purchase = logs.groupby('source')['purchase'].sum() # количество покупок

conversion = purchase / visits # поделите количество покупок на количество визитов
print(conversion)