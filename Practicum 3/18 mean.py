import pandas as pd

position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(
    position['timestamp'], format='%Y-%m-%dT%H:%M:%S'
)
position['month'] = pd.DatetimeIndex(position['timestamp']).month

print(position.groupby('month')['level'].mean())