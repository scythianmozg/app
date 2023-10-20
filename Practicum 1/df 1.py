import pandas as pd

df = pd.read_csv('music_log.csv')
genre_fight = df[['genre', 'Artist']]

genre_pop = df.loc[df.loc[:, 'genre'] == 'pop']['genre'].count()
genre_rock = df.loc[df.loc[:, 'genre'] == 'rock']['genre'].count()
print(f'Число прослушанных треков в жанре поп равно {genre_pop}')
print(f'Число прослушанных треков в жанре рок равно {genre_rock}')

if genre_pop > genre_rock:
    print('Поп-музыку слушают больше.')
elif genre_pop < genre_rock:
    print('Рок слушают больше.')
else:
    print('Поп и рок слушают одинаково часто.')