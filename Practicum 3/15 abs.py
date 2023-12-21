import pandas as pd

data = [
    ['600748331392', 'C', 17515.4],
    ['600748331404', 'B', -10117.6],
    ['600748331412', 'B', 18489.3],
    ['600748331430', 'B', 6620.22],
    ['600748331447', 'C', -7559.9]
]

transactions = pd.DataFrame(data, columns=['id', 'category', 'amount'])
# используем метод abs(), чтобы привести все значения к неотрицательным
transactions['amount'] = transactions['amount'].abs()
print(transactions)