import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]

nice_strings = 0

def is_nice(str):
  condition1 = False
  vowel_count = 0
  for letter in str:
    if letter in "aeiou":
      vowel_count += 1
    if vowel_count == 3:
      condition1 = True
      break
  
  condition2 = False
  for i in range(len(str)-1):
    if str[i] == str[i+1]:
      condition2 = True
      break

  banned = ["ab", "cd", "pq", "xy"]
  for ban in banned:
    if ban in str:
      return False
  
  return condition1 and condition2

for line in lines:
  if is_nice(line):
    nice_strings += 1

print("Part 1 Answer:", nice_strings)

nice_strings = 0

def is_nice_2(str):
  condition1 = False
  for i in range(len(str)-1):
    if str[i:i+2] in f"{str[:i]} {str[i+2:]}":
      condition1 = True
      break

  condition2 = False
  for i in range(len(str)-2):
    if str[i] == str[i+2]:
      condition2 = True
      break
  
  return condition1 and condition2

for line in lines:
  if is_nice_2(line):
    nice_strings += 1

print("Part 2 Answer:", nice_strings)