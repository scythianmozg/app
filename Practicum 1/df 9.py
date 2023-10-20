import pandas as pd

board_df = pd.read_csv('game_board.csv')
print (board_df.loc[0, 'J'])