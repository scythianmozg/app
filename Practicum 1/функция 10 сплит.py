def get_hours_and_minutes(time_string):
    time_list = time_string.split(':')
    h = int(time_list[0])
    m = int(time_list[1])
    return h, m

time_str = '12:35'
hours, minutes = get_hours_and_minutes(time_str)
print(hours, minutes)