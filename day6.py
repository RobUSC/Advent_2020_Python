file = open('./inputs/day6.txt', 'r')
answers = {}
group_total = 0
unanimous_group_total = 0
for line in file.read().split('\n\n'):
    responders_count = 0
    for c in line:
        if c != '\n':
            answers[c] = answers.get(c, 0) + 1
    responders_count = len(line.split('\n'))
    for k in answers:
        if answers.get(k) >= responders_count:
            unanimous_group_total += 1
    group_total += len(answers)
    answers = {}
print('Part1:', group_total)
print('Part2:', unanimous_group_total)
