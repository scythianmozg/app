import pandas as pd
df = pd.read_csv('music_log.csv')

# сохраняем Series в отдельную переменную
total_play = df['total play']

# через логическую индексацию получаем недослушанные треки,
# и считаем их методом count()
print(total_play[total_play <= 10].count())