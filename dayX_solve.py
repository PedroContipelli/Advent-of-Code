import sys
input = "input" if sys.argv[-1] != "--test" else "testcase"
input_file = open(f"day1_{input}.txt", "r")

lines = [line.strip() for line in input_file.readlines()]
grid = [list(line.strip()) for line in input_file.readlines()]




print("Part 1 Answer:", )
print("Part 2 Answer:", )
