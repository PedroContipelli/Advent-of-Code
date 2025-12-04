import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

input = input_file.readline().strip()

dX = [0, 0, -1, 1]
dY = [1, -1, 0, 0]

houses = set()
x,y = 0,0
houses.add((x,y))

for dir in input:
  i = "^v<>".index(dir)
  x += dX[i]
  y += dY[i]
  houses.add((x,y))

print("Part 1 Answer:", len(houses))

houses = set()
x1,y1,x2,y2 = 0,0,0,0
houses.add((x1,y1))

for index, dir in enumerate(input):
  i = "^v<>".index(dir)
  if index % 2 == 0:
    x1 += dX[i]
    y1 += dY[i]
    houses.add((x1,y1))
  else:
    x2 += dX[i]
    y2 += dY[i]
    houses.add((x2,y2))
    
print("Part 2 Answer:", len(houses))