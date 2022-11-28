def part_one():
    count = 0
    prev = ''
    for num in nums:
        if num == 'end':
            return count
        elif num == '':
            continue
        elif prev == '':
            prev = int(num)
        else:
            curr = int(num)
            if curr > prev:
                count = count + 1
            prev = curr

def part_two():
    count = 0
    window = []
    currSum = 0
    toRemove = 0
    for num in nums:
        if num == 'end':
            return count
        elif num == '':
            continue
        elif len(window) < 3:
            window.append(int(num))
            currSum += int(num)
        else:
            prevSum = currSum
            currSum -= window[toRemove]
            window[toRemove] = int(num)
            currSum += int(num)
            if currSum > prevSum:
                count = count + 1
            if (toRemove == 2):
                toRemove = 0
            else:
                toRemove += 1

file = open("sonarsweep.txt")
nums = file.readlines()
print("Part One Count: ", part_one())
print("Part Two Count: ", part_two())