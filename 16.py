import collections
import parse

def addr(registers, a, b, c):
    result = registers[:]

    result[c] = result[a] + result[b]

    return result

def addi(registers, a, b, c):
    result = registers[:]

    result[c] = result[a] + b

    return result

def mulr(registers, a, b, c):
    result = registers[:]

    result[c] = result[a] * result[b]

    return result

def muli(registers, a, b, c):
    result = registers[:]

    result[c] = result[a] * b

    return result

def banr(registers, a, b, c):
    result = registers[:]

    result[c] = result[a] & result[b]

    return result

def bani(registers, a, b, c):
    result = registers[:]

    result[c] = result[a] & b

    return result

def borr(registers, a, b, c):
    result = registers[:]

    result[c] = result[a] | result[b]

    return result

def bori(registers, a, b, c):
    result = registers[:]

    result[c] = result[a] | b

    return result

def setr(registers, a, b, c):
    result = registers[:]

    result[c] = result[a]

    return result

def seti(registers, a, b, c):
    result = registers[:]

    result[c] = a

    return result

def gtir(registers, a, b, c):
    result = registers[:]

    result[c] = int(a > registers[b])

    return result

def gtri(registers, a, b, c):
    result = registers[:]

    result[c] = int(registers[a] > b)

    return result

def gtrr(registers, a, b, c):
    result = registers[:]

    result[c] = int(registers[a] > registers[b])

    return result

def eqir(registers, a, b, c):
    result = registers[:]

    result[c] = int(a == registers[b])

    return result

def eqri(registers, a, b, c):
    result = registers[:]

    result[c] = int(registers[a] == b)

    return result

def eqrr(registers, a, b, c):
    result = registers[:]

    result[c] = int(registers[a] == registers[b])

    return result

operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def a(experiments):
    chunks = [experiments[i:i + 4] for i in range(0, len(experiments), 4)]

    total = 0
    for chunk in chunks:
        before = list(parse.parse('Before: [{:d}, {:d}, {:d}, {:d}]', chunk[0]))
        instruction = [int(item) for item in chunk[1].split(' ')]
        after = tuple(parse.parse('After:  [{:d}, {:d}, {:d}, {:d}]', chunk[2]))

        results = collections.Counter()

        for operation in operations:
            result = tuple(operation(before, *instruction[-3:]))
            results[result] += 1

        if results[after] >= 3:
            total += 1

    return total

def b(experiments, test_program):
    chunks = [experiments[i:i + 4] for i in range(0, len(experiments), 4)]

    possible_operations = {
        opcode: set(operations)
        for opcode in range(0, 16)
    }

    while any(len(possible_operations[opcode]) > 1 for opcode in range(0, 16)):
        for chunk in chunks:
            before = list(parse.parse('Before: [{:d}, {:d}, {:d}, {:d}]', chunk[0]))
            instruction = [int(item) for item in chunk[1].split(' ')]
            after = tuple(parse.parse('After:  [{:d}, {:d}, {:d}, {:d}]', chunk[2]))

            opcode = instruction[0]
            arguments = instruction[-3:]

            operations_to_remove = set()

            for operation in possible_operations[opcode]:
                result = tuple(operation(before, *arguments))

                if result != after:
                    operations_to_remove.add(operation)

            possible_operations[opcode] -= operations_to_remove

            if len(possible_operations[opcode]) == 1:
                remaining_operation = next(iter(possible_operations[opcode]))

                for other_opcode in range(0, 16):
                    if opcode != other_opcode and remaining_operation in possible_operations[other_opcode]:
                        possible_operations[other_opcode].remove(remaining_operation)

    mappings = {}
    for opcode in range(0, 16):
        mappings[opcode] = possible_operations[opcode].pop()

    registers = [0, 0, 0, 0]

    for line in test_program:
        print(registers)
        instruction = [int(item) for item in line.split(' ')]

        opcode = instruction[0]
        arguments = instruction[-3:]

        registers = mappings[opcode](registers, *arguments)

    return registers[0]

with open('input/16a', 'r') as file:
    experiments = file.readlines()

    print(a(experiments))

    with open('input/16b', 'r') as file2:
        test_program = file2.readlines()

        print(b(experiments, test_program))
