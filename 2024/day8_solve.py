input_file = open("day8_input.txt", "r")

grid = [list(line.strip()) for line in input_file.readlines()]
antinodes = set()

def inbounds(row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])

for r1 in range(len(grid)):
    for c1 in range(len(grid[r1])):
        if grid[r1][c1] != ".":
            for r2 in range(len(grid)):
                for c2 in range(len(grid[r2])):
                    if r2*len(grid)+c2 > r1*len(grid)+c1 and grid[r2][c2] == grid[r1][c1]:
                        dR = r2 - r1
                        dC = c2 - c1
                        antinode1 = (r1 - dR, c1 - dC)
                        antinode2 = (r2 + dR, c2 + dC)
                        if (inbounds(*antinode1)):
                            antinodes.add(antinode1)
                        if (inbounds(*antinode2)):
                            antinodes.add(antinode2)

print("Part 1 answer:", len(antinodes))

antinodes.clear()

for r1 in range(len(grid)):
    for c1 in range(len(grid[r1])):
        if grid[r1][c1] != ".":
            for r2 in range(len(grid)):
                for c2 in range(len(grid[r2])):
                    if r2*len(grid)+c2 > r1*len(grid)+c1 and grid[r2][c2] == grid[r1][c1]:
                        dR = r2 - r1
                        dC = c2 - c1
                        antinode = antinode_start = (r1, c1)

                        while (inbounds(*antinode)):
                            antinodes.add(antinode)
                            antinode = (antinode[0] - dR, antinode[1] - dC)

                        antinode = antinode_start = (r1, c1)

                        while (inbounds(*antinode)):
                            antinodes.add(antinode)
                            antinode = (antinode[0] + dR, antinode[1] + dC)

print("Part 2 answer:", len(antinodes))
