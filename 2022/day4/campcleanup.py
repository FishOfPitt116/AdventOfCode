file = open("campcleanup.txt")
lines = file.readlines()
part1_output = 0
part2_output = 0
for n, line in enumerate(lines):
    pairs = line.split(",")
    first_elf = pairs[0].split("-")
    second_elf = pairs[1].split("-")
    if n != len(lines)-1:
        second_elf[1] = second_elf[1][:len(second_elf[1])-1]
    first_elf = [int(ele) for ele in first_elf]
    second_elf = [int(ele) for ele in second_elf]
    if (first_elf[0] >= second_elf[0]) and (first_elf[1] <= second_elf[1]):
        part1_output += 1
    elif (second_elf[0] >= first_elf[0]) and (second_elf[1] <= first_elf[1]):
        part1_output += 1
    if (first_elf[0] <= second_elf[1]) and (second_elf[0] <= first_elf[1]):
        part2_output += 1
print("Star 1 Solution:", part1_output)
print("Star 2 Solution:", part2_output)
file.close()