import pandas as pd

df = pd.DataFrame({
    'name': ['Сырок Мечта', 'Молоко Отличное', 'Сырок Мечта', 'Сырок Дружба',\
             'Сырок Дружба', 'Молоко Вкусное'],
    'count': [120, 200, 125, 100, 35, 500]
})

mechta = df[df['name'] == 'Сырок Мечта']['count'].sum()
druzhba = df[df['name'] == 'Сырок Дружба']['count'].sum()
print('Сырок Мечта:', mechta, 'Сырок Дружба:', druzhba)