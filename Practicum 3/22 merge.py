import pandas as pd
data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
subcategory_dict = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='subcategory_ids')
data_subcategory = data.merge(subcategory_dict, on='subcategory_id', how='left')
print(data_subcategory.head(10))