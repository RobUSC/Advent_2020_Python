import re

instructions = {}
accumulator = 0
with open('./inputs/day8.txt', 'r') as input:
    for index, line in enumerate(input):
        line = line.strip('\n')
        instructions[index] = [line, True]

    i = 0
    m = re.match(r"(.*) (.*)", instructions.get(i)[0])
    while m:
        prev = i
        if m.group(1) == 'acc':
            accumulator += int(m.group(2))
            i += 1
        elif m.group(1) == 'jmp':
            i += int(m.group(2))
        elif m.group(1) == 'nop':
            i += 1
        if instructions.get(i) is not None and instructions.get(i)[1]:
            instructions[i][1] = False
            m = re.match(r"(.*) (.*)", instructions.get(i)[0])
        elif instructions.get(i) is not None:
            print('Part 1:', accumulator)
            var = instructions[prev][0]
            if var[0:3] == 'jmp':
                var = var.replace('jmp', 'nop')
            else:
                var = var.replace('nop', 'jmp')
            instructions[prev][0] = var
            instructions[prev][1] = True
            i = prev
            m = re.match(r"(.*) (.*)", instructions.get(i)[0])
        else:
            print('Part 2:', accumulator)
            m = False

