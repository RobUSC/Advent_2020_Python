def factor_of(num, offset):
    if num % offset == 0:
        return True
    else:
        return False


def convert_to_time(number):
    hour = int(number / 60)
    minute = number % 60
    return int(hour + minute)


with open('./inputs/day13.txt', 'r') as input:
    # input = [939, [7, 13, 'x', 'x', 59, 'x', 31, 19]]

    depart_time = 0
    buses = []
    for index, line in enumerate(input):
        line = str(line).strip('\n')
        if index == 0:
            depart_time = line
        if index == 1:
            for item in line.strip('[').strip(']').strip("'").strip(' ').split(','):
                buses.append(item)

    bus_depart_time = {}
    for bus in buses:
        bus = bus.strip(' ').strip("'")
        if bus.isnumeric():
            bus = int(bus)
            bus_depart_time[bus] = 0
            while convert_to_time(int(bus_depart_time[bus]) < int(depart_time)):
                bus_depart_time[bus] += int(bus)

    searching = True
    i = 0
    while searching:
        for k in bus_depart_time:
            if int(bus_depart_time[k]) == i + int(depart_time):
                print('Part 1:', int(k) * i)
                searching = False
        i += 1

    bus_map = {}
    for idx, x in enumerate(buses):
        x = str(x).strip(' ')
        if x != 'x':
            bus_map[int(x)] = idx

    searching = True
    i = 0
    step = 1
    for k in bus_map:
        while (i + int(bus_map.get(k))) % k != 0:
            i += step
        step *= k
    print('Part2:', i)

