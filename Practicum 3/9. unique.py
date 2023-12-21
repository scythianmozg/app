import pandas as pd

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
df = pd.DataFrame(data)
group = df["source"].unique()
print(group)