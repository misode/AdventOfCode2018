file = "day2/input.txt"
number = 0
with open(file, 'r+') as f:
    lines = f.readlines()
    two = 0
    three = 0
    for i in range(0, len(lines)):
        line = lines[i]
        dict = {}
        for j in range(0, len(line)):
            letter = line[j]
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        add_two = 0
        add_three = 0
        for j in dict:
            if dict[j] == 2:
                add_two = 1
            if dict[j] == 3:
                add_three = 1
        two += add_two
        three += add_three
print(two*three)
