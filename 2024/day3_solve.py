import re
import math

input_file = open("day3_input.txt", "r")

mul_pattern = r"mul\(\d+,\d+\)"
num_pattern = r"\d+"
mul_pattern_start = r"^mul\(\d+,\d+\)"

sum = 0
sum_enabled = 0

def eval_mul(instruction):
    args = re.findall(num_pattern, instruction)
    return int(args[0]) * int(args[1])

enabled = True

for line in input_file:
    instructions = re.findall(mul_pattern, line)

    for instruction in instructions:
        # print(instruction)
        sum += eval_mul(instruction)

    for i in range(len(line)):
        suffix = line[i:]
        if suffix.startswith("do()"):
            enabled = True
        if suffix.startswith("don't()"):
            enabled = False
        if (instruction := re.match(mul_pattern_start, suffix)) and enabled:
            sum_enabled += eval_mul(instruction.group())

print("Part 1 answer:", sum)
print("Part 2 answer:", sum_enabled)
