from copy import deepcopy

file = open("supplystacks.txt")
lines = file.readlines()
part1_stacks = []
part2_stacks = []
part1_output = ""
part2_output = ""
for column in range(1, 34, 4):
    curr_stack = []
    for row in range(7, -1, -1):
        if ord(lines[row][column]) == 32:
            break
        curr_stack.append(lines[row][column])
    part1_stacks.append(curr_stack)
part2_stacks = deepcopy(part1_stacks)
for i in range(10, len(lines)):
    words = lines[i].split(" ")
    amount = int(words[1])
    src = int(words[3])
    if i == len(lines)-1:
        dst = int(words[5])
    else:
        dst = int(words[5][:len(words[5])-1])
    temp_stack = []
    for i in range(amount):
        ele_1 = part1_stacks[src-1].pop()
        ele_2 = part2_stacks[src-1].pop()
        part1_stacks[dst-1].append(ele_1)
        temp_stack.append(ele_2)
    while len(temp_stack) != 0:
            part2_stacks[dst-1].append(temp_stack.pop())
for stack in part1_stacks:
    part1_output += stack[len(stack)-1]
for stack in part2_stacks:
    part2_output += stack[len(stack)-1]
print("Star 1 Solution:", part1_output)
print("Star 2 Solution:", part2_output)
file.close()