import time
from random import random, seed, shuffle
from turtle import pos


FREQ = {'a': 0.1462, 'b': 0.0104, 'c': 0.0388, 'd': 0.0499,
        'e': 0.1257, 'f': 0.0102, 'g': 0.0130, 'h': 0.0128,
        'i': 0.0618, 'j': 0.0040, 'k': 0.0002, 'l': 0.0278,
        'm': 0.0474, 'n': 0.0505, 'o': 0.1073, 'p': 0.0252,
        'q': 0.0120, 'r': 0.0653, 's': 0.0781, 't': 0.0434,
        'u': 0.0463, 'v': 0.0167, 'w': 0.0001, 'x': 0.0021,
        'y': 0.0001, 'z': 0.0047}


V_FREQ = {'a': 0.300, 'e': 0.258, 'i': 0.127, 'o': 0.22,
          'u': 0.095}

C_FREQ = {'b': 0.020, 'c': 0.076, 'd': 0.097, 'f': 0.020,
          'g': 0.025, 'h': 0.025, 'j': 0.008, 'l': 0.054,
          'm': 0.093, 'n': 0.099, 'p': 0.049, 'q': 0.023,
          'r': 0.127, 's': 0.153, 't': 0.085, 'v': 0.033,
          'x': 0.004, 'z': 0.009}


def get_letter(group='vowel'):
    freqs = {'vowel': V_FREQ, 'consonant': C_FREQ}
    value = random()
    acc = 0
    for l, v in freqs[group].items():
        acc += v
        if value <= acc:
            return l.upper()

def get_letters(v, c, random_seed=None):
    if random_seed:
        seed(random_seed)
    result = []
    for _ in range(v):
        result.append(get_letter('vowel'))
    for _ in range(c):
        result.append(get_letter('consonant'))
    shuffle(result)
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
