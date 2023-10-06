import pandas

data = pandas.read_csv('crops_usa.csv')

# отберите значения Year, равные 2019, затем укажите столбец Acres
acres_2019 = data[data['Year'] == 2019]['Acres']
# отберите значения Year, равные 2019, затем укажите столбец State
states_2019 = data[data['Year'] == 2019]['State']

print(acres_2019)
print(states_2019)