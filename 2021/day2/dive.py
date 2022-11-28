def part_one(pos, depth):
    for line in lines:
        if line == "":
            continue
        curr = line.split()
        if curr[0] == "forward":
            pos += int(curr[1])
        elif curr[0] == "up":
            depth -= int(curr[1])
        elif curr[0] == "down":
            depth += int(curr[1])
    
    return pos*depth

def part_two(pos, depth, aim):
    for line in lines:
        if line == "":
            continue
        curr = line.split()
        if curr[0] == "forward":
            pos += int(curr[1])
            inc = aim * int(curr[1])
            depth += inc
        elif curr[0] == "up":
            aim -= int(curr[1])
        elif curr[0] == "down":
            aim += int(curr[1])

    return pos*depth

file = open("dive.txt")
lines = file.readlines()
print("Part One Count: ", part_one(0, 0))
print("Part Two Count: ", part_two(0, 0, 0))