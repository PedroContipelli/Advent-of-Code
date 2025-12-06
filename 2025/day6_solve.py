import sys, os, math
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]
rows = []

for row_num in range(4):
  nums = [int(x) for x in lines[row_num].split()]
  rows.append(nums)

total = 0
for i, op in enumerate(lines[4].split()):
  if op == "*":
    total += rows[0][i] * rows[1][i] * rows[2][i] * rows[3][i]
  elif op == "+":
    total += rows[0][i] + rows[1][i] + rows[2][i] + rows[3][i]

print("Part 1 Answer:", total)

input_file = open(f"day{day}_{input}.txt")
grid = [list(line.strip()) for line in input_file]
rows = []

for c in range(len(grid[0])):
  divider = True
  for r in range(5):
    if grid[r][c] != ' ':
      divider = False
      break
  if divider:
    for r in range(4):
      grid[r][c] = '|'

for row_num in range(4):
  rows.append("".join(grid[row_num]).split("|"))

def cephalopod_math(nums):
  col_nums = []
  digit_index = -1
  while True:
    col_num = ""
    counting = False
    for num in nums:
      if -digit_index - 1 < len(num) and num[digit_index] != " ":
        col_num += str(num)[digit_index]
        counting = True
    if not counting:
      break
    col_nums.append(col_num)
    digit_index -= 1
  return [int(x) for x in col_nums]

total = 0
for i, op in enumerate(lines[4].split()):
  human_nums = [rows[0][i], rows[1][i], rows[2][i], rows[3][i]]
  if op == "*":
    total += math.prod(cephalopod_math(human_nums))
  elif op == "+":
    total += sum(cephalopod_math(human_nums))

print("Part 2 Answer:", total)