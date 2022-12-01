file = open("caloriecounting.txt")
lines = file.readlines() # array representation of file lines
max_calories = 0
second_calories = 0
third_calories = 0
curr_calories = 0
for i, v in enumerate(lines):
    if v == "\n":
        if curr_calories > max_calories:
            third_calories = second_calories
            second_calories = max_calories
            max_calories = curr_calories
        elif curr_calories > second_calories:
            third_calories = second_calories
            second_calories = curr_calories
        elif curr_calories > third_calories:
            third_calories = curr_calories
        curr_calories = 0
    else:
        curr_calories += int(v)
print("Star 1 Solution: ", max_calories)
print("Star 2 Solution: ", max_calories + second_calories + third_calories)
file.close()