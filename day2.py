def readFile():
    file = open('./inputs/day2.txt', 'r')

    matches_part1 = 0
    matches_part2 = 0
    for line in file:
        range1 = line.split('-')
        range2 = range1[1].split(' ')
        criteria = range2[1].split(':')
        value = range2[2]
        # Part 1
        count = 0
        for i in value:
            if i == criteria[0]:
                count = count + 1
        if int(range1[0]) <= count <= int(range2[0]):
            matches_part1 = matches_part1 + 1
        # Part 2
        var1 = value[int(range1[0])-1]
        var2 = (value[int(range2[0])-1])
        if (var1 == criteria[0]) ^ (var2 == criteria[0]):
            matches_part2 = matches_part2 + 1

    print("Matched Part 1: " + str(matches_part1))
    print("Matched Part 2: " + str(matches_part2))


readFile()
