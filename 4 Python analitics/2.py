import pandas

data = pandas.read_csv('polomki.csv', index_col='Магазин')
data['Неделя 14'] = data['Неделя 14'] * 100
print(data)