def part_one():
    onecount = []
    for i in range(12):
        onecount.append(0)
    for line in lines:
        for i in range(12):
            if line[i] == '1':
                onecount[i] += 1

    exp = 1
    gamma = 0
    epsilon = 0
    for n in range(len(onecount)-1, -1, -1):
        if onecount[n] > len(lines)/2:
            gamma += exp
        else:
            epsilon += exp
        exp = exp << 1

    return gamma*epsilon

def part_two():
    def oxygen_generator(vals, bit):
        if (len(vals) == 1):
            return binary_to_dec(vals[0])
        zeros = []
        ones = []
        for val in vals:
            if val[bit] == '0':
                zeros.append(val)
            else:
                ones.append(val)
        if len(zeros) > len(ones):
            return oxygen_generator(zeros, bit+1)
        return oxygen_generator(ones, bit+1)

    def co2_scrubber(vals, bit):
        if (len(vals) == 1):
            return binary_to_dec(vals[0])
        zeros = []
        ones = []
        for val in vals:
            if val[bit] == '0':
                zeros.append(val)
            else:
                ones.append(val)
        if len(zeros) > len(ones):
            return co2_scrubber(ones, bit+1)
        return co2_scrubber(zeros, bit+1)

    def binary_to_dec(num):
        exp = 1
        output = 0
        for i in range(11, -1, -1):
            if num[i] == '1':
                output += exp
            exp = exp << 1
        return output

    return oxygen_generator(lines, 0)*co2_scrubber(lines, 0)

file = open("binarydiagnostic.txt")
lines = file.readlines()
print('Part One Count: ', part_one())
print('Part Two Count: ', part_two())