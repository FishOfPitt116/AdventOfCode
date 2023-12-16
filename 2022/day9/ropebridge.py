import math

file = open("ropebridge.txt")
lines = file.readlines()
head = (0, 0)
tail = (0, 0)
part1_output = 1
visited = {(0, 0) : 1}
movements = {"D" : (0, 1), "U" : (0, -1), "L" : (-1, 0), "R" : (1, 0)}
for line in lines:
    movement = movements[line.split(" ")[0]]
    amount = int(line.split(" ")[1])
    for i in range(amount):
        head = (head[0] + movement[0], head[1] + movement[1])
        separation = math.dist(head, tail)
        if separation > math.sqrt(2):
            if math.dist(head, tail) == 2:
                tail = (tail[0] + movement[0], tail[1] + movement[1])
            else:
                if head[0] > tail[0] and head[1] > tail[1]:
                    tail = (tail[0] + 1, tail[1] + 1)
                elif head[0] > tail[0] and head[1] < tail[1]:
                    tail = (tail[0] + 1, tail[1] - 1)
                elif head[0] < tail[0] and head[1] > tail[1]:
                    tail = (tail[0] - 1, tail[1] + 1)
                elif head[0] < tail[0] and head[1] < tail[1]:
                    tail = (tail[0] - 1, tail[1] - 1)
        if tail not in visited:
            visited[tail] = 1
            part1_output += 1
print("Star 1 Solution:", part1_output)
file.close()