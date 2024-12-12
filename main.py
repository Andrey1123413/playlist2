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

