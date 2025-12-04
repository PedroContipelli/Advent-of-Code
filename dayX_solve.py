import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]
grid = [list(line.strip()) for line in input_file]




print("Part 1 Answer:", )
print("Part 2 Answer:", )
