import copy
input_file = open("day15_input.txt", "r")

grid = []
moves = []
reading_grid = True

for line in input_file.readlines():
    if line == '\n':
        reading_grid = False
        continue

    if reading_grid:
        grid.append(list(line.strip()))
    else:
        moves.append(list(line.strip()))

grid_copy = copy.deepcopy(grid)

def find_robot():
    global robot
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '@':
                robot = (r,c)

find_robot()

# UP, RIGHT, DOWN, LEFT aka North, East, South, West
dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]
symbols = "^>v<"

def apply_move(dir):
    global robot
    push_boxes = 0
    checkR, checkC = robot[0], robot[1]

    while True:
        checkR += dR[dir]
        checkC += dC[dir]

        if grid[checkR][checkC] == '#':
            break
        elif grid[checkR][checkC] == '.':
            # Move robot
            grid[robot[0]][robot[1]] = '.'
            robot = (robot[0] + dR[dir], robot[1] + dC[dir])
            grid[robot[0]][robot[1]] = '@'

            # Minor optimization here: just set last box directly
            if push_boxes > 0:
                grid[checkR][checkC] = 'O'
            break

        push_boxes += 1

def apply_all_moves():
    for row in moves:
        for move in row:
            dir = symbols.find(move)
            apply_move(dir)

apply_all_moves()

def sum_gps_coords(box_char):
    sum_coords = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == box_char:
                sum_coords += 100*r + c
    return sum_coords

print("Part 1 answer:", sum_gps_coords('O'))

# PART 2
grid = grid_copy

for i, row in enumerate(grid):
    wide_row = []
    for tile in row:
        if tile == '#':
            wide_row += ['#', '#']
        elif tile == 'O':
            wide_row += ['[', ']']
        elif tile == '.':
            wide_row += ['.', '.']
        elif tile == '@':
            wide_row += ['@', '.']
    grid[i] = wide_row

find_robot()

'''
Iteration-based approach won't work (ex: complex recursive case below)
.............
......[].....
.[]..[][].#..
..[][]..[]...
..#[].##.[]..
....[]..[]...
.....[][]....
......[].....
......@......
Move UP from here
'''

# Depth-first search: backpropagate whether push in front was successful
def attempt_vertical_push(boxes, row, dir):
    global robot

    # Base Case #1: Nothing in front of us
    if not boxes:
        return True

    new_boxes = set()
    new_row = row + dR[dir]

    for box in boxes:
        for c in range(box[0], box[1]):
            # Base Case #2: Wall preventing push
            if grid[new_row][c] == '#':
                return False

            if grid[new_row][c] == '[':
                new_boxes.add((c,c+2))
            elif grid[new_row][c] == ']':
                new_boxes.add((c-1,c+1))

    # If boxes in front were successfully pushed (or nothing to push)
    if attempt_vertical_push(new_boxes, new_row, dir):
        # Push current boxes/robot
        for box in boxes:
            for c in range(box[0], box[1]):
                if grid[row][c] == '@':
                    robot = (new_row, c)
                grid[new_row][c] = grid[row][c]
                grid[row][c] = '.'
        # Return successful push
        return True

    # Otherwise (boxes in front failed to push), backpropagate failure
    return False

def apply_move(dir):
    global robot
    checkR, checkC = robot[0], robot[1]

    # LEFT/RIGHT CASE (basically same as part 1)
    if dir % 2 == 1:
        while True:
            checkC += dC[dir]

            if grid[checkR][checkC] == '#':
                break
            # Detect that a move/push is possible
            elif grid[checkR][checkC] == '.':
                # Move boxes/robot over (from end to start)
                for c in range(checkC, robot[1], -dC[dir]):
                    grid[checkR][c] = grid[checkR][c - dC[dir]]

                # Erase robot's last position and update current
                grid[robot[0]][robot[1]] = '.'
                robot = (robot[0], robot[1] + dC[dir])
                break
    # UP/DOWN CASE (DFS)
    else:
        # Initialize push attempt with robot as our first "box"
        row, col = robot
        attempt_vertical_push({(col, col+1)}, row, dir)

apply_all_moves()

print("Part 2 answer:", sum_gps_coords('['))
