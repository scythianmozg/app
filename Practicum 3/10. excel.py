import pandas as pd
subcategory_dict = pd.read_excel('/datasets/seo_data.xlsx', sheet_name = 'subcategory_ids')
subcategory_dict.head(5)
print(subcategory_dict.head(5))