Задача 1
import pandas as pd
 
metrica = pd.read_csv('/datasets/metrica_data.csv')
age_avg = metrica['age'].mean()
print (age_avg)
 
Задача 2
import pandas as pd
 
metrica = pd.read_csv('/datasets/metrica_data.csv')
age_avg = metrica['age'].mean()
metrica['age']=metrica['age'].fillna(value = age_avg)
print(metrica.head(10))
 
Задача 3
import pandas as pd
 
metrica = pd.read_csv('/datasets/metrica_data.csv')
time_avg = metrica['time'].mean() #запишите среднее время просмотра
print(time_avg)
 
Задача 4
import pandas as pd
 
metrica = pd.read_csv('/datasets/metrica_data.csv')
desktop_data= metrica[metrica['device_type'] == 'desktop']
print(desktop_data.head())
 
Задача 5
import pandas as pd
 
metrica = pd.read_csv('/datasets/metrica_data.csv')
desktop_data= metrica[metrica['device_type'] == 'desktop']
desktop_data_time_avg = desktop_data['time'].mean()
print (desktop_data_time_avg)
 
Задача 6
import pandas as pd
 
metrica = pd.read_csv('/datasets/metrica_data.csv')
mobile_data = metrica[metrica['device_type'] == 'mobile']
print(mobile_data.head())
 
Задача 7
import pandas as pd
 
metrica = pd.read_csv('/datasets/metrica_data.csv')
mobile_data = metrica[metrica['device_type'] == 'mobile']
mobile_data_time_avg = mobile_data['time'].mean()
print (mobile_data_time_avg)