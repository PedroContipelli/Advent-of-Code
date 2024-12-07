input_file = open("day7_input.txt", "r")

lines = [line.strip() for line in input_file.readlines()]

def is_valid(current_value, i):
    if i >= len(equation):
        return current_value == test_value
    elif current_value > test_value:
        return False
    else:
        return is_valid(current_value + int(equation[i]), i+1) or is_valid(current_value * int(equation[i]), i+1)

total_calibration = 0

for line in lines:
    equation = line.split()
    test_value = int(equation[0][:-1])

    if is_valid(int(equation[1]), 2):
        total_calibration += test_value

print("Part 1 answer:", total_calibration)

def is_valid(current_value, i):
    if i >= len(equation):
        return current_value == test_value
    elif current_value > test_value:
        return False
    else:
        return is_valid(current_value + int(equation[i]), i+1) or is_valid(current_value * int(equation[i]), i+1) or is_valid(int(str(current_value) + equation[i]), i+1)

total_calibration_2 = 0

for line in lines:
    equation = line.split()
    test_value = int(equation[0][:-1])

    if is_valid(int(equation[1]), 2):
        total_calibration_2 += test_value


print("Part 2 answer:", total_calibration_2)
