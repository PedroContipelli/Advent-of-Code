import subprocess
import os
file_prefix = "dayX"
input_file = open(f"{file_prefix}_tests.txt", "r")
output_file = open(f"{file_prefix}_testcase.txt", "w")

part_1_cases = []
part_2_cases = []

for line in input_file.readlines():
  if line.startswith("="):
    expected_answers = line[2:].strip().split(",")
    output_file.flush()
    result = subprocess.run(
      ["python", f"{file_prefix}_solve.py", "--test"],
      capture_output=True,
      text=True
    )
    my_answers = [result.stdout.splitlines()[part].split()[3] for part in (0,1)]
    if expected_answers[0] != "":
      part_1_cases.append((expected_answers[0], my_answers[0]))
    if expected_answers[1] != "":
      part_2_cases.append((expected_answers[1], my_answers[1]))
    
  elif line.startswith("\n"):
    output_file = open(f"{file_prefix}_testcase.txt", "w")
  else:
    output_file.write(line)

output_file.close()
os.remove(f"{file_prefix}_testcase.txt")

if part_1_cases != []:
  print("\n--- PART 1 ---")
  for num, case in enumerate(part_1_cases):
    print(f"Case #{num}: ", end="")
    print("✅" if case[0] == case[1] else f"❌ (Expected: {case[0]} --- Got: {case[1]})")

if part_2_cases != []:
  print("\n--- PART 2 ---")
  for num, case in enumerate(part_2_cases):
    print(f"Case #{num}: ", end="")
    print("✅" if case[0] == case[1] else f"❌ (Expected: {case[0]} --- Got: {case[1]})")

print()
