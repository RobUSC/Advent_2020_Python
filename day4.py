import re

def valid_field(field, value):
    if field == 'byr':
        return 1920 <= int(value) <= 2002
    if field == 'iyr':
        return 2010 <= int(value) <= 2020
    if field == 'eyr':
        return 2020 <= int(value) <= 2030
    if field == 'hgt':
        return re.search(
            '^[1][5-8][0-9]cm$|^[1][9][0-3]cm$|^59in$|^[6][0-9]in$|^[7][0-6]in$', value)
    if field == 'hcl':
        return re.search('#([a-f]|[0-9]){6}', value)
    if field == 'ecl':
        return any(elem == value for elem in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    if field == 'pid':
        return re.search('[0-9]{9}', value)
    if field == 'cid':
        return True
    return False


def read_file():
    file = open('./inputs/day4.txt', 'r')

    valid_passport_count = 0
    validated_passport_count = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    presented_fields = []
    validated_presented_fields = []
    for line in enumerate(file.read().split('\n\n')):
        if line == '\n':
            if all(item in presented_fields for item in required_fields):
                valid_passport_count += 1
            if all(item in validated_presented_fields for item in required_fields):
                validated_passport_count += 1
            else:
                print(validated_presented_fields)
            presented_fields = []
            validated_presented_fields = []
        else:
            var = line.split(' ')
            for item in var:
                field = item.split(':')
                presented_fields.append(field[0])
                if valid_field(field[0], field[1].strip('\n')):
                    validated_presented_fields.append(field[0])
    print('Part 1:', valid_passport_count)
    print('Part 2:', validated_passport_count)



read_file()


# import re
#
# def part_1(data, regexes):
#     return sum(1 for pp in data if all(re.search(reg[1:4], pp) for reg in regexes))
#
# def part_2(data, regexps):
#     return sum(1 for pp in data if all(re.search(reg, pp) for reg in regexps))
#
# def main():
#     d = open('./inputs/day4.txt').read().split('\n\n')
#     regexes = [r'(byr:(19[2-8][0-9]|199[0-9]|200[0-2]))',
#                r'(iyr:(201[0-9]|2020))',
#                r'(eyr:(202[0-9]|2030))',
#                r'(hgt:(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)',
#                r'(hcl:#([0-9]|[a-f]){6})',
#                r'(ecl:(amb|blu|brn|gry|grn|hzl|oth))',
#                r'(pid:\d{9}(?!\S))']
#
#     print(part_1(d, regexes))
#     print(part_2(d, regexes))
#
#
# if __name__ == '__main__':
#     main()