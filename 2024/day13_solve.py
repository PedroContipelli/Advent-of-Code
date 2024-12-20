input_file = open("day13_input.txt", "r")

lines = [line.strip() for line in input_file.readlines()]

def min_tokens(A, B, Prize):
    min_cost = 500

    for A_presses in range(101):
        for B_presses in range(101):
            token_cost = A_presses * 3 + B_presses
            if token_cost < min_cost:
                if A[0] * A_presses + B[0] * B_presses == Prize[0]:
                    if A[1] * A_presses + B[1] * B_presses == Prize[1]:
                        min_cost = token_cost

    return min_cost if min_cost != 500 else 0

total_tokens = 0

for machine in range(0, len(lines), 4):
    A = lines[machine].replace("+", ",").split(",")
    A = (int(A[1]), int(A[3]))

    B = lines[machine+1].replace("+", ",").split(",")
    B = (int(B[1]), int(B[3]))

    Prize = lines[machine+2].replace("=", ",").split(",")
    Prize = (int(Prize[1]), int(Prize[3]))

    total_tokens += min_tokens(A, B, Prize)

print("Part 1 answer:", total_tokens)

def lin_eq_solver(A, B, Prize):
    eq1 = (A[0], B[0], Prize[0])
    eq2 = (A[1], B[1], Prize[1])

    scaled_eq1 = tuple(num * (A[1] / A[0]) for num in eq1)
    elim_eq3 = tuple(num1 - num2 for num1, num2 in zip(scaled_eq1, eq2))

    try:
        Y = elim_eq3[2] / elim_eq3[1]
        X = (eq1[2] - eq1[1]*Y) / eq1[0]
        return (X, Y)
    except:
        # Not implementing these cases as they are not represented in the input
        if elim_eq3[1] == 0 and elim_eq3[2] == 0:
            return "Infinite solutions"

        return "No solution"

# ONE SOLUTION
# A = (1, 2)
# B = (1, 1)
# Prize = (2, 3)

# NO SOLUTION
# A = (1, 1)
# B = (1, 1)
# Prize = (1, 2)

# INFINITE SOLUTIONS
# A = (1, 2)
# B = (1, 2)
# Prize = (10, 20)

# print(lin_eq_solver(A, B, Prize))

# Handle floating point precision errors
def is_integer(num, epsilon=1e-3):
    return abs(num - round(num)) < epsilon

total_tokens = 0

for machine in range(0, len(lines), 4):
    A = lines[machine].replace("+", ",").split(",")
    A = (int(A[1]), int(A[3]))

    B = lines[machine+1].replace("+", ",").split(",")
    B = (int(B[1]), int(B[3]))

    Prize = lines[machine+2].replace("=", ",").split(",")
    Prize = (int(Prize[1]) + 10_000_000_000_000, int(Prize[3]) + 10_000_000_000_000)

    A_presses, B_presses = lin_eq_solver(A, B, Prize)
    if is_integer(A_presses) and is_integer(B_presses):
        total_tokens += 3 * A_presses + B_presses

print("Part 2 answer:", int(total_tokens))
