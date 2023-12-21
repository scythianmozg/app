import pandas as pd

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
data['visits'] = pd.to_numeric(data['visits'])