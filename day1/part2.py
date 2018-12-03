file = "day1/input.txt"
number = 0
set = set([])
with open(file, 'r+') as f:
    lines = f.readlines()
    while True:
        for i in range(0, len(lines)):
            line = lines[i]
            if line.startswith('+'):
                number += int(line[1:-1])
            else:
                number -= int(line[1:-1])

            if number in set:
                print(number)
                exit()
            else:
                set.add(number)
