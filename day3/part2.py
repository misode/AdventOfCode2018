import re

file = "day3/input.txt"
spots = {}
claims = [True] * 1237

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
                        claims[spots[spot]] = False
                        claims[i] = False
                    else:
                        spots[spot] = i

    for i in range(0, len(claims)):
        if claims[i]:
            print(i+1)
