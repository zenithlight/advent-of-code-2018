import parse

def update_points(points):
    return [update_point(point) for point in points]

def update_point(point):
    return (point[0] + point[2], point[1] + point[3], point[2], point[3])

def get_bounds(points):
    x_positions = [point[0] for point in points]
    y_positions = [point[1] for point in points]

    return (min(x_positions), max(x_positions), min(y_positions), max(y_positions))

def get_area(bounds):
    return (bounds[1] - bounds[0]) * (bounds[3] - bounds[2])

def print_points(points):
    min_x, max_x, min_y, max_y = get_bounds(points)

    width = max_x - min_x
    height = max_y - min_y

    grid = []
    for i in range(height + 1):
        row = ['.' for _ in range(width + 1)]
        grid.append(row)

    for point in points:
        x = (point[0]) - min_x
        y = (point[1]) - min_y

        grid[y][x] = '#'

    for row in grid:
        print(''.join(row))

def solve(points):
    test_points = points[:]

    last_area = get_area(get_bounds(test_points))
    iterations = 0
    while True:
        iterations += 1
        test_points = update_points(test_points)

        if get_area(get_bounds(test_points)) > last_area:
            break

        last_area = get_area(get_bounds(test_points))

    iterations -= 1

    for i in range(iterations):
        points = update_points(points)

    print('Part A solution:')
    print_points(points)
    print()
    print(f'Part B solution: {iterations}')

with open('input/10', 'r') as file:
    points = []

    for line in file:
        points.append(parse.parse('position=<{:d},{:d}>velocity=<{:d},{:d}>', line.replace(' ', '')))

    solve(points)
