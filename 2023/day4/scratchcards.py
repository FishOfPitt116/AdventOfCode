part1_solution = 0
with open("scratchcards.txt") as f:
    lines = f.readlines()
    for line in lines:
        numbers = line.split(":")[1]
        winning_numbers, our_numbers = numbers.split("|")
        winning_numbers, our_numbers = winning_numbers.strip().split(), our_numbers.strip().split()
        dic = {n : 1 for n in our_numbers}
        i = -1
        for w in winning_numbers:
            if w in dic:
                i += 1
        if i != -1:
            part1_solution += pow(2, i)
print("Part 1 Solution:", int(part1_solution))

cards = {}
with open("scratchcards.txt") as f:
    lines = f.readlines()
    for line_num, line in enumerate(lines):
        line_num += 1
        if line_num not in cards:
            cards[line_num] = 0
        cards[line_num] += 1
        numbers = line.split(":")[1]
        winning_numbers, our_numbers = numbers.split("|")
        winning_numbers, our_numbers = winning_numbers.strip().split(), our_numbers.strip().split()
        dic = {n : 1 for n in our_numbers}
        i = -1
        for w in winning_numbers:
            if w in dic:
                i += 1
        for a in range(line_num+1, line_num+1+(i+1)):
            if a not in cards:
                cards[a] = 0
            cards[a] += cards[line_num]
part2_solution = sum(cards.values())
print("Part 2 Solution:", int(part2_solution))