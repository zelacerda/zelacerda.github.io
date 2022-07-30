from time import time
from random import random, seed, shuffle


V_FREQ = {'a': 0.3235, 'e': 0.2592, 'i': 0.1971, 'o': 0.1610,
          'u': 0.0592}

C_FREQ = {'b': 0.0233, 'c': 0.0757, 'd': 0.0612, 'f': 0.0226,
          'g': 0.0258, 'h': 0.0142, 'j': 0.0064, 'l': 0.0493,
          'm': 0.0981, 'n': 0.0800, 'p': 0.0397, 'q': 0.0062,
          'r': 0.1743, 's': 0.1920, 't': 0.0780, 'v': 0.0332,
          'x': 0.0060, 'z': 0.0140}


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
    now = int(time())
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
