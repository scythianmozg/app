import pandas

data = pandas.read_csv('crops_usa.csv')

production_2018 = data[data['Year'] == 2018]['Production']
print(production_2018)