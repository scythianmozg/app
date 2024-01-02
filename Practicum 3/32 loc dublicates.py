import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')
xiaomi = stock[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum()
huawei = stock[stock['item'] == 'Смартфон HUAWEI P30 lite']['count'].sum()

stock = stock.drop_duplicates(subset=['item'], keep='first')
stock = stock.reset_index(drop=True)

# замените значение в ячейке с количеством смартфонов Xiaomi
stock.loc[0, 'count'] = xiaomi
# выведите таблицу stock на экран
print(stock)