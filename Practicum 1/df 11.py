import pandas as pd

board_df = pd.read_csv('game_board.csv')
# напишите ваш код здесь

print(board_df.loc[5, 'C':'F'])