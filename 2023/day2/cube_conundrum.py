part1_solution = 0
max_values = {'red' : 12, 'green' : 13, 'blue' : 14}
with open("cube_conundrum.txt") as f:
    for line in f.readlines():
        game_id = int(line.split(" ")[1].replace(":", ""))
        valid_game = True
        for groups in line.split(":")[1].split(";"):
            red, blue, green = 0, 0, 0
            group = groups[1:].replace(",", "").replace("\n", "").split(" ")
            for i in range(0, len(group), 2):
                if int(group[i]) > max_values[group[i+1]]:
                    valid_game = False
                    break
            if not valid_game:
                break
        if valid_game:
            part1_solution += game_id
print("Part 1 Solution:", part1_solution)

part2_solution = 0
with open("cube_conundrum.txt") as f:
    for line in f.readlines():
        min_values = {}
        for groups in line.split(":")[1].split(";"):
            group = groups[1:].replace(",", "").replace("\n", "").split(" ")
            for i in range(0, len(group), 2):
                min_values[group[i+1]] = int(group[i]) if group[i+1] not in min_values else max(min_values[group[i+1]], int(group[i]))
        part2_solution += (min_values['red'] * min_values['green'] * min_values['blue'])
print("Part 2 Solution:", part2_solution)