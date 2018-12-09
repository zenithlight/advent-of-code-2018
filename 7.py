import collections
import parse

def get_available_tasks(starters, required_by, provided_by, visited):
    available = set(starters)

    for step in visited:
        available.update(provided_by[step])

    available -= visited

    to_remove = set()
    for step in available:
        if not all(requirement in visited for requirement in required_by[step]):
            to_remove.add(step)
    available -= to_remove

    return available

def get_step_duration(step):
    return 61 + ('ABCDEFGHIJKLMNOPQRSTUVWXYZ').index(step)

def a(steps):
    required_by = collections.defaultdict(list)
    provided_by = collections.defaultdict(list)

    for step in steps:
        required_by[step[1]].append(step[0])
        provided_by[step[0]].append(step[1])

    starters = sorted([step for step in provided_by if len(required_by[step]) == 0])

    answer = starters[0]
    visited = {starters[0]}

    while True:
        available = get_available_tasks(starters, required_by, provided_by, visited)

        if len(available) == 0:
            break

        next_step = sorted(list(available))[0]

        answer += next_step
        visited.add(next_step)

    return answer

def b(steps):
    worker_times = [0, 0, 0, 0, 0]
    worker_tasks = [None, None, None, None, None]

    required_by = collections.defaultdict(list)
    provided_by = collections.defaultdict(list)

    for step in steps:
        required_by[step[1]].append(step[0])
        provided_by[step[0]].append(step[1])

    starters = sorted([step for step in provided_by if len(required_by[step]) == 0])

    total_time = -1
    visited = set()

    while True:
        for i, time in enumerate(worker_times):
            if time <= 0:
                if worker_tasks[i] is not None:
                    visited.add(worker_tasks[i])
                    worker_tasks[i] = None

                available = get_available_tasks(starters, required_by, provided_by, visited)
                processed_next_steps = sorted(list(available - set(worker_tasks)))
                if len(processed_next_steps) > 0:
                    next_step = processed_next_steps[0]

                    worker_times[i] = get_step_duration(next_step)
                    worker_tasks[i] = next_step

        print(total_time, worker_tasks, worker_times)

        if len(get_available_tasks(starters, required_by, provided_by, visited)) == 0:
            break

        worker_times = [time - 1 for time in worker_times]
        total_time += 1

    return total_time

with open('input/7', 'r') as file:
    input = []
    for line in file:
        result = parse.parse('Step {} must be finished before step {} can begin.', line)
        input.append(tuple(result))

    print(a(input))
    print(b(input))
