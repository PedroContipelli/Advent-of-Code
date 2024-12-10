input_file = open("day5_input.txt", "r")

lines = [line.strip() for line in input_file.readlines()]

seeds = [int(x) for x in lines[0].split()[1:]]

line_num = 3
x_to_y_maps = []

for map_type in range(7):
    x_to_y_maps.append([])
    while line_num < len(lines) and lines[line_num] != "":
        map_range = tuple(int(x) for x in lines[line_num].split())
        x_to_y_maps[map_type].append(map_range)
        line_num += 1
    line_num += 2

def seed_to_location(seed):
    for map in x_to_y_maps:
        for dest_start, source_start, range_length in map:
            if source_start <= seed < (source_start + range_length):
                seed += (dest_start - source_start)
                break
    return seed

locations = [seed_to_location(seed) for seed in seeds]

print("Part 1 answer:", min(locations))

# PART 2

# Brute Force (obviously does not work for full input)
# min_location = 9999999999999999999999999999999
#
# for i in range(0, len(seeds), 2):
#     for j in range(seeds[i], seeds[i] + seeds[i+1]):
#         min_location = min(min_location, seed_to_location(j))

# New Idea: Use the domain intervals and x_to_y_map to generate range intervals
# May also need to add a merge step to stop exponential growth of # of intervals | Edit: turns out not necessary!
# Final answer = least of all final range intervals

# Not the cleanest way, but I worked the math out with "a to b" intervals rather than "a to (a + length)"
# So I used these conversion functions to convert between the two notations before and after each step
def length_to_interval(start, length):
    return (start, start + length)

def interval_to_length(start, end):
    return (start, end - start)

# Adds offset to start and end of range
def apply_map(interval, map):
    offset = map[0] - map[1]
    return (interval[0] + offset, interval[1] + offset)

# Apply a single map step to list of domain intervals (ex: Seed -> Soil (line 1))
# My intervals are [a , b) a.k.a. include start, but exclude end
def update(domains, range, map):
    new_domain = set()
    new_range = set()

    for domain in domains:
        domain_start, domain_end = length_to_interval(*domain)
        map_start, map_end = length_to_interval(map[1], map[2])

        # 6 Unique cases for relationship between two intervals

        # Map fully encompasses domain
        if map_start <= domain_start and map_end >= domain_end:
            new_range.add(apply_map((domain_start, domain_end), map))
        # Map is < domain. No effect
        elif map_end <= domain_start:
            new_domain.add((domain_start, domain_end))
        # Map is > domain. No effect
        elif map_start >= domain_end:
            new_domain.add((domain_start, domain_end))
        # Map fully within domain
        elif map_start >= domain_start and map_end <= domain_end:
            new_domain.add((domain_start, map_start))
            new_range.add(apply_map((map_start, map_end), map))
            new_domain.add((map_end, domain_end))
        # Left overlap
        elif map_end <= domain_end:
            new_range.add(apply_map((domain_start, map_end), map))
            new_domain.add((map_end, domain_end))
        # Right overlap
        elif map_start < domain_end:
            new_domain.add((domain_start, map_start))
            new_range.add(apply_map((map_start, domain_end), map))

    # Remove any 0 length intervals (caused by boundary conditions)
    range |= {interval_to_length(*x) for x in new_range if x[0] != x[1]}
    return {interval_to_length(*x) for x in new_domain if x[0] != x[1]}

# Apply a full map step (ex: Seed -> Soil)
def apply_x_to_y_map(domain, x_to_y_map):
    range = set()

    # On each iteration, recalculates domain and adds mapped values to range
    for map in x_to_y_map:
        domain = update(domain, range, map)

    # Pass through remaining domain intervals that were unaffected by any map
    range |= domain

    return range

# The Whole Shabang: apply all sequential maps
# Seed -> Soil -> Fertilizer -> Water -> Light -> Temperature -> Humidity -> Location
def apply_all_maps(intervals):
    for x_to_y_map in x_to_y_maps:
        intervals = apply_x_to_y_map(intervals, x_to_y_map)
    return intervals

# Parse input in new format
def get_seed_intervals():
    seed_intervals = set()
    for i in range(0, len(seeds), 2):
        seed_intervals.add((seeds[i], seeds[i+1]))
    return seed_intervals

all_location_intervals = apply_all_maps(get_seed_intervals())

# Since we're looking for the absolute least location, we only need to check
# the start of each interval (as it's already the local minimum)
print("Part 2 answer:", min([x[0] for x in all_location_intervals]))
