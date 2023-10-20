import pandas as pd
df = pd.read_csv('music_log.csv')

# <напишите код здесь>

rock = df.loc[df.loc[:, 'genre'] == 'rock']

#rock = df[df['genre'] == 'rock'] #второй вариант

# через логическую индексацию получаем недослушанные треки,
# и считаем их методом count()
# print(total_play[total_play <= 10].count()) 