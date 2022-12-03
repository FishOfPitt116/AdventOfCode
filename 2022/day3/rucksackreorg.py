def part1():
    file = open("rucksackreorg.txt")
    lines = file.readlines()
    output = 0
    for line in lines:
        items = {}
        for i in range(len(line)//2):
            items[line[i]] = 1
        j = len(line)//2
        while line[j] not in items:
            j += 1
        if ord(line[j]) >= 97:
            output += (ord(line[j])-96)
        else:
            output += (ord(line[j])-38)
    print(output)
    file.close()

file = open("rucksackreorg.txt")
lines = file.readlines()
output = 0
group = {}
for n, line in enumerate(lines):
    items = {}
    for item in line:
        if item not in group:
            group[item] = 0
        if item not in items:
            group[item] += 1
        items[item] = 1
        if group[item] == 3:
            if ord(item) >= 97:
                output += (ord(item)-96)
            else:
                output += (ord(item)-38)
            break
    if n%3 == 2:
        group = {}
print(output)
file.close()