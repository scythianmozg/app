import pandas as pd
support = pd.read_csv('/datasets/support.csv')
support = support.rename(columns={'Тип обращения':'type_message','Время обращения':'timestamp'})
support.info()