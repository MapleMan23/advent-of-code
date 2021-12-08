from collections import defaultdict

with open("day-2/day-2-input.txt") as f:
    commands = [line.split() for line in f.readlines()]
commands = list(map(lambda x: (x[0], int(x[1])), commands))

# Part 1
c = defaultdict(list)
for d, v in commands:
    c[d].append(int(v))

right = sum(c["forward"])
up = sum(c["up"])
down = sum(c["down"])

vert = down - up

print(right * vert)


# Part 2
horiz, vert, aim = 0, 0, 0
for comm, amount in commands:
    if comm == 'up':
        aim -= amount
    elif comm == 'down':
        aim += amount
    elif comm == 'forward':
        horiz += amount
        vert += aim * amount

print(horiz * vert)