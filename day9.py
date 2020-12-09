def get_sums(num_list):
    sums = []
    for i in num_list:
        for k in num_list:
            sums.append(int(i) + int(k))
    return sums


def find_weakness_chain(num_list=[], number_to_sum=0, num_range=[]):
    for i in num_list:
        num_range.append(i)
        range_sum = sum(num_range)
        if range_sum == int(number_to_sum) and len(num_range) > 1:
            num_range.sort()
            print('Part 2:', int(num_range.pop(0)) + int(num_range.pop(-1)))
        if range_sum > int(number_to_sum):
            num_list.pop(0)
            return find_weakness_chain(num_list, number_to_sum, [])


with open('./inputs/day9.txt', 'r') as input:
    preamble = []
    full_list = []
    searching = True
    encryption_weakness = 0
    for index, line in enumerate(input):
        line = str(line).strip('\n')

        if len(preamble) == 25 and searching:
            var = get_sums(preamble)
            if not int(line) in var:
                print('Part1:', line, 'at index', index, 'not in', var)
                searching = False
                encryption_weakness = line
            else:
                preamble.pop(0)
        preamble.append(line)
        full_list.append(int(line))
    find_weakness_chain(full_list, encryption_weakness)
