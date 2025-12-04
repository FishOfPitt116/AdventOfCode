def _get_accessible_rolls(roll_lines: list[list[int]]):
    accessible_rolls = []

    for i in range(len(roll_lines)):
        for j in range(len(roll_lines[0])):
            if roll_lines[i][j] == 1:
                num_adjacent_rolls = 0
                if i > 0:
                    if j > 0:
                        num_adjacent_rolls += roll_lines[i-1][j-1]
                    num_adjacent_rolls += roll_lines[i-1][j]
                    if j < len(roll_lines[0])-1:
                        num_adjacent_rolls += roll_lines[i-1][j+1]
                if j > 0:
                    num_adjacent_rolls += roll_lines[i][j-1]
                if j < len(roll_lines[0])-1:
                    num_adjacent_rolls += roll_lines[i][j+1]
                if i < len(roll_lines)-1:
                    if j > 0:
                        num_adjacent_rolls += roll_lines[i+1][j-1]
                    num_adjacent_rolls += roll_lines[i+1][j]
                    if j < len(roll_lines[0])-1:
                        num_adjacent_rolls += roll_lines[i+1][j+1]
                if num_adjacent_rolls < 4:
                    accessible_rolls.append([i, j])
    
    return accessible_rolls

def _remove_accessible_rolls(roll_lines: list[list[int]], accessible_rolls: list[list[int]]):
    for roll_loc in accessible_rolls:
        roll_lines[roll_loc[0]][roll_loc[1]] = 0
    return roll_lines

accessible_rolls_part_1 = 0
accessible_rolls_part_2 = 0

with open("printing_department.txt", "r") as f:
    lines: list[str] = f.read().strip().splitlines()

    roll_lines: list[list[int]] = []
    for line in lines:
        roll_line = []
        for char in line:
            if char == '@':
                roll_line.append(1)
            else:
                roll_line.append(0)
        roll_lines.append(roll_line)

    accessible_rolls = _get_accessible_rolls(roll_lines)
    accessible_rolls_part_1 = len(accessible_rolls)
    accessible_rolls_part_2 = len(accessible_rolls)
    while len(accessible_rolls) != 0:
        roll_lines = _remove_accessible_rolls(roll_lines, accessible_rolls)
        accessible_rolls = _get_accessible_rolls(roll_lines)
        accessible_rolls_part_2 += len(accessible_rolls)

print(f"Part 1 Result: {accessible_rolls_part_1}")
print(f"Part 2 Result: {accessible_rolls_part_2}")