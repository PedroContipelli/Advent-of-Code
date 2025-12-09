import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]
red_tiles = []

for red_tile in lines:
  red_tiles.append([int(x) for x in red_tile.split(",")])

def area(corner1, corner2):
  x1, y1 = corner1
  x2, y2 = corner2
  return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

max_area = 0

for i in range(len(red_tiles)):
  for j in range(i+1, len(red_tiles)):
    max_area = max(max_area, area(red_tiles[i], red_tiles[j]))

print("Part 1 Answer:", max_area)

# Part 2 Solution: plot and analyze manually lol

# import matplotlib.pyplot as plt

# xs = [p[0] for p in red_tiles]
# ys = [p[1] for p in red_tiles]

# plt.plot(xs, ys, marker='o')
# plt.grid(True)
# plt.show()

# After some thinking, the largest contained rectange will have one
# corner at one of the inner mouth corners of the "pacman" shape plot.

# Inner Pacman Mouth (bottom point): (94693,48547)
# Look for opposite point above Y=32338 to ensure contained rectangle
# Corner: (5030,33077)
# print("Part 2 Answer:", area((94693,48547), (5030,33077)))
# Submission Incorrect (Advent of Code tells us answer is too low). So we know it's > 1,387,191,744

# Inner Pacman Mouth (top point): (94693,50233)
# Look for opposite point below Y=69349 to ensure contained rectangle
# Corner: (5570,68792)
print("Part 2 Answer:", area((94693,50233), (5570,68792)))
# Correct! (Honestly... kind of amazed this worked)