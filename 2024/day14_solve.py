import re
import math
import time

input_file = open("day14_input.txt", "r")

lines = [line.strip() for line in input_file.readlines()]
delimiters = r"[ =,]"
grid_size = (101, 103)
seconds = 100
quadrant_count = [0, 0, 0, 0]

for robot in lines:
    nums = re.split(delimiters, robot)

    p = (int(nums[1]), int(nums[2]))
    v = (int(nums[4]), int(nums[5]))
    move = (p[0] + v[0]*seconds, p[1] + v[1]*seconds)

    col, row = move[0] % grid_size[0], move[1] % grid_size[1]

    half = (grid_size[0] // 2 , grid_size[1] // 2)

    if col < half[0] and row < half[1]:
        quadrant_count[0] += 1
    elif col < half[0] and row > half[1]:
        quadrant_count[1] += 1
    elif col > half[0] and row < half[1]:
        quadrant_count[2] += 1
    elif col > half[0] and row > half[1]:
        quadrant_count[3] += 1

print("Part 1 answer:", math.prod(quadrant_count))

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()
    print("#" * 100)
    print()

# I just watched the animation for a few mins until I spotted the tree. Nothing fancy.
# Tip: zoom out if possible, so the grid stays fixed in your console

for seconds in range(0, 1000000):
    grid = [[" "] * grid_size[0] for _ in range(grid_size[1])]
    for robot in lines:
        nums = re.split(delimiters, robot)

        p = (int(nums[1]), int(nums[2]))
        v = (int(nums[4]), int(nums[5]))
        move = (p[0] + v[0]*seconds, p[1] + v[1]*seconds)

        col, row = move[0] % grid_size[0], move[1] % grid_size[1]
        grid[row][col] = 'X'
    print(seconds)
    print_grid(grid)
    time.sleep(0.01)
