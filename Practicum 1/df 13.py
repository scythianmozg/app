import pandas as pd
df = pd.read_csv('music_log.csv')
df = df.rename(columns={'  user_id':'user_id','total play':'total_play','Artist':'artist'})
print(df.columns)