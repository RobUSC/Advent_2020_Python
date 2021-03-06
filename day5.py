def calc_pos(line, idx, op, hi, lo):
    mid = int((hi + lo) / 2)
    if op in 'BR':
        lo = mid + 1
    if op in 'FL':
        hi = mid
    if hi == lo:
        return hi
    return int(calc_pos(line, idx + 1, line[idx + 1], hi, lo))


def find_seat(seats):
    for i in range(0, 1000):
        up = max(i + 1, 0)
        down = max(i - 1, 0)
        if seats.get(up) is not None and seats.get(down) is not None and seats.get(i) is None:
            print('My seat', i)


file = open('./inputs/day5.txt', 'r')
max_seat = 0
seats = {}
for line in file:
    var3 = (int(calc_pos(line, 0, line[0], 127, 0)) * 8 + int(calc_pos(line, 7, line[7], 7, 0)))
    seats[var3] = var3
    if max_seat < var3:
        max_seat = var3

print(max_seat)
find_seat(seats)
