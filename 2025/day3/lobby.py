def _get_joltage_output(line: str, digits: int) -> int:
    joltage_output = ""
    starting_idx = 0
    for d in range(digits):
        max_joltage = int(line[starting_idx])
        for i in range(starting_idx, len(line)-(digits-d-1)):
            if int(line[i]) > max_joltage:
                max_joltage = int(line[i])
                starting_idx = i
        joltage_output += str(max_joltage)
        starting_idx += 1
    return int(joltage_output)


joltage_sum_part_1 = 0
joltage_sum_part_2 = 0

with open("lobby.txt", "r") as f:
    lines: list[str] = f.read().strip().splitlines()

    for x, line in enumerate(lines):
        joltage_sum_part_1 += _get_joltage_output(line, 2)
        joltage_sum_part_2 += _get_joltage_output(line, 12)


print(f"Part 1 Result: {joltage_sum_part_1}")
print(f"Part 2 Result: {joltage_sum_part_2}")