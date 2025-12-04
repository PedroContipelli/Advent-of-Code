import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

grid = [list(line.strip()) for line in input_file]

sum = 0

dR = [-1, -1, -1, 0, 0, 1, 1, 1]
dC = [-1, 0, 1, -1, 1, -1, 0, 1]

def in_bounds(grid, r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[r])

for r in range(len(grid)):
  for c in range(len(grid[r])):
    if grid[r][c] != '@':
      continue
    count = 0
    for i in range(8):
      checkR, checkC = r + dR[i], c + dC[i]
      if in_bounds(grid, checkR, checkC) and grid[checkR][checkC] == '@':
        count += 1
    if count < 4:
      sum += 1

print("Part 1 Answer:", sum)

sum = 0
remove_list = []

while True:
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] != '@':
        continue
      count = 0
      for i in range(8):
        checkR, checkC = r + dR[i], c + dC[i]
        if in_bounds(grid, checkR, checkC) and grid[checkR][checkC] == '@':
          count += 1
      if count < 4:
        remove_list.append((r,c))
        sum += 1
  if remove_list == []:
    break
  for r, c in remove_list:
    grid[r][c] = '.'
  remove_list = []

print("Part 2 Answer:", sum)
