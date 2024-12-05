input_file = open("day2_input.txt", "r")

def is_safe(report):
    if len(report) < 2:
        return True

    increasing = report[1] - report[0] > 0

    for i in range(len(report) - 1):
        level1 = report[i]
        level2 = report[i+1]
        diff = level2 - level1
        if (diff > 0) != increasing:
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            return False

    return True

def is_safe_dampened(report):
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True

    return False

total_safe_reports = 0
total_safe_reports_dampened = 0

for line in input_file:
    report = [int(level) for level in line.split()]
    total_safe_reports += is_safe(report)
    total_safe_reports_dampened += is_safe(report) or is_safe_dampened(report)

print("Part 1 answer:", total_safe_reports)
print("Part 2 answer:", total_safe_reports_dampened)
