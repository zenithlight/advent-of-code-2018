def a(frequencies):
    return sum(frequencies)

def b(frequencies):
    current = 0
    seen = set()

    revisited = False
    while True:
        for frequency in frequencies:
            current += frequency

            if current in seen:
                revisited = True
                break

            seen.add(current)

        if revisited:
            break

    return current

with open('input/1', 'r') as file:
    input = [int(number) for number in file]

    print(a(input))
    print(b(input))
