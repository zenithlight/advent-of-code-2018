import collections
import concurrent.futures
import itertools
import numpy

WIDTH = 300
HEIGHT = 300

def get_grid(width, height):
    grid = numpy.ndarray((300, 300))

    points = itertools.product(range(WIDTH), range(HEIGHT))
    for point in points:
        rack_id = point[0] + 10
        power_level = rack_id * point[1]
        power_level += serial_number
        power_level *= rack_id
        power_level = (power_level // 100) % 10
        power_level -= 5

        grid[point] = power_level

    return grid

def get_area_value(top_left_corner, grid, area_width, area_height):
    x, y = top_left_corner
    return sum(sum(grid[x:x + area_width, y:y + area_height]))

def scan(grid, area_width, area_height):
    results = {}

    for point in itertools.product(range(WIDTH - area_width), range(HEIGHT - area_height)):
        results[(*point, area_width)] = get_area_value(point, grid, area_width, area_height)

    return results

def a(serial_number):
    area_width = 3
    area_height = 3

    grid = get_grid(WIDTH, HEIGHT)

    points = itertools.product(range(WIDTH - area_width), range(HEIGHT - area_height))

    results = collections.Counter({
        point: get_area_value(point, grid, area_width, area_height)
        for point in points
    })

    return ','.join(map(str, results.most_common()[0][0]))

def b(serial_number):
    grid = get_grid(WIDTH, HEIGHT)

    results = collections.Counter()

    def callback(future):
        results.update(future.result())

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for area_width in range(1, min(WIDTH, HEIGHT) + 1):
            area_height = area_width

            future = executor.submit(scan, grid, area_width, area_height)
            future.add_done_callback(callback_generator(area_width))

    return ','.join(map(str, results.most_common()[0][0]))

with open('input/11', 'r') as file:
    serial_number = int(file.read().strip())

    print(a(serial_number))
    print(b(serial_number))
