class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False

    def set_visible(self):
        if self.get_visible():
            return 0
        self.visible = True
        return 1

    def get_visible(self):
        return self.visible

file = open("treehouse.txt")
lines = file.readlines()
trees = []
for line in lines:
    row = []
    for h in line:
        if h != "\n":
            row.append(Tree(int(h)))
    trees.append(row)
part1_output = 0
for row in range(len(trees)):
    max_h = -1
    for column in range(len(trees[0])):
        tree = trees[row][column]
        if tree.height > max_h:
            part1_output += tree.set_visible()
            max_h = tree.height
        if max_h == 9:
            break
    max_h = -1
    for column in range(len(trees[0])-1, -1, -1):
        tree = trees[row][column]
        if tree.height > max_h:
            part1_output += tree.set_visible()
            max_h = tree.height
        if max_h == 9:
            break
for column in range(len(trees[0])):
    max_h = -1
    for row in range(len(trees)):
        tree = trees[row][column]
        if tree.height > max_h:
            part1_output += tree.set_visible()
            max_h = tree.height
        if max_h == 9:
            break
    max_h = -1
    for row in range(len(trees)-1, -1, -1):
        tree = trees[row][column]
        if tree.height > max_h:
            part1_output += tree.set_visible()
            max_h = tree.height
        if max_h == 9:
            break
print("Star 1 Solution:", part1_output)
part2_output = 0
for row in range(1, len(trees)-1):
    for column in range(1, len(trees[0])-1):
        height = trees[row][column].height
        temp_output = 1
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            view_distance = 1
            curr_r = row+dir[0]
            curr_c = column+dir[1]
            curr_h = trees[curr_r][curr_c].height
            while curr_r in range(1, len(trees)-1) and curr_c in range(1, len(trees[0])-1) and curr_h < height:
                view_distance += 1
                curr_r += dir[0]
                curr_c += dir[1]
                curr_h = trees[curr_r][curr_c].height
            temp_output = temp_output * view_distance
        if temp_output > part2_output:
            part2_output = temp_output
print("Star 2 Solution:", part2_output)
file.close()