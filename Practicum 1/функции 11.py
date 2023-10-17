def get_minutes_and_seconds(time_string):
    time_list = time_string.split(':')
    m = int(time_list[0])
    s = int(time_list[1])
    return m, s


def check_song_duration(time_string):
    minutes, seconds = get_minutes_and_seconds(time_string)
    seconds = minutes * 60 + seconds
    if seconds < 210:
        return True
    return False

print(check_song_duration('4:35'))
print(check_song_duration('2:10'))