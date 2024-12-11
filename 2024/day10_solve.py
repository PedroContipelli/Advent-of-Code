import copy

input_file = open("day10_input.txt", "r")

grid = [list(line.strip()) for line in input_file.readlines()]

dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]

def inbounds(row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])

def trail_score(startRow, startCol):
    score = 0
    visited = copy.deepcopy(grid)
    queue = [(startRow, startCol)]
    visited[startRow][startCol] = '#'

    while queue:
        row, col = queue.pop(0)
        height = int(grid[row][col])

        for i in range(4):
            newR = row + dR[i]
            newC = col + dC[i]

            if inbounds(newR, newC) and visited[newR][newC] != '#':
                newHeight = int(grid[newR][newC]) if grid[newR][newC] != '.' else -1

                if newHeight == height + 1:
                    queue.append((newR, newC))
                    visited[newR][newC] = '#'
                    if newHeight == 9:
                        score += 1

    return score

sum_scores = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == '0':
            sum_scores += trail_score(r, c)

print("Part 1 answer:", sum_scores)

def trail_rating(startRow, startCol):
    rating = 0
    visited = copy.deepcopy(grid)
    routes = [[0] * len(grid[row]) for row in range(len(grid))]
    queue = [(startRow, startCol)]
    routes[startRow][startCol] = 1

    while queue:
        row, col = queue.pop(0)
        height = int(grid[row][col])
        visited[row][col] = '#'

        if height == 9:
            rating += routes[row][col]

        for i in range(4):
            newR = row + dR[i]
            newC = col + dC[i]

            if inbounds(newR, newC) and visited[newR][newC] != '#':
                newHeight = int(grid[newR][newC]) if grid[newR][newC] != '.' else -1

                if newHeight == height + 1:
                    routes[newR][newC] += routes[row][col]
                    if (newR, newC) not in queue:
                        queue.append((newR, newC))

    return rating

sum_rating = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == '0':
            sum_rating += trail_rating(r, c)

print("Part 2 answer:", sum_rating)
