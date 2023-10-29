import pandas as pd
df = pd.read_csv('music_log_upd.csv')
track_grouping = df.groupby('user_id')['genre_name']
# считаем количество композиций для каждого пользователя 
track_counting = track_grouping.count() 
 
# выводим первые 30 строк 
print(track_counting.head(30))