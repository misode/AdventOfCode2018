import re

file = "day3/input.txt"
spots = {}

with open(file, 'r+') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        match = re.match('#.+ @ (.+),(.*): (.*)x(.*)', line)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            w = int(match.group(3))
            h = int(match.group(4))
            for j in range(x, x+w):
                for k in range(y, y+h):
                    spot = f'{j},{k}'

                    if spot in spots:
                        spots[spot] += 1
                    else:
                        spots[spot] = 1

    conflicts = 0
    for s in spots:
        if spots[s] > 1:
            conflicts += 1
    print(conflicts)
