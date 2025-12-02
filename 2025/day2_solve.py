import sys
input = "input" if sys.argv[-1] != "--test" else "testcase"
input_file = open(f"day2_{input}.txt", "r")

all = input_file.readline().strip().split(",")

def is_invalid(id):
  if len(id) % 2 != 0:
    return False
  half = len(id) // 2
  return id[:half] == id[half:]

sum = 0

for id_range in all:
  start, end = id_range.split("-")
  for num in range(int(start), int(end)+1):
    if is_invalid(str(num)):
      sum += num

print("Part 1 Answer:", sum)

def is_invalid_2(id):
  for pattern_len in range(1, len(id)//2 + 1):
    pattern = id[:pattern_len]
    found = True
    for i in range(0, len(id), pattern_len):
      if id[i:i+pattern_len] != pattern:
        found = False
        break
    if found:
      return True
  return False

sum = 0

for id_range in all:
  start, end = id_range.split("-")
  for num in range(int(start), int(end)+1):
    if is_invalid_2(str(num)):
      sum += num

print("Part 2 Answer:", sum)
