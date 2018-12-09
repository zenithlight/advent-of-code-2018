import collections
import math
import sys
import itertools
import parse

WIDTH = 1000
HEIGHT = 1000

def get_region(x, y, w, h):
    return itertools.product(range(x, x + w), range(y, y + h))

def claim_region(region, fabric):
    for coordinate in region:
        fabric[coordinate] += 1

def get_fabric(claims):
    fabric = collections.Counter()

    for claim in claims:
        region = get_region(*claim[1:])
        claim_region(region, fabric)

    return fabric

def count_contested_coordinates(region, fabric):
    return len([coordinate for coordinate in region if fabric[coordinate] >= 2])

def check_region(region, fabric):
    return all(fabric[coordinate] == 1 for coordinate in region)

def a(claims):
    fabric = get_fabric(claims)
    return count_contested_coordinates(get_region(0, 0, WIDTH, HEIGHT), fabric)

def b(claims):
    fabric = get_fabric(claims)

    for claim in claims:
        if check_region(get_region(*claim[1:]), fabric):
            return claim[0]

with open('input/3', 'r') as file:
    parser = parse.compile('#{:d} @ {:d},{:d}: {:d}x{:d}')
    input = [list(parser.parse(line)) for line in file]

    print(a(input))
    print(b(input))
