from random import random, randint, shuffle

dices = ['ETUKNO', 'EVGTIN', 'DECAMP', 'IELRUW',
         'EHIFSE', 'RECALS', 'ENTDOS', 'OFXRIA',
         'NAVEDZ', 'EIOATA', 'GLENYU', 'BMAQJO',
         'TLIBRA', 'SPULTE', 'AIMSOR', 'ENHRIS']

freq = {'a': 0.1462, 'b': 0.0104, 'c': 0.0388, 'd': 0.0499,
        'e': 0.1257, 'f': 0.0102, 'g': 0.0130, 'h': 0.0128,
        'i': 0.0618, 'j': 0.0040, 'k': 0.0002, 'l': 0.0278,
        'm': 0.0474, 'n': 0.0505, 'o': 0.1073, 'p': 0.0252,
        'q': 0.0120, 'r': 0.0653, 's': 0.0781, 't': 0.0434,
        'u': 0.0463, 'v': 0.0167, 'w': 0.0001, 'x': 0.0021,
        'y': 0.0001, 'z': 0.0047}

def roll_dice(dice):
    return dice[randint(0, 5)]

def roll_dices():
    board = []
    for dice in dices:
        board.append(roll_dice(dice))
    shuffle(board)
    return board[0:4], board[4:8], board[8:12], board[12:16]

def get_letter():
    '''Deprecated: use roll_dice instead.'''
    value = random()
    acc = 0
    for l, v in freq.items():
        acc+= v
        if value <= acc:
            return l.upper()

def get_letters(n):
    '''Deprecated: use roll_dices instead.'''
    result = []
    for _ in range(n):
        result.append(get_letter())
    return result

