favorite_songs = {
    'Серёга': ['Unforgiven', 'Holiday', 'Highway to hell'], 
    'Соня': ['Shake it out', 'The Show Must Go On', 'Наше лето'], 
    'Дима': ['Владимирский централ', 'Мурка', 'Третье сентября']
}
# Ниже напишите код, который напечатает на экран, сколько у Димы любимых песен

# Ниже напишите код, который построчно напечатает
# все любимые песни Сони.
print(len(favorite_songs['Дима']))

songs = favorite_songs['Соня']

for song in songs:
     print(song)