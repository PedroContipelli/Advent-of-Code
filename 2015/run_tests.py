import sys, subprocess, os
file_prefix = sys.argv[1]
input_file = open(f"{file_prefix}_tests.txt", "r")
output_file = open(f"{file_prefix}_testcase.txt", "w")

test_out = {1: {}, 2: {}}
case = 0

for line in input_file:
  # Evaluate
  if line.startswith("="):
    # Expected
    expected_answers = line[1:].strip().split(",")
    for part in range(1,3):
      test_out[part].setdefault(case, {})["expected"] = expected_answers[part-1]
      test_out[part].setdefault(case, {})["debug"] = ""
    # Run program
    output_file.flush()
    result = subprocess.run(
      ["python", f"{file_prefix}_solve.py", "--test"],
      capture_output=True,
      text=True
    )
    if result.stderr:
      print("\n=============\nPROGRAM ERROR\n=============\n", result.stderr)
      break
    output_lines = result.stdout.splitlines()
    # My answers
    part = 1
    for output_line in output_lines:
      if output_line.startswith(f"Part {part} Answer: "):
        test_out[part][case]["mine"] = output_line.split()[3]
        part += 1
      else:
        test_out[part][case]["debug"] += output_line + "\n"
  # Next test case
  elif line == "----------\n":
    output_file = open(f"{file_prefix}_testcase.txt", "w")
    case += 1
  # Write test case
  else:
    output_file.write(line)

# Cleanup
output_file.close()
os.remove(f"{file_prefix}_testcase.txt")

# Print results
for part, cases in test_out.items():
  print(f"\n--- PART {part} ---")
  for num, case in cases.items():
    if case["expected"] and "mine" in case:
      print(f"Case #{num}:", end=" ")
      print("✅" if case["expected"] == case["mine"] else f"❌ (Expected: {case["expected"]} --- Got: {case["mine"]})")
      if case["debug"]:
        print(case["debug"])

print()