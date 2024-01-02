import pandas as pd

# служебная строка для печати всех столбцов таблицы на экран
pd.set_option('display.max_columns', None)

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')
stock['item_lowercase'] = stock['item'].str.lower()

apple = stock[stock['item_lowercase'] == 'смартфон apple iphone xr 64gb']['count'].sum()
samsung = stock[stock['item_lowercase'] == 'смартфон samsung galaxy a30 32gb']['count'].sum()

stock = stock.drop_duplicates(subset=['item_lowercase'], keep='first')
stock = stock.reset_index(drop=True)
stock.loc[3, 'count'] = apple
# запишите новое количество телефонов Apple в ячейку таблицы
# выведите таблицу stock на экран
print(stock)