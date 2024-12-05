input_file = open("day2_input.txt", "r")

sum_ids = 0
sum_powers = 0

for line in input_file:
    data = line.split()
    game_id = int(data[1][:-1])

    possible = True

    for i in range(2, len(data), 2):
        num_cubes = int(data[i])
        color = data[i+1].rstrip(",;")

        if color == "red" and num_cubes > 12:
            possible = False
        if color == "green" and num_cubes > 13:
            possible = False
        if color == "blue" and num_cubes > 14:
            possible = False

        if not possible:
            break

    if possible:
        sum_ids += game_id

    min_red = min_green = min_blue = 0

    for i in range(2, len(data), 2):
        num_cubes = int(data[i])
        color = data[i+1].rstrip(",;")

        if color == "red":
            min_red = max(min_red, num_cubes)
        if color == "green":
            min_green = max(min_green, num_cubes)
        if color == "blue":
            min_blue = max(min_blue, num_cubes)

    sum_powers += min_red * min_green * min_blue

print("Part 1 answer:", sum_ids)
print("Part 2 answer:", sum_powers)
