def do_iteration(recipes, elf1, elf2):
    new_recipes = [int(character) for character in str(recipes[elf1] + recipes[elf2])]

    recipes.extend(new_recipes)

    return ((elf1 + 1 + recipes[elf1]) % len(recipes), (elf2 + 1 + recipes[elf2]) % len(recipes))

def a(iterations_text):
    iterations = int(iterations_text)

    recipes = [3, 7]

    elf1 = 0
    elf2 = 1

    while len(recipes) < iterations + 10:
        elf1, elf2 = do_iteration(recipes, elf1, elf2)

    return ''.join(str(recipe) for recipe in recipes[-10:])

def b(final_recipes_text):
    final_recipes = [int(character) for character in final_recipes_text]

    recipes = [3, 7]

    elf1 = 0
    elf2 = 1

    while True:
        elf1, elf2 = do_iteration(recipes, elf1, elf2)

        if recipes[-len(final_recipes):] == final_recipes:
            return len(recipes) - len(final_recipes)
            break

        if recipes[-len(final_recipes) - 1:-1] == final_recipes:
            return len(recipes) - len(final_recipes) - 1
            break

with open('input/14', 'r') as file:
    puzzle_input = file.read().strip()

    print(a(puzzle_input))
    print(b(puzzle_input))
