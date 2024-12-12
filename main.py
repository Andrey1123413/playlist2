import random
import re

# Функция для парсинга плейлиста строк
def parse_playlist_e(playlist):
    pattern = re.compile(r"(.+?)\s+(\d+[\.:]\d+)")
    songs = pattern.findall(playlist)
    return {name: float(time.replace(':', '.')) for name, time in songs if time}