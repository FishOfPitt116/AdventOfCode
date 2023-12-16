part1_solution = 0
with open("trebuchet.txt") as f:
    for line in f.readlines():
        front = 0
        while not line[front].isdigit():
            front += 1
        back = len(line)-1
        while not line[back].isdigit():
            back -= 1
        value = int(line[front] + line[back])
        part1_solution += value
print("Part 1 Solution:", part1_solution)

part2_solution = 0
word2num_dic = { "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9" }
with open("trebuchet.txt") as f:
    for line in f.readlines():
        front = 0
        while not line[front].isdigit() and line[front:front+3] not in word2num_dic and line[front:front+4] not in word2num_dic and line[front:front+5] not in word2num_dic:
            front += 1
        front = word2num_dic[line[front:front+3]] if line[front:front+3] in word2num_dic else word2num_dic[line[front:front+4]] if line[front:front+4] in word2num_dic else word2num_dic[line[front:front+5]] if line[front:front+5] in word2num_dic else line[front]
        back = len(line)
        while not line[back-1].isdigit() and line[back-3:back] not in word2num_dic and line[back-4:back] not in word2num_dic and line[back-5:back] not in word2num_dic:
            back -= 1
        back = word2num_dic[line[back-3:back]] if line[back-3:back] in word2num_dic else word2num_dic[line[back-4:back]] if line[back-4:back] in word2num_dic else word2num_dic[line[back-5:back]] if line[back-5:back] in word2num_dic else line[back-1]
        value = int(front + back)
        part2_solution += value
print("Part 2 Solution:", part2_solution)