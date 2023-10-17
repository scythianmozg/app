def get_minutes_and_seconds(time_string):
    time_list = time_string.split(':')
    m = int(time_list[0])
    s = int(time_list[1])
    return m, s


def check_song_duration(time_string):
    minutes, seconds = get_minutes_and_seconds(time_string)
    seconds = minutes * 60 + seconds
    return seconds <= 210


tracks = ['2:25', '2:35', '3:45', '2:00', '5:10']

for song_duration in tracks:
    print(check_song_duration(song_duration))