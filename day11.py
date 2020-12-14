def all_adjacent(grid, row, column, occupied):
    var = 0
    if row > 0 and column > 0:
        if grid[row - 1][column - 1][0] in occupied:
            var += 1
    if row > 0:
        if grid[row - 1][column][0] in occupied:
            var += 1
    if row > 0 and column < len(grid[0]) - 1:  # TR
        if grid[row - 1][column + 1][0] in occupied:
            var += 1
    if column > 0:
        if grid[row][column - 1][0] in occupied:
            var += 1
    if column < len(grid[0]) - 1:
        if grid[row][column + 1][0] in occupied:
            var += 1
    if len(grid) - 1 > row and column > 0:
        if grid[row + 1][column - 1][0] in occupied:
            var += 1
    if row < len(grid) - 1:
        if grid[row + 1][column][0] in occupied:
            var += 1
    if row < len(grid) - 1 and column < len(grid[0]) - 1:
        if grid[row + 1][column + 1][0] in occupied:
            var += 1
    return var


def eval_seats(grid):
    seats_to_fill = []
    seats_to_empty = []
    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            if not column[0] == '.':
                var = all_adjacent(grid, row_index, column_index, '#')
                if column == 'L' and var == 0:
                    seats_to_fill.append([row_index, column_index])
                elif var >= 4:
                    seats_to_empty.append([row_index, column_index])

    for seat in seats_to_fill:
        grid[seat[0]][seat[1]] = '#'
    for seat in seats_to_empty:
        grid[seat[0]][seat[1]] = 'L'


def init_seats(input):
    seat_grid = []
    for index, line in enumerate(input):
        seat_grid.append([])
        line = str(line).strip('\n')

        for column, c in enumerate(line):
            seat_grid[index].append([])
            seat_grid[index][column] = c
    return seat_grid


with open('./inputs/day11.txt', 'r') as input:
    seats = init_seats(input)

    for i in range(0, 5):
        eval_seats(seats)

    count = 0
    for row in seats:
        for column in row:
            for seat in column:
                if seat == '#':
                    count += 1

    print(count)
