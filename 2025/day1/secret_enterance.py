pointer = 50
zeros = 0
times_pointed = 0

with open("secret_enterance.txt", "r") as f:
    data: list[str] = f.read().strip().splitlines()
    for move in data:
        direction, amount = move[0], int(move[1:])
        
        # avoid double counting when starting on 0
        if direction == "L" and pointer == 0:
            times_pointed -= 1

        # pointer moving logic
        if direction == "L":
            pointer -= amount
        elif direction == "R":
            pointer += amount
        else:
            raise Exception("invalid direction")

        # calculate times pointed and the number of zeros we land on
        times_pointed += abs(pointer // 100)
        pointer = pointer % 100
        if pointer == 0:
            zeros += 1

        # avoid missing the last click
        if direction == "L" and pointer == 0:
            times_pointed += 1

print(f"Part 1 Result: {zeros}")
print(f"Part 2 Result: {times_pointed}")