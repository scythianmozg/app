import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')

#xiaomi = # подсчитайте количество телефонов Xiaomi Redmi
# выведите значение xiaomi на экран
xiaomi = stock[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum()
print(xiaomi)

huawei = stock[stock['item'] == 'Смартфон HUAWEI P30 lite']['count'].sum()