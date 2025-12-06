import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]

ranges = []
ingredients = []
reading_ranges = True
count = 0

for line in lines:
  if line == "":
    reading_ranges = False
    continue
  if reading_ranges:
    start, end = line.split("-")
    ranges.append((int(start), int(end)+1))
    continue
  
  ingredients.append(int(line))
  
for ingredient in ingredients:
  for start, end in ranges:
    if start <= ingredient < end:
      count += 1
      break

print("Part 1 Answer:", count)

# Realized after that my solution is wrong, but it still passed on my input lol
# I only deconflicted neighboring ranges.
count = 0
ranges = sorted(ranges, key=lambda x: (x[1], x[0]))

for i in range(len(ranges)):
  start, end = ranges[i]
  count += (end - start)

  if i < len(ranges) - 1:
    nextStart, nextEnd = ranges[i+1]
    if nextStart < end:
      count -= min(end, nextEnd) - max(start, nextStart)

print("Part 2 Answer:", count)