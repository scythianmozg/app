import pandas as pd

support_log = pd.read_csv('/datasets/support_log.csv')
support_log_grouped = support_log.groupby('type_id').count()
def alert_group(messages): 
    if messages <= 300: 
        return 'средний' 
    if messages <= 500: 
        return 'высокий' 
    return 'критичный' 

#print(alert_group(10)) 
#print(alert_group(450)) 
#print(alert_group(1000))

support_log_grouped['alert_group'] = support_log_grouped['user_id'].apply(alert_group) 
print(support_log_grouped.head(10))