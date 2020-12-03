def readFile():
    file = open('./inputs/day1.txt', 'r')
    pairs = dict({})
    nums = []
    for line in file:
        line = int(line)
        nums.append(line)
        pairs[2020 - line] = line
        if pairs.get(line) is not None:
            print(line * pairs.get(line))
    searching = True
    while searching:
        for i in nums:
            for j in nums:
                for k in nums:
                    if i + j + k == 2020 and searching:
                        print(i * j * k)
                        searching = False


readFile()
