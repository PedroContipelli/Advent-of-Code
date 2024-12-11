import functools

input_file = open("day11_input.txt", "r")

input = input_file.readline().strip().split()

def apply_blink(stones):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif (num_digits := len(stone)) % 2 == 0:
            new_stones.append(str(int(stone[:num_digits//2])))
            new_stones.append(str(int(stone[num_digits//2:])))
        else:
            new_stones.append(str(int(stone) * 2024))
    return new_stones

def n_blinks(stones, n_times):
    for i in range(n_times):
        stones = apply_blink(stones)
    return stones

print("Part 1 answer:", len(n_blinks(input, 25)))

# Memoize solutions (top-down dynamic programming)
@functools.cache
def total_count(stone, n_blinks):
    if n_blinks == 0:
        return 1
    if stone == 0:
        return total_count(1, n_blinks - 1)
    elif (num_digits := len(str(stone))) % 2 == 0:
        first_half = int(str(stone)[:num_digits//2])
        second_half = int(str(stone)[num_digits//2:])
        return total_count(first_half, n_blinks - 1) + total_count(second_half, n_blinks - 1)
    else:
        return total_count(stone * 2024, n_blinks - 1)

print("Part 2 answer:", sum([total_count(int(stone), 75) for stone in input]))
