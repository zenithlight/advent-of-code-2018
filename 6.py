import collections

def get_extents(coordinates):
    min_x = min(coordinate[0] for coordinate in coordinates)
    max_x = max(coordinate[0] for coordinate in coordinates)
    min_y = min(coordinate[1] for coordinate in coordinates)
    max_y = max(coordinate[1] for coordinate in coordinates)

    return (min_x, max_x, min_y, max_y)

def get_manhattan_distance(coordinate1, coordinate2):
    return abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])

def get_nearest_cell_counts(min_x, max_x, min_y, max_y, coordinates):
    counter = collections.Counter()

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            coordinate1 = (x, y)

            shortest_distance = (max_x - min_x) + (max_y - min_y)
            nearest_coordinate = None
            doubled = False # this point is closes to 2 coordinates

            for i, coordinate2 in enumerate(coordinates):
                manhattan_distance = get_manhattan_distance(coordinate1, coordinate2)

                if manhattan_distance < shortest_distance:
                    doubled = False
                    shortest_distance = manhattan_distance
                    nearest_coordinate = i
                elif manhattan_distance == shortest_distance:
                    doubled = True

            if not doubled:
                counter[nearest_coordinate] += 1

    return counter

def a(coordinates):
    min_x, max_x, min_y, max_y = get_extents(coordinates)

    counts1 = get_nearest_cell_counts(min_x, max_x, min_y, max_y, coordinates)
    counts2 = get_nearest_cell_counts(min_x - 50, max_x + 50, min_y - 50, max_y + 50, coordinates)

    return max(counts1[coordinate] for coordinate in counts1 if counts1[coordinate] == counts2[coordinate])

def b(coordinates):
    SAFE_DISTANCE = 10000

    min_x, max_x, min_y, max_y = get_extents(coordinates)

    number_of_safe_cells = 0
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            coordinate1 = (x, y)

            total_distance = 0
            for coordinate2 in coordinates:
                total_distance += get_manhattan_distance(coordinate1, coordinate2)

            if total_distance < SAFE_DISTANCE:
                number_of_safe_cells += 1

    return number_of_safe_cells

with open('input/6', 'r') as file:
    input = []

    for line in file:
        split_line = line.split(', ')
        input.append((int(split_line[0]), int(split_line[1])))

    print(a(input))
    print(b(input))
