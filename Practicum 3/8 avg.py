# импортируем библиотеку pandas
import pandas as pd

# создаём датафрейм metrica из CSV-файла
metrica = pd.read_csv('/datasets/metrica_data.csv')

# перебираем каждый тип девайса в наборе уникальных значений столба device_type
for d in metrica['device_type'].unique():
    # на каждом шаге цикла с помощью атрибута loc выбираем строки,
    # в которых в device_type текущий тип девайса (d) и есть пропуски в time 
    metrica.loc[(metrica['device_type'] == d) & (metrica['time'].isna()), 'time'] = \
    metrica.loc[(metrica['device_type'] == d), 'time'].mean()
    # и записываем в них среднее значение time среди строк с текущим типом девайса (d)

# проверяем, что все пропуски заполнены
print(metrica['time'].isna().sum())