import copy
input_file = open("day6_input.txt", "r")

lines = [list(line.strip()) for line in input_file.readlines()]

for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == "^":
            guard_start = guard = (r, c)

map = copy.deepcopy(lines)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_i = 0

def inbounds(row, col):
    return 0 <= row < len(map) and 0 <= col < len(map[row])

while inbounds(guard[0], guard[1]):
    map[guard[0]][guard[1]] = 'X'

    next_row = guard[0] + directions[dir_i][0]
    next_col = guard[1] + directions[dir_i][1]

    if inbounds(next_row, next_col) and map[next_row][next_col] == '#':
        dir_i = (dir_i + 1) % 4
    else:
        guard = (next_row, next_col)

path_count = 0

for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] == "X":
            path_count += 1

print("Part 1 answer:", path_count)

loop_obstacle_count = 0

map = copy.deepcopy(lines)

def is_loop():
    count = 0
    global guard, dir_i
    guard = guard_start
    dir_i = 0
    while inbounds(guard[0], guard[1]):
        next_row = guard[0] + directions[dir_i][0]
        next_col = guard[1] + directions[dir_i][1]

        if inbounds(next_row, next_col) and map[next_row][next_col] == '#':
            dir_i = (dir_i + 1) % 4
        else:
            guard = (next_row, next_col)

        # Too lazy to check for loops the proper way, so just assume loop if no exit after 10k steps
        if (count := count + 1) >= 10_000:
            return True

    return False


for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] == ".":
            map[r][c] = "#"

            if is_loop():
                loop_obstacle_count += 1

            map[r][c] = "."







print("Part 2 answer:", loop_obstacle_count)
