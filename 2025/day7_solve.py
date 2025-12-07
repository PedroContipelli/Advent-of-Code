import sys, os
input = "testcase" if sys.argv[-1] == "--test" else "input"
day = os.path.basename(__file__).split("y")[1].split("_")[0]
input_file = open(f"day{day}_{input}.txt")

lines = [line.strip() for line in input_file]
beam_cols = set()
beam_cols.add(lines[0].index("S"))
total_splits = 0

for row in lines[1:]:
  new_beam_cols = set()
  for col in beam_cols:
    if row[col] == '^':
      total_splits += 1
      new_beam_cols.add(col-1)
      new_beam_cols.add(col+1)
    else:
      new_beam_cols.add(col)
  beam_cols = new_beam_cols

print("Part 1 Answer:", total_splits)

beam_cols = {}
beam_cols[lines[0].index("S")] = 1
timelines = 0

for row in lines[1:]:
  new_beam_cols = {}
  for col, timeline in beam_cols.items():
    if row[col] == '^':
      new_beam_cols[col-1] = new_beam_cols.get(col-1, 0) + timeline
      new_beam_cols[col+1] = new_beam_cols.get(col+1, 0) + timeline
    else:
      new_beam_cols[col] = new_beam_cols.get(col, 0) + timeline
  beam_cols = new_beam_cols

print("Part 2 Answer:", sum(beam_cols.values()))