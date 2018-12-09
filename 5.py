import concurrent.futures

def react(polymer):
    while True:
        any_reactions = False

        for i in range(0, len(polymer) - 1):
            left = polymer[i]
            right = polymer[i + 1]

            same_type = False
            same_polarity = False

            if right.lower() == left.lower():
                same_type = True

                if right == left:
                    same_polarity = True

            if same_type and not same_polarity:
                polymer[i] = '~'
                polymer[i + 1] = '~'

                any_reactions = True

        polymer = [unit for unit in polymer if unit != '~']

        if not any_reactions:
            break

    return len(polymer)

def a(polymer):
    return react(polymer)

def b(polymer):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        to_remove = 'qwertyuiopasdfghjklzxcvbnm'

        results = executor.map(
            react,
            ([unit for unit in polymer if unit.lower() != removed] for removed in to_remove)
        )

        return min(results)

with open('input/5', 'r') as file:
    input = list(''.join(file.read().strip()))

    print(a(input))
    print(b(input))
