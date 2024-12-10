input_file = open("day9_input.txt", "r")

input = input_file.readline().strip()

blocks = []

for i, length in enumerate(input):
    # FILE
    if i % 2 == 0:
        file_id = i // 2
        for j in range(int(length)):
            blocks.append(file_id)
    # FREE SPACE
    else:
        for j in range(int(length)):
            blocks.append(".")

blocks_copy = blocks.copy()

free_index = 0
file_index = len(blocks) - 1

def get_next_free_index(i):
    while i < len(blocks) and blocks[i] != '.':
        i += 1
    return i

def get_prev_file_index(i):
    while i >= 0 and blocks[i] == '.':
        i -= 1
    return i

# Compact files step
while True:
    free_index = get_next_free_index(free_index)
    file_index = get_prev_file_index(file_index)

    if free_index >= file_index:
        break

    blocks[free_index], blocks[file_index] = blocks[file_index], blocks[free_index]

# Checksum step
def calc_checksum(blocks):
    checksum = 0
    for position, file_id in enumerate(blocks):
        if file_id != '.':
            checksum += position * file_id
    return checksum

print("Part 1 answer:", calc_checksum(blocks))

print ("\nRunning Part 2 now... (may take a while)")

blocks = blocks_copy

free_interval = (0, 0)
file_interval = (len(blocks), len(blocks))

def get_next_free_interval(interval):
    start, end = interval
    start = end
    while start < len(blocks) and blocks[start] != '.':
        start += 1
    end = start
    while end < len(blocks) and blocks[end] == '.':
        end += 1
    return (start, end)

def get_prev_file_interval(interval):
    start, end = interval
    end = start - 1
    while end > 0 and blocks[end] == '.':
        end -= 1
    start = end - 1
    while start > 0 and blocks[start] == blocks[end]:
        start -= 1
    return (start + 1, end + 1)

def length(interval):
    return interval[1] - interval[0]

free_interval_reset = (0, 0)

# Compact files step
while True:
    free_interval = free_interval_reset
    file_interval = get_prev_file_interval(file_interval)

    if file_interval[0] == -1:
        break

    no_space_left = False

    while length(free_interval) < length(file_interval):
        free_interval = get_next_free_interval(free_interval)
        if free_interval[0] >= file_interval[0]:
            no_space_left = True
            break

    if no_space_left:
        continue

    for i in range(length(file_interval)):
        blocks[free_interval[0] + i], blocks[file_interval[0] + i] = blocks[file_interval[0] + i], blocks[free_interval[0] + i]

print("Part 2 answer:", calc_checksum(blocks))
