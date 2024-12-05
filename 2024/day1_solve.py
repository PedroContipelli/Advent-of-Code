input_file = open("day1_input.txt", "r")

list_1 = []
list_2 = []

for line in input_file:
    parts = line.split()
    list_1.append(int(parts[0]))
    list_2.append(int(parts[1]))

list_1.sort()
list_2.sort()

sum = 0

for i in range(len(list_1)):
    sum += abs(list_1[i] - list_2[i])

print("Part 1 answer:", sum)

sum = 0

list_2_counts = {}

for num in list_2:
    if num not in list_2_counts:
        list_2_counts[num] = 0

    list_2_counts[num] += 1

for num in list_1:
    sum += num * list_2_counts.get(num, 0)

print("Part 2 answer:", sum)
