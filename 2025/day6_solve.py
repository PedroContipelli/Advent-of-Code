import sys, os, math
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]
num_lines = len(lines)
num_grid = []

for row_num in range(num_lines - 1):
  num_grid.append([int(x) for x in lines[row_num].split()])

total = 0
operations = lines[-1].split()

for col, op in enumerate(operations):
  if op == "*":
    product = 1
    for row in range(num_lines - 1):
      product *= num_grid[row][col]
    total += product
  elif op == "+":
    for row in range(num_lines - 1):
      total += num_grid[row][col]

print("Part 1 Answer:", total)

input_file = open(f"day{day}_{input}.txt")
char_grid = [list(line.strip("\n")) for line in input_file]
num_grid = []

for col in range(len(char_grid[0])-1):
  if char_grid[-1][col+1] in "*+":
    for row in range(num_lines-1):
      char_grid[row][col] = '|'

for row_num in range(num_lines-1):
  num_grid.append("".join(char_grid[row_num]).split("|"))

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
for col, op in enumerate(lines[num_lines-1].split()):
  human_nums = [num_grid[row][col] for row in range(num_lines-1)]
  if op == "*":
    total += math.prod(cephalopod_math(human_nums))
  elif op == "+":
    total += sum(cephalopod_math(human_nums))

print("Part 2 Answer:", total)