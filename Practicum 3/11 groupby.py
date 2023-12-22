import pandas as pd

transactions = pd.read_excel('/datasets/ids.xlsx')
transactions['id'] = pd.to_numeric(transactions['id'], errors='coerce')
transactions['amount'] = pd.to_numeric(transactions['amount'], errors='coerce')
transactions_per_category = transactions.groupby('category')['amount'].sum() # Рассчитайте сумму продаж для каждой категории
print(transactions_per_category)