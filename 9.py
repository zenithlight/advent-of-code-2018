import collections
import blist
import parse

def a(number_of_players, last_marble):
    scores = collections.Counter()

    circle = blist.blist([0, 1])
    current = 1

    for i in range(2, last_marble):
        if i % 23 == 0:
            player = i % number_of_players

            scores[player] += i

            to_remove = (current - 7) % len(circle)
            scores[player] += circle[to_remove]

            del circle[to_remove]
            current = to_remove
        else:
            insert_after = (current + 1) % len(circle)

            circle.insert(insert_after + 1, i)
            current = insert_after + 1

    return scores.most_common()[0][1]

def b(number_of_players, last_marble):
    return a(number_of_players, last_marble * 100)

with open('input/9', 'r') as file:
    number_of_players, last_marble = parse.parse('{} players; last marble is worth {} points', file.read().strip())

    print(a(int(number_of_players), int(last_marble)))
    print(b(int(number_of_players), int(last_marble)))
