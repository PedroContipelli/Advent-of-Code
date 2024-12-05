input_file = open("day4_input.txt", "r")

lines = input_file.readlines()

total_value = 0

for card in lines:
    tokens = card.split()
    winning = []
    i = 2

    while tokens[i] != '|':
        winning.append(tokens[i])
        i += 1

    i += 1
    card_value = 0

    while i < len(tokens):
        if tokens[i] in winning:
            if card_value == 0:
                card_value = 1
            else:
                card_value *= 2
        i += 1

    total_value += card_value

print("Part 1 answer:", total_value)

total_cards = 0
copies = {}

for card_id, card in enumerate(lines):
    tokens = card.split()
    copies[card_id] = copies.get(card_id, 0) + 1

    winning = []
    i = 2

    while tokens[i] != '|':
        winning.append(tokens[i])
        i += 1

    i += 1
    matching_numbers = 0

    while i < len(tokens):
        if tokens[i] in winning:
            matching_numbers += 1
        i += 1

    for card_num in range(card_id + 1, card_id + 1 + matching_numbers):
        copies[card_num] = copies.get(card_num, 0) + copies[card_id]

print("Part 2 answer:", sum(copies.values()))
