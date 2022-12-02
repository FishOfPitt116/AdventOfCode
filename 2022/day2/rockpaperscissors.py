file = open("input.txt")
lines = file.readlines()
score = 0
for line in lines:
    opponent = line[0]
    you = line[2]
    # Star 1
    if you == 'X':
        pass
        if opponent == 'A':
            score += 3
        elif opponent == 'B':
            score += 1
        elif opponent == 'C':
            score += 2
    #     score += 1
    #     if opponent == 'A':
    #         score += 3
    #     elif opponent == 'C':
    #         score += 6
    elif you == 'Y':
        score += 3
        if opponent == 'A':
            score += 1
        elif opponent == 'B':
            score += 2
        elif opponent == 'C':
            score += 3
    #     score += 2
    #     if opponent == 'A':
    #         score += 6
    #     elif opponent == 'B':
    #         score += 3
    elif you == 'Z':
        score += 6
        if opponent == 'A':
            score += 2
        elif opponent == 'B':
            score += 3
        elif opponent == 'C':
            score += 1
    #     score += 3
    #     if opponent == 'B':
    #         score += 6
    #     elif opponent == 'C':
    #         score += 3
print(score)
file.close()