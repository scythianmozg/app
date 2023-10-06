# импортируем библиотеки
import pandas
import matplotlib
import seaborn

# указываем размер графика
matplotlib.rcParams['figure.figsize'] = [15, 7]

# читаем файл и записываем в переменную
data = pandas.read_csv('crops_usa.csv')

# группируем значения Acres и Production по годам и суммируем по каждой группе
acres_usa = data.groupby('Year')['Acres'].sum()
production_usa = data.groupby('Year')['Production'].sum()

# Делим значения столбца production_usa на значения столбца acres_usa,
# получаем урожайность и сохраняем её в yield_usa
yield_usa = production_usa / acres_usa

# достаём индексы (порядковые номера) столбца acres_usa, это числа от 1980 до 2019
years_unique = acres_usa.index.values

# постройте столбчатую диаграмму урожайности по годам
seaborn.barplot(x= years_unique, y= yield_usa)