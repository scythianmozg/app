import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')
print(stock['item'].value_counts())