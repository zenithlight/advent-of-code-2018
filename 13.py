import copy
import subprocess

# RDLU
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def print_tracks(carts, tracks):
    subprocess.call('clear', shell=True)

    for i, line in enumerate(tracks):
        printed_line = ''

        for j, character in enumerate(line):
            print_track = True

            for cart in carts:
                if (i, j) == cart['location']:
                    printed_line += ['>', 'v', '<', '^'][cart['direction']]
                    print_track = False

            if print_track:
                printed_line += character

        print(printed_line)

    input()

def key(cart):
    return cart['location'][0] + (cart['location'][1] * 0.0001)

def a(carts, tracks):
    while True:
        carts = [cart for cart in carts if 'should_remove' not in cart]
        carts.sort(key=key)

        for cart in carts:
            cart['location'] = tuple(sum(coordinate) for coordinate in zip(cart['location'], DIRECTIONS[cart['direction']]))

            x, y = cart['location']

            if tracks[x][y] == '/':
                if cart['direction'] == 0:
                    cart['direction'] = 3
                elif cart['direction'] == 1:
                    cart['direction'] = 2
                elif cart['direction'] == 2:
                    cart['direction'] = 1
                elif cart['direction'] == 3:
                    cart['direction'] = 0

            if tracks[x][y] == '\\':
                if cart['direction'] == 0:
                    cart['direction'] = 1
                elif cart['direction'] == 1:
                    cart['direction'] = 0
                elif cart['direction'] == 2:
                    cart['direction'] = 3
                elif cart['direction'] == 3:
                    cart['direction'] = 2

            if tracks[x][y] == '+':
                if cart['turn'] == 0:
                    cart['direction'] = (cart['direction'] - 1) % 4

                if cart['turn'] == 2:
                    cart['direction'] = (cart['direction'] + 1) % 4

                cart['turn'] = (cart['turn'] + 1) % 3

            for cart2 in carts:
                if cart['location'] == cart2['location'] and cart is not cart2:
                    return ','.join([str(coordinate) for coordinate in cart['location']][::-1])

def b(carts, tracks):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while True:
        carts = [cart for cart in carts if 'should_remove' not in cart]
        carts.sort(key=key)

        if len(carts) == 1:
            return ','.join([str(coordinate) for coordinate in carts[0]['location']][::-1])

        #print_tracks(carts, tracks)

        for cart in carts:
            cart['location'] = tuple(sum(coordinate) for coordinate in zip(cart['location'], DIRECTIONS[cart['direction']]))

            x, y = cart['location']

            if tracks[x][y] == '/':
                if cart['direction'] == 0:
                    cart['direction'] = 3
                elif cart['direction'] == 1:
                    cart['direction'] = 2
                elif cart['direction'] == 2:
                    cart['direction'] = 1
                elif cart['direction'] == 3:
                    cart['direction'] = 0

            if tracks[x][y] == '\\':
                if cart['direction'] == 0:
                    cart['direction'] = 1
                elif cart['direction'] == 1:
                    cart['direction'] = 0
                elif cart['direction'] == 2:
                    cart['direction'] = 3
                elif cart['direction'] == 3:
                    cart['direction'] = 2

            if tracks[x][y] == '+':
                if cart['turn'] == 0:
                    cart['direction'] = (cart['direction'] - 1) % 4

                if cart['turn'] == 2:
                    cart['direction'] = (cart['direction'] + 1) % 4

                cart['turn'] = (cart['turn'] + 1) % 3

            for cart2 in carts:
                if cart['location'] == cart2['location'] and cart is not cart2:
                    cart['should_remove'] = True
                    cart2['should_remove'] = True

with open('input/13', 'r') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]

    height = len(lines)
    width = max(len(line) for line in lines)

    carts = []
    tracks = [[' ' for _ in range(width)] for _ in range(height)]

    for i, line in enumerate(lines):
        for j, character in enumerate(line):
            if character in ('^', 'v'):
                carts.append({
                    'location': (i, j),
                    'direction': 3 if character == '^' else 1,
                    'turn': 0
                })
                tracks[i][j] = '|'
            elif character in ('>', '<'):
                carts.append({
                    'location': (i, j),
                    'direction': 0 if character == '>' else 2,
                    'turn': 0
                })
                tracks[i][j] = '-'
            else:
                tracks[i][j] = character

    print(a(copy.deepcopy(carts), tracks))
    print(b(copy.deepcopy(carts), tracks))
