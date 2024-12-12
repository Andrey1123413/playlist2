import random
import re

# Функция для парсинга плейлиста строк
def parse_playlist_e(playlist):
    pattern = re.compile(r"(.+?)\s+(\d+[\.:]\d+)")
    songs = pattern.findall(playlist)
    return {name: float(time.replace(':', '.')) for name, time in songs if time}
# Функция для парсинга плейлиста из кортежа 
def parse_playlist_f(playlist):
    combined_dict = {}
    for p in playlist:
        combined_dict.update(p)
    return combined_dict
# Функция для объединения двух плейлистов
def combine_playlists(playlist_e, playlist_f):
    playlist_e_dict = parse_playlist_e(playlist_e)
    playlist_f_dict = parse_playlist_f(playlist_f)
    combined_playlist = {**playlist_e_dict, **playlist_f_dict}
    return combined_playlist

# Функция для выбора случайных песен из плейлиста
def select_random_songs(combined_playlist, n):
    return random.sample(list(combined_playlist.items()), n)

# Функция для подсчета общего времени звучания
def calculate_total_time(selected_songs):
    total_time = sum(time for _, time in selected_songs)
    return total_time

# Основная функция для подсчета общего времени звучания n случайных песен
def get_duration(playlist_e, playlist_f, n):
    combined_playlist = combine_playlists(playlist_e, playlist_f)
    selected_songs = select_random_songs(combined_playlist, n)
    total_time = calculate_total_time(selected_songs)
    return total_time

# Плейлисты из нашего задания(5 задание 2 кейс Крупкин и Коршунов)
playlist_e = """
Sunday 5:09
Why Does My Heart Feel so Bad? 4.23
Everlong 3.25
To Let Myself Go
Golden 2.56
Daisuke 2.41
Miami 3.31
Chill Bill Lofi 2.05
The Perfect Girl 1.48
Resonance 3.32
"""

playlist_f = (
    {"Free Bird": 9.08, "Enter Sandman": 5.31, "One": 7.45, "Sliver" : 2.10, "Come as You Are": 3.45},
    {"Thunderstruck": 4.53, "You Shook Me All Night Long": 3.29, "Everlong" : 4.51, "My Hero" : 4.02},
)
