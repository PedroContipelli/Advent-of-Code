input_file = open("day1_input.txt", "r")

def calibration_value(line):
    for char in line:
        if '0' <= char <= '9':
            tens = 10 * int(char)
            break

    for char in reversed(line):
        if '0' <= char <= '9':
            ones = int(char)
            break

    return tens + ones

word_to_num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def calibration_value_words(line):
    for i in range(len(line)):
        if '0' <= line[i] <= '9':
            tens = 10 * int(line[i])
            break
        for num_word in word_to_num.keys():
            if line[i:].startswith(num_word):
                tens = 10 * word_to_num[num_word]
                break
        if "tens" in locals():
            break

    for i in range(len(line)-1,-1,-1):
        if '0' <= line[i] <= '9':
            ones = int(line[i])
            break
        for num_word in word_to_num.keys():
            if line[:i].endswith(num_word):
                ones = word_to_num[num_word]
                break
        if "ones" in locals():
            break

    return tens + ones

total_sum = 0
total_sum_words = 0

for line in input_file:
    total_sum += calibration_value(line)
    total_sum_words += calibration_value_words(line)

print("Part 1 answer:", total_sum)
print("Part 2 answer:", total_sum_words)
