def readFile():
    file = open('./inputs/day1.txt', 'r')
    pairs = dict({})
    for line in file:
        line = int(line)
        pairs[2020 - line] = line
        if pairs.get(line) is not None:
            print(line * pairs.get(line))


readFile()
