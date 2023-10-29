import pandas as pd

df = pd.read_csv('music_log_upd.csv')
track_grouping = df.groupby('user_id')['genre_name']


def user_tracks(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user
        
search_id = user_tracks(track_grouping)
print(search_id)