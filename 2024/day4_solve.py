input_file = open("day4_input.txt", "r")

grid = input_file.readlines()

def inbounds(grid, row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

dR = [-1, -1, -1, 0, 0, 1, 1, 1]
dC = [-1, 0, 1, -1, 1, -1, 0, 1]

def get_str(grid, row, col, dIndex):
    str = ""
    for i in range(4):
        currRow = row + i*dR[dIndex]
        currCol = col + i*dC[dIndex]

        if inbounds(grid, currRow, currCol):
            str += grid[currRow][currCol]
        else:
            break

    return str

xmas_count = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 'X':
            for i in range(8):
                if get_str(grid, row, col, i) == 'XMAS':
                    xmas_count += 1

print("Part 1 answer:", xmas_count)

x_mas_count = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 'A':
            currRow = row-1
            currCol = col-1
            str1 = ""
            for i in range(3):
                if inbounds(grid, currRow, currCol):
                    str1 += grid[currRow][currCol]
                    currRow += 1
                    currCol += 1
                else:
                    break
            currRow = row-1
            currCol = col+1
            str2 = ""
            for i in range(3):
                if inbounds(grid, currRow, currCol):
                    str2 += grid[currRow][currCol]
                    currRow += 1
                    currCol -= 1
                else:
                    break

            if (str1 == 'MAS' or str1 == 'SAM') and (str2 == 'MAS' or str2 == 'SAM'):
                x_mas_count += 1

print("Part 2 answer:", x_mas_count)
