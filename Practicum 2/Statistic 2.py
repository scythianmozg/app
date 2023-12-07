import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')

visits = logs.groupby('source')['user_id'].count()
print(visits)

#Посчитайте значения в колонке 'source', вызвав методы groupby() и count(), либо метод value_counts(). Если используете groupby(), группируйте данные из колонки 'user_id' по колонке 'source'.