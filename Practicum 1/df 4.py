import pandas as pd
df = pd.read_csv('music_log.csv')

rock = df[df['genre'] == 'rock']

rock_time = rock['total play']