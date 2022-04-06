import time
from random import random, seed
from turtle import pos


FREQ = {'a': 0.1462, 'b': 0.0104, 'c': 0.0388, 'd': 0.0499,
        'e': 0.1257, 'f': 0.0102, 'g': 0.0130, 'h': 0.0128,
        'i': 0.0618, 'j': 0.0040, 'k': 0.0002, 'l': 0.0278,
        'm': 0.0474, 'n': 0.0505, 'o': 0.1073, 'p': 0.0252,
        'q': 0.0120, 'r': 0.0653, 's': 0.0781, 't': 0.0434,
        'u': 0.0463, 'v': 0.0167, 'w': 0.0001, 'x': 0.0021,
        'y': 0.0001, 'z': 0.0047}

def get_letter():
    value = random()
    acc = 0
    for l, v in FREQ.items():
        acc+= v
        if value <= acc:
            return l.upper()

def get_letters(n, random_seed=None):
    if random_seed:
        seed(random_seed)
    result = []
    for _ in range(n):
        result.append(get_letter())
    return result

def count2sec(count):
    min = int(count / 60)
    sec = count % 60
    return f"{min}:{sec:02d}"

def get_day_game():
    init_time = 1644116400 # 2022-02-06 00:00
    now = int(time.time())
    day_game = int((now - init_time) / 86400) + 1
    return day_game

def pos_to_coord(num, grid_size=4):
    return num // grid_size, num % grid_size

def is_adjacent(last_pos, new_pos):
    if last_pos is None:
        return True
    else:
        x1, y1 = pos_to_coord(last_pos)
        x2, y2 = pos_to_coord(new_pos)
        dist = max(abs(x2-x1), abs(y2-y1))
        return dist == 1
