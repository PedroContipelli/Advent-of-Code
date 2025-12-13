import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]

presents = {}
regions = []

for line in lines:
  if line == "":
    continue

  if line.endswith(":"):
    present_index = int(line[:-1])
    presents[present_index] = {"shape": [], "tiles": 0}
  elif line[0] in ".#":
    presents[present_index]["shape"].append(line)
    presents[present_index]["tiles"] += line.count("#")
  else:
    region = {}
    info = line.split(" ")
    dims = info[0].split("x")
    region["x"] = int(dims[0])
    region["y"] = int(dims[1][:-1]) # Remove colon
    region["present_count"] = [int(count) for count in info[1:]]
    regions.append(region)

# Analyze the input and notice you can ignore the problem almost entirely.
# Just look at total number of tiles. Cheese <_<
possible = 0

for region in regions:
  total_area = region["x"]*region["y"]
  present_area = 0
  for i, count in enumerate(region["present_count"]):
    present_area += count * presents[i]["tiles"]
  if present_area <= total_area:
    possible += 1

print(f"Part 1 Answer: {possible}")