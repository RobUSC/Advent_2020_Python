def turn_90_degrees(dir, heading):
    if heading == 'L':
        if dir == 'E':
            return 'N'
        elif dir == 'N':
            return 'W'
        elif dir == 'W':
            return 'S'
        elif dir == 'S':
            return 'E'
    elif heading == 'R':
        if dir == 'E':
            return 'S'
        elif dir == 'S':
            return 'W'
        elif dir == 'W':
            return 'N'
        elif dir == 'N':
            return 'E'


def rotate_waypoint_90_degrees(waypoint, heading):
    if heading == 'L':
        return [-waypoint[1], waypoint[0]]
    else:
        return [waypoint[1], -waypoint[0]]


with open('./inputs/day12.txt', 'r') as input:
    turns = ['L', 'R']
    position = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
    direction = 'E'
    waypoint = [10, 1]
    planar_position = [0, 0]

    for index, line in enumerate(input):
        line = str(line).strip('\n')
        var = line[0]

        if var in turns:
            for i in range(int(int(line[1:]) / 90)):
                waypoint = rotate_waypoint_90_degrees(waypoint, line[0])
                direction = turn_90_degrees(direction, line[0])
        elif var == 'F':
            position[direction] += int(line[1:])
            planar_position[0] += waypoint[0] * int(line[1:])
            planar_position[1] += waypoint[1] * int(line[1:])
        else:
            if var == 'N':
                position['N'] += int(line[1:])
                waypoint[1] += int(line[1:])
            if var == 'E':
                position['E'] += int(line[1:])
                waypoint[0] += int(line[1:])
            if var == 'W':
                position['W'] += int(line[1:])
                waypoint[0] -= int(line[1:])
            if var == 'S':
                position['S'] += int(line[1:])
                waypoint[1] -= int(line[1:])

    print('Part 1', abs((position.get('E') - position.get('W'))) + abs((position.get('N') - position.get('S'))))
    print('Part 2', abs(planar_position[0]) + abs(planar_position[1]))
