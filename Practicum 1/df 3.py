import pandas as pd
df = pd.read_csv('music_log.csv')

# Получаем Series из датафрейма
artist = df['Artist']

# Получаем ячейку из Series по единственной координате
print(artist[0]) 