import networkx as nx

with open('./inputs/day10.txt', 'r') as input:
    adaptors = {}
    for index, line in enumerate(input):
        line = int(line.strip('\n'))
        adaptors[line] = line

    max = 0
    for k in adaptors:
        if adaptors[k] > max:
            max = adaptors[k]
    adaptors[max + 3] = max + 3
    one_jolt_differences = 0
    three_jolt_differences = 0
    current_jolts = 0
    g = nx.DiGraph

    for i in range(1, max + 3):
        if i > current_jolts:
            if adaptors.get(i) is not None:
                one_jolt_differences += 1
                current_jolts += 1
            elif adaptors.get(i + 1) is not None:
                current_jolts += 2
            elif adaptors.get(i + 2) is not None:
                three_jolt_differences += 1
                current_jolts += 3

    for i in range(1, max + 3):
        if i > current_jolts:
            if adaptors.get(i) is not None:
                g.add_edge(i - 1, i)
            if adaptors.get(i + 1) is not None:
                g.add_edge(i - 2, i)
            if adaptors.get(i + 2) is not None:
                g.add_edge(i - 3, i)

    for g.

    print('Part1: ', one_jolt_differences * three_jolt_differences)
    print('Part2: ', g.predecessors(0,max+3))

