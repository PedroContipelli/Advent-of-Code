import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]

sum = 0

for line in lines:
  sides = [int(side) for side in line.strip().split("x")]
  sides.sort()
  surface_area = 2*(sides[0]*sides[1] + sides[0]*sides[2] + sides[1]*sides[2])
  smallest_side = sides[0]*sides[1]
  sum += surface_area + smallest_side

print("Part 1 Answer:", sum)

sum = 0

for line in lines:
  sides = [int(side) for side in line.strip().split("x")]
  sides.sort()
  smallest_perimeter = 2*(sides[0]+sides[1])
  volume = sides[0]*sides[1]*sides[2]
  sum += smallest_perimeter + volume

print("Part 2 Answer:", sum)
