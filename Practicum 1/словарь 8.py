tracklist = [
    {
        'title': 'Stronger', # название трека
        'artist': 'Saimoo', # исполнитель
        'duration': 145, # продолжительность (в секундах)
        'genre': 'Deep House', # жанр
    },
    {
        'title': 'Alors On Danse',
        'artist': 'Stromae',
        'duration': 205,
        'genre': 'Hip-Hop',
    },
    {
        'title': 'Don\'t Be So Shy',
        'artist': 'Imany (Filatov & Karas Remix)',
        'duration': 190,
        'genre': 'Deep House',
    },
    {
        'title': 'Off My Mind',
        'artist': 'Matvey Emerson',
        'duration': 130,
        'genre': 'Deep House',
    },
    {
        'title': 'Now You\'re Gone',
        'artist': 'Basshunter',
        'duration': 154,
        'genre': 'Eurodance',
    },
    {
        'title': 'It Was A Good Day',
        'artist': 'Ice Cube',
        'duration': 260,
        'genre': 'Hip-Hop',
    },
    {
        'title': 'Diva',
        'artist': 'Beyonce',
        'duration': 200,
        'genre': 'Hip-Hop',
    }
]

hip_hop_duration = 0

for song in tracklist:
    if song['genre'] == 'Hip-Hop':
        hip_hop_duration += song['duration']

print(hip_hop_duration)