import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

total_connections = 10 if sys.argv[-1] == "--test" else 1000

lines = [line.strip() for line in input_file]
total_boxes = len(lines)

parent = [i for i in range(total_boxes)]

def root(x):
  if parent[x] == x:
    return x
  
  parent[x] = root(parent[x])
  return parent[x]

def union(x, y):
  parent[root(x)] = root(y)

boxes = {}
for i in range(total_boxes):
  boxes[i] = [int(x) for x in lines[i].split(",")]

def dist_squared(box1, box2):
  p1 = boxes[box1]
  p2 = boxes[box2]
  return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

all_pairs = []
for i in range(total_boxes):
    for j in range(i+1, total_boxes):
      all_pairs.append((i,j))

all_pairs.sort(key = lambda pair: dist_squared(pair[0], pair[1]))

for connection in range(total_connections):
  box1, box2 = all_pairs[connection]
  union(box1, box2)

sizes = {}
for i in range(total_boxes):
  circuit = root(i)
  sizes[circuit] = sizes.get(circuit, 0) + 1

totals = sorted(sizes.values())
print("Part 1 Answer:", totals[-1]*totals[-2]*totals[-3])

def all_connected():
  for i in range(total_boxes):
    if root(i) != root(0):
      return False
  return True

for box1, box2 in all_pairs:
  union(box1, box2)

  if all_connected():
    print("Part 2 Answer:", boxes[box1][0] * boxes[box2][0])
    break