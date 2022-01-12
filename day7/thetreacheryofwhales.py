crab_submarines = {}
curr_fuel = 0
crab_count = 0
on_left = 0
input_stream = open("thetreacheryofwhales.txt")
init = input_stream.readline()
temp = ""
for char in init:
    if char == ",":
        if int(temp) not in crab_submarines.keys():
            crab_submarines[int(temp)] = 0
        crab_submarines[int(temp)] += 1
        crab_count += 1
        curr_fuel += int(temp)
        temp = ""
    else:
        temp += char
if int(temp) not in crab_submarines.keys():
    crab_submarines[int(temp)] = 0
crab_submarines[int(temp)] += 1
crab_count += 1
curr_fuel += int(temp)
# What each global variable now represents:
#   crab_submarines: Dictionary mapping horizontal position to # of crabs there
#   curr_fuel: Current amount of fuel needed to move to position 0 (will be updated for each position)
#   crab_count: Total number of crabs to move
#   on_left: Crabs to the left of the current position tracking (i.e. the number of crabs which add to curr_fuel)

print(curr_fuel)
for i in range(crab_count):
    if i in crab_submarines.keys():
        on_left += crab_submarines[i]
    if on_left > (crab_count/2):
        print("Part One Count: ", curr_fuel)
        break
    curr_fuel += (2 * on_left) - crab_count
    print(curr_fuel)