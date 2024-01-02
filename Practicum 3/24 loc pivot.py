import pandas as pd
data_final = pd.read_csv('/datasets/data_final.csv')
data_pivot = data_final.pivot_table(index=['category_name', 'subcategory_name'], columns='source', values='visits', aggfunc='sum')
data_pivot['ratio'] = data_pivot['organic'] / data_pivot['direct']

data_pivot = data_pivot.loc[data_pivot['direct'] > 1000]
 
print(data_pivot.sort_values(by='ratio', ascending=False).tail(10))