with open("day-1/day-1-input.txt") as f:
    measurements = [int(line) for line in f.readlines()]

# Part 1
n = 0
for i in range(1, len(measurements)):
    if measurements[i - 1] < measurements[i]:
        n += 1

print(f"Part 1: {n = }")


# Part 2
n = 0
for i in range(3, len(measurements)):
    if measurements[i - 3] < measurements[i]:
        n += 1

print(f"Part 2: {n = }")

