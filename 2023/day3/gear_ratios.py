def is_symbol(c: str):
    return not c.isdigit() and c != '.' and c != '\n'

def get_num(line, j):
    if not line[j].isdigit():
        return None
    while j > 0 and line[j-1].isdigit():
        j -= 1
    num = ""
    while line[j].isdigit():
        num += line[j]
        j += 1
    return int(num)

part1_solution = 0
with open("gear_ratios.txt") as f:
    lines = f.readlines()
    curr_num = ""
    valid_num = False
    for i in range(len(lines)):
        curr_num = ""
        valid_num = False
        for j in range(len(lines[i])):
            curr = lines[i][j]
            if curr == '.': # nothing
                if len(curr_num) != 0:
                    if valid_num or (i > 0 and is_symbol(lines[i-1][j])) or (i < len(lines)-1 and is_symbol(lines[i+1][j])):
                        part1_solution += int(curr_num)
                    curr_num = ""
                    valid_num = False
            elif is_symbol(curr): # symbol
                if len(curr_num) != 0:
                    part1_solution += int(curr_num)
                    curr_num = ""
                    valid_num = False
            elif curr.isdigit():
                if len(curr_num) == 0:
                    if (i > 0 and j > 0 and is_symbol(lines[i-1][j-1])) or (j > 0 and is_symbol(lines[i][j-1])) or (i < len(lines)-1 and j > 0 and is_symbol(lines[i+1][j-1])):
                        valid_num = True
                if (i > 0 and is_symbol(lines[i-1][j])) or (i < len(lines)-1 and is_symbol(lines[i+1][j])):
                    valid_num = True
                curr_num += curr
        if valid_num:
            part1_solution += int(curr_num)
print("Part 1 Solution:", part1_solution)

part2_solution = 0
with open("gear_ratios.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "*":
                nums = []
                coords = [(i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1), (i, j-1), (i-1, j-1)]
                for (curr_i, curr_j) in coords:
                    n = get_num(lines[curr_i], curr_j)
                    if n is not None and n not in nums:
                        nums.append(n)
                if len(nums) == 2:
                    part2_solution += (nums[0] * nums[1])
print("Part 2 Solution:", part2_solution)