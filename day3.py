def read_file():
    file = open('./inputs/day3.txt', 'r')
    criteria = '#'
    trees_encountered_map = {1: [[1, 0, 0], [2, 0, 0]], 3: [[1, 0, 0]], 5: [[1, 0, 0]], 7: [[1, 0, 0]]}
    for index, line in enumerate(file.readlines()):
        length_of_tree_pattern = len(line) - 1
        for k in trees_encountered_map:
            for v in trees_encountered_map[k]:
                if index % v[0] == 0:
                    if line[v[1]] == criteria:
                        v[2] += 1
                    v[1] = (v[1] + k) % length_of_tree_pattern

    result = 1
    for k in trees_encountered_map:
        for v in trees_encountered_map[k]:
            result *= v[2]
    print(trees_encountered_map)
    print("Part 1:", trees_encountered_map[3][0][2])
    print("Part 2:", result)


read_file()
