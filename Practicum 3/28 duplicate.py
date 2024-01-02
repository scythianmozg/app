import pandas as pd

df = pd.DataFrame({
    'name': ['Сырок Мечта', 'Молоко Отличное', 'Сырок Мечта', 'Сырок Дружба',\
             'Сырок Дружба', 'Молоко Вкусное'],
    'count': [120, 200, 125, 100, 35, 500]
})

mechta = df[df['name'] == 'Сырок Мечта']['count'].sum()
druzhba = df[df['name'] == 'Сырок Дружба']['count'].sum()

df = df.drop_duplicates(subset=['name'], keep='first')
df = df.reset_index(drop=True)

df.loc[0, 'count'] = mechta
df.loc[2, 'count'] = druzhba

print(df)