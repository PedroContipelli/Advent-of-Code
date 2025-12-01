import subprocess
import os
file_prefix = "day1"
input_file = open(f"{file_prefix}_tests.txt", "r")
output_file = open(f"{file_prefix}_testcase.txt", "w")
case_number = 0

for line in input_file.readlines():
  if line.startswith("="):
    case_number += 1
    print(f"Case #{case_number}: ", end="")
    expected_answer = line.split(" ")[1].strip()
    output_file.flush()
    result = subprocess.run(
      ["python", f"{file_prefix}_solve.py", "--test"],
      capture_output=True,
      text=True
    )
    my_answer = result.stdout.splitlines()[1].split()[3]
    print("✅" if my_answer == expected_answer else f"❌ (Expected: {expected_answer} --- Got: {my_answer})")
  elif line.startswith("\n"):
    output_file = open(f"{file_prefix}_testcase.txt", "w")
  else:
    output_file.write(line)

output_file.close()
os.remove(f"{file_prefix}_testcase.txt")
