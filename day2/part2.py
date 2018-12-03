file = "day2/input.txt"
set = set()
with open(file, 'r+') as f:
    lines = f.readlines()
    for i in range(0, 25):
        set.clear()
        for j in range(0, len(lines)):
            line = lines[j]
            newline = line[:i] + line[i+1:]
            if newline in set:
                print(newline)
            else:
                set.add(newline)
