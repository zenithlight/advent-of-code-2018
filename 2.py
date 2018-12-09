import collections
import itertools

def a(boxes):
    counters = [collections.Counter(box) for box in boxes]

    number_of_doubles = len(
        [box for box in counters if any(box[key] == 2 for key in box)]
    )
    number_of_triples = len(
        [box for box in counters if any(box[key] == 3 for key in box)]
    )

    return number_of_doubles * number_of_triples

def b(boxes):
    for box1, box2 in itertools.combinations(boxes, 2):
        if len([i for i, j in zip(box1, box2) if i != j]) == 1:
            return ''.join(i for i, j in zip(box1, box2) if i == j)

with open('input/2', 'r') as file:
    input = [line.strip() for line in file]

    print(a(input))
    print(b(input))
