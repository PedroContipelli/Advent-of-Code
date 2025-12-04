import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

instructions = input_file.readline().strip()
floor = 0

for instruction in instructions:
  if instruction == "(":
    floor += 1
  elif instruction == ")":
    floor -= 1

print("Part 1 Answer:", floor)

floor = 0
first_basement_index = 0

for position, instruction in enumerate(instructions):
  if instruction == "(":
    floor += 1
  elif instruction == ")":
    floor -= 1
  if floor == -1:
    first_basement_index = position+1
    break

print("Part 2 Answer:", first_basement_index)
