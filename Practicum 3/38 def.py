import pandas as pd
support_log_grouped = pd.read_csv('/datasets/support_log_grouped.csv')

def alert_group_importance(row):
    alert_group = row['alert_group']
    importance = row['importance']
    if alert_group=='средний':
        if importance==1:
            return 'обратить внимание'
    if alert_group=='высокий':
        if importance== 1:
            return 'высокий риск'
    if alert_group=='критичный':
        if importance== 1:
            return 'блокер'
    return 'в порядке очереди'
   
row_values = ['высокий', 1]
row_columns = ['alert_group', 'importance']
row = pd.Series(data=row_values, index=row_columns)
print(alert_group_importance(row))