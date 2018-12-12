import parse
import collections

WINDOW_PADDING = 2

def get_window(state, center):
    return ''.join([state[i] for i in range(center - WINDOW_PADDING, center + WINDOW_PADDING + 1)])

def print_state(state, left_bound, right_bound):
    print(''.join([state[i] for i in range(left_bound, right_bound)]))

def a(initial_state, mappings):
    state = collections.defaultdict(lambda: '.')
    for i, character in enumerate(initial_state):
        state[i] = character

    left_bound = 0 - WINDOW_PADDING
    right_bound = len(initial_state) + WINDOW_PADDING

    for _ in range(20):
        new_state = collections.defaultdict(lambda: '.')

        for i in range(left_bound, right_bound):
            new_state[i] = mappings[get_window(state, i)]

        state = new_state

        left_bound -= WINDOW_PADDING
        right_bound += WINDOW_PADDING

    return sum(i for i in range(left_bound, right_bound) if state[i] == '#')

# i found a pattern, dependent on my input
def b():
    return int(1739 + (20 * (50000000000 - 304) / 4))

with open('input/12', 'r') as file:
    lines = file.readlines()

    initial_state = parse.parse('initial state: {}', lines[0])[0]

    mappings = {}
    for line in lines[2:]:
        input, output = parse.parse('{} => {}', line)
        mappings[input] = output

    print(a(initial_state, mappings))
    print(b())
