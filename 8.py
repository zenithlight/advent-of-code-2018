def get_tree(i, items, simple_checksum):
    total = 0
    children = []

    children_remaining = items[i]
    i += 1
    metadata_remaining = items[i]
    i += 1

    for child in range(children_remaining):
        new_i, child_total = get_tree(i, items, simple_checksum)
        i = new_i
        children.append(child_total)

    if simple_checksum or children_remaining == 0:
        total += sum(children)
        total += sum(items[i:i + metadata_remaining])
    else:
        for entry in items[i:i + metadata_remaining]:
            if entry <= children_remaining:
                total += children[entry - 1]

    return (i + metadata_remaining, total)

def a(items):
    return(get_tree(0, items, True)[1])

def b(items):
    return(get_tree(0, items, False)[1])

with open('input/8', 'r') as file:
    items = [int(item) for item in file.read().strip().split(' ')]

    print(a(items))
    print(b(items))
