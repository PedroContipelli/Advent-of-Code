import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]
graph = {}

for line in lines:
  devices = line.split(" ")
  input_device = devices[0][:-1]
  output_devices = devices[1:]
  graph[input_device] = output_devices

def bfs(src, inDegree):
  queue = [src]
  seen = {src}

  while queue:
    current = queue.pop(0)
    for connection in graph.get(current, []):
      inDegree[connection] = inDegree.get(connection, 0) + 1
      if connection not in seen:
        seen.add(connection)
        queue.append(connection)

# Topological sort
def paths_between(src, target):
  inDegree = {src: 0}
  bfs(src, inDegree)

  paths = {src: 1}
  queue = [src]

  while queue:
    current = queue.pop(0)
    for connection in graph.get(current, []):
      paths[connection] = paths.get(connection, 0) + paths[current]
      inDegree[connection] -= 1
      if inDegree[connection] == 0:
        queue.append(connection)

  return paths.get(target, 0)

print("Part 1 Answer:", paths_between("you", "out"))

svr_to_fft = paths_between("svr", "fft")
fft_to_dac = paths_between("fft", "dac")
dac_to_out = paths_between("dac", "out")

print("Part 2 Answer:", svr_to_fft*fft_to_dac*dac_to_out)