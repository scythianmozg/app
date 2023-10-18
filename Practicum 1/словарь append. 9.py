from json import dumps

tracklist = [
    {
        'title': 'Stronger',
        'artist': 'Saimoo',
        'duration': 145,
        'genre': 'Deep House',
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

deep_house_tracklist = []
for item in tracklist:
    if item['genre'] == 'Deep House':
        deep_house_tracklist.append(item)


for track in deep_house_tracklist:
    print(dumps(track, indent=4))