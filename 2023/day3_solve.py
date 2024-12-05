import re

input_file = open("day3_input.txt", "r")
lines = input_file.readlines()

num_pattern = r"^\d+"

def contains_symbol(str):
    return any(char in str for char in "*@#%/=+-$&")

def clamped_substring(str, i, num_str):
    return str[max(i-1, 0) : i+len(num_str) + 1]

sum_part_nums = 0

for line_num in range(len(lines)):
    prev_line = lines[line_num - 1] if line_num > 0 else ""
    current_line = lines[line_num]
    next_line = lines[line_num + 1] if (line_num < len(lines) - 1) else ""

    i = 0
    while i < len(current_line):
        if num_match := re.match(num_pattern, current_line[i:]):
            num_str = num_match.group()
            adjacent = False

            if contains_symbol(clamped_substring(prev_line, i, num_str)):
                adjacent = True
            elif contains_symbol(clamped_substring(current_line, i, num_str)):
                adjacent = True
            elif contains_symbol(clamped_substring(next_line, i, num_str)):
                adjacent = True

            if adjacent:
                sum_part_nums += int(num_str)

            i += len(num_str)
            continue

        i += 1

print("Part 1 answer:", sum_part_nums)

gear_counts = {}
gear_ratios = {}

def hash(line_num, index):
    return line_num * 1000000000 + index

def inbound(str, j):
    return j >= 0 and j < len(str)

def process_gear(posX, posY, ratio):
    gear_id = hash(posX, posY)
    gear_counts[gear_id] = gear_counts.get(gear_id, 0) + 1
    gear_ratios[gear_id] = gear_ratios.get(gear_id, 1) * ratio

for line_num in range(len(lines)):
    prev_line = lines[line_num - 1] if line_num > 0 else ""
    current_line = lines[line_num]
    next_line = lines[line_num + 1] if (line_num < len(lines) - 1) else ""

    i = 0
    while i < len(current_line):
        if num_match := re.match(num_pattern, current_line[i:]):
            num_str = num_match.group()
            ratio = int(num_str)

            for j in range(i-1, i + len(num_str) + 1):
                if inbound(prev_line, j) and prev_line[j] == "*":
                    process_gear(line_num - 1, j, ratio)
                if inbound(current_line, j) and current_line[j] == "*":
                    process_gear(line_num, j, ratio)
                if inbound(next_line, j) and next_line[j] == "*":
                    process_gear(line_num + 1, j, ratio)

            i += len(num_str)
            continue

        i += 1

sum_gear_ratios = 0

for gear_id, count in gear_counts.items():
    if count == 2:
        sum_gear_ratios += gear_ratios[gear_id]

print("Part 2 answer:", sum_gear_ratios)
