import pandas as pd

metrica = pd.read_csv('/datasets/metrica_data.csv')
age_avg = metrica['age'].mean()
metrica['age']=metrica['age'].fillna(value = age_avg)

time_avg = metrica['time'].mean() #запишите среднее время просмотра
print(time_avg)
print(metrica.head(10))