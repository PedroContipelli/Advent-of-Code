import sys, os, time, math
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]

def is_correct(presses):
  lights = [False] * len(expected_lights)
  for press_index, num_presses in enumerate(presses):
    if num_presses != 0:
      for light_index in buttons[press_index]:
        lights[light_index] ^= bool(num_presses % 2)
  return lights == expected_lights

def add_press(presses):
  all = []
  for i in range(len(presses)):
    presses[i] += 1
    all.append(list(presses))
    presses[i] -= 1
  return all

def all_extra_press(press_list):
  all = []
  for presses in press_list:
    all += add_press(presses)
  return all

def any_is_correct(press_list):
  for presses in press_list:
    if is_correct(presses):
      return True
  return False

total = 0

for i, machine in enumerate(lines):
  instructions = machine.split(" ")
  expected_lights = [light == '#' for light in instructions[0][1:-1]]
  buttons = []
  for button in instructions[1:-1]:
    buttons.append([int(wire) for wire in button[1:-1].split(",")])

  presses = [0 for _ in buttons]
  all = [presses]

  for num_presses in range(0, 10):
    if any_is_correct(all):
      total += num_presses
      break
    all = all_extra_press(all)

print("Part 1 Answer:", total)

# PART 2 - W.I.P.
# total = 0

# def upper_bound_presses(button):
#   upper_bound = 999
#   for wire in button:
#     upper_bound = min(upper_bound, expected_joltage[wire])
#   return upper_bound

# for i, machine in enumerate(lines):
#   instructions = machine.split(" ")
#   buttons = []
#   for button in instructions[1:-1]:
#     buttons.append([int(num) for num in button[1:-1].split(",")])

#   expected_joltage = [int(num) for num in instructions[-1][1:-1].split(",")]

#   max_presses = [upper_bound_presses(button) for button in buttons]
#   print(max_presses, "=", math.prod(max_presses))

# print("Part 2 Answer:", )