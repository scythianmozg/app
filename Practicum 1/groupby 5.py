import pandas as pd
df = pd.read_csv('music_log_upd.csv')

genre_grouping = df.groupby('user_id')['genre_name']

def user_genres(group):
  for col in group:
    if len(col[1]) > 50:
      user = col[0]
      return user

search_id = user_genres(genre_grouping)
# Получим таблицу с прослушанными меломаном треками.Для этого запросите из структуры данных df строки, отвечающие сразу двум условиям:
#1) значение в столбце 'user_id' должно быть равно значению переменной search_id;
#2) время прослушивания, т.е. значение в столбце 'total_play_seconds', не должно равняться 0.
#Сохраним результат в переменной music_user.

music_user = df[(df['user_id'] == search_id)&(df['total_play_seconds'] != 0)]
# Cгруппируем данные таблицы music_user по столбцу 'genre_name' и получите сумму значений столбца 'total_play_seconds'. Сохраним результат в переменной sum_music_user и выведем её значение на экран.
sum_music_user = music_user.groupby('genre_name')['total_play_seconds'].sum()
# print(sum_music_user)
# Сгруппируем данные по столбцу genre_name и посчитаем, сколько значений в столбце genre_name. Сохраним результат в переменной count_music_user и выведем её значение на экран.
count_music_user = music_user.groupby('genre_name').count()
print(count_music_user)