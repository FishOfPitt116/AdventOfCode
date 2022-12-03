file = open("rucksackreorg.txt")
lines = file.readlines()
part1_output = 0
part2_output = 0
group = {}
for n, line in enumerate(lines):
    items = {}
    for i in range(len(line)//2):
        items[line[i]] = 1
    j = len(line)//2
    while line[j] not in items:
        j += 1
    if ord(line[j]) >= 97:
        part1_output += (ord(line[j])-96)
    else:
        part1_output += (ord(line[j])-38)
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
                part2_output += (ord(item)-96)
            else:
                part2_output += (ord(item)-38)
            break
    if n%3 == 2:
        group = {}
print("Star 1 Solution:", part1_output)
print("Star 2 Solution:", part2_output)
file.close()