import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')

xiaomi = stock[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum()
huawei = stock[stock['item'] == 'Смартфон HUAWEI P30 lite']['count'].sum()


stock = stock.drop_duplicates(subset='item',  keep='first')
print(stock)