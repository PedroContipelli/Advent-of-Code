import sys
input = "testcase" if sys.argv[-1] == "--test" else "input"
input_file = open(f"dayX_{input}.txt", "r")

lines = [line.strip() for line in input_file.readlines()]
grid = [list(line.strip()) for line in input_file.readlines()]




print("Part 1 Answer:", )
print("Part 2 Answer:", )
