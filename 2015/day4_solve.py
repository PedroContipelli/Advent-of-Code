import sys, os, hashlib
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

input = input_file.readline().strip()

for num in range(100_000_000):
  md5_hash = hashlib.md5(f"{input}{num}".encode()).hexdigest()
  if md5_hash[:5] == "00000":
    print("Part 1 Answer:", num)
    break

for num in range(100_000_000):
  md5_hash = hashlib.md5(f"{input}{num}".encode()).hexdigest()
  if md5_hash[:6] == "000000":
    print("Part 2 Answer:", num)
    break