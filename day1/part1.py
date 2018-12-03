file = "day1/input.txt"
number = 0
with open(file, 'r+') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith('+'):
            number += int(line[1:-1])
        else:
            number -= int(line[1:-1])

print(number)
