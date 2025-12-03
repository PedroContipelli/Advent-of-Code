import sys
input = "testcase" if sys.argv[-1] == "--test" else "input"
input_file = open(f"day3_{input}.txt", "r")

lines = [line.strip() for line in input_file.readlines()]
sum = 0

for bank in lines:
  max_tens = 0
  max_tens_index = 0
  for i, digit in enumerate(bank[:-1]):
    if int(digit) > max_tens:
      max_tens = int(digit)
      max_tens_index = i
  max_ones = 0
  for i in range(max_tens_index+1, len(bank)):
    if int(bank[i]) > max_ones:
      max_ones = int(bank[i])
  joltage = f"{max_tens}{max_ones}"
  sum += int(joltage)

print("Part 1 Answer:", sum)

sum = 0

def max_digit_from_index(bank, index, from_end):
  max_digit = 0
  max_index = 0
  for i in range(index, len(bank) - from_end):
    if int(bank[i]) > max_digit:
      max_digit = int(bank[i])
      max_index = i
  return max_digit, max_index

for bank in lines:
  joltage = ""
  index = 0
  for from_end in range(11,-1,-1):
    max_digit, max_index = max_digit_from_index(bank, index, from_end)
    joltage += str(max_digit)
    index = max_index+1
  sum += int(joltage)

print("Part 2 Answer:", sum)
