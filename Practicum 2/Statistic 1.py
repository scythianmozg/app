import pandas as pd

hogwarts_points = pd.read_csv('/datasets/hogwarts_points.csv')
hogwarts_points['faculty_name'] = hogwarts_points['faculty_name'].fillna(value='Гриффиндор')
points_sum = hogwarts_points['points'].sum()
faculty_sum = hogwarts_points.groupby('faculty_name')['points'].sum()
winner = hogwarts_points.groupby('faculty_name')['points'].sum().idxmax()

print(f'Сумма баллов учеников: {hogwarts_points["points"].sum()}') , # сумма значений столбца 'points'
print(f'Сумма баллов факультетов: {hogwarts_points.groupby("faculty_name")["points"].sum().sum()}') , # сгруппируйте по столбцу 'faculty_name'
# сложите значения столбца 'points' этой группировки методом sum()
# и примените метод sum() к результату

print(f'Кубок получает {hogwarts_points.groupby("faculty_name")["points"].sum().idxmax()}')