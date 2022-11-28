lanternfish = []
running_sum = 0
for i in range(9):
    lanternfish.append(0)
input_stream = open("lanternfish.txt")
init = input_stream.readline()
for val in range(0, len(init), 2):
    lanternfish[int(init[val])] += 1
    running_sum += 1
# lanternfish now contains the # of lanternfish with each age. population contains the starting population of lanternfish

for i in range(256): # loop thru 256 days to simulate
    running_sum += lanternfish[0]
    lanternfish = [lanternfish[1], lanternfish[2], lanternfish[3], lanternfish[4], lanternfish[5], lanternfish[6], lanternfish[0]+lanternfish[7], lanternfish[8], lanternfish[0]]
    if i == 79: # If we've gotten through 80 days, print part one solution
        print("Part One Count: ", running_sum)
print("Part Two Count: ", running_sum)