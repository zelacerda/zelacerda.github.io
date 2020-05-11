import random

def generate_ticket(ticket_number=None):

    if ticket_number is None:
        ticket_number = random.randint(1, 9999)
    random.seed(ticket_number)

    valid = False

    while not valid:
        lines = [random.sample(range(9), 5) for _ in range(3)]
        tens_counts = [sum([d in line for line in lines]) for d in range(9)]
        if 0 not in tens_counts:
            valid = True

    pos = sorted([(c, i) for i, l in enumerate(lines) for c in l])

    numbers = []
    for tens, count in enumerate(tens_counts):
        if tens < 8:
            range_values = range(tens * 10 + 1, (tens + 1) * 10)
        else:
            range_values = range(81, 91)
        numbers.extend(random.sample(range_values, count))

    numbers = sorted(numbers)
    ticket = [[], [], []]
    for i, num in enumerate(numbers):
        ticket[pos[i][1]].append(num)

    return f'{ticket_number:04d}', ticket


def to_string(ticket):
    grid = [['' for j in range(9)] for i in range(3)]
    for line, numbers in enumerate(ticket):
        for number in numbers:
            if number == 90:
                column = 8
            else:
                column = int(number / 10)
            grid[line][column] = str(number)
    return grid