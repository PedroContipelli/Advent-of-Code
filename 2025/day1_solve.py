
import sys
input = "input" if sys.argv[-1] != "--test" else "testcase"
input_file = open(f"day1_{input}.txt", "r")

lines = [line.strip() for line in input_file.readlines()]

dial = 50
password_counter = 0

for instruction in lines:
  direction = 1 if instruction.startswith("R") else -1
  magnitude = int(instruction[1:])
  dial += direction * magnitude
  dial %= 100
  password_counter += int(dial == 0)

print("Part 1 Answer:", password_counter)

prev_dial = 50
dial = 50
password_counter = 0

# -200 | -100 | 0 | (50) | 100 | 200

for instruction in lines:
  direction = 1 if instruction.startswith("R") else -1
  magnitude = int(instruction[1:])

  full_rotations = magnitude // 100
  password_counter += full_rotations

  remainder = magnitude % 100
  dial += direction * remainder
  if prev_dial != 0 and (dial <= 0 or dial >= 100):
    password_counter += 1

  dial %= 100
  prev_dial = dial

print("Part 2 Answer:", password_counter)
