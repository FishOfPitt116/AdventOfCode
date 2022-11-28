class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occurrences = 1

    def occur(self):
        self.occurrences += 1

    def equals(self, x, y):
        return self.x == x and self.y == y

class Node:
    def __init__(self, point):
        self.point = point
        self.next = None
    
    def set_next(self, next_point):
        self.next = next_point

class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, node):
        if self.head is not None:
            node.next = self.head
        self.head = node

    def find_point(self, x, y):
        curr = self.head
        while curr is not None:
            if curr.point.equals(x, y):
                return curr
            curr = curr.next
        return None

class Path:
    def __init__(self, x1, y1, x2, y2):
        self.start = Point(x1, y1)
        self.end = Point(x2, y2)
        self.isDiagonal = x1 != x2 and y1 != y2
        self.horizontal = y1 == y2
        positiveDir = y2 > y1
        if self.horizontal:
            positiveDir = x2 > x1
        if not positiveDir:
            self.start, self.end = self.end, self.start

# Parsing paths
input_stream = open("hydrothermalventure.txt")
paths = []
diags = []
curr_path = input_stream.readline()
while curr_path != "end":
    i = 0
    vals = []
    for n in range(4):
        temp = ""
        while curr_path[i] not in [",", " ", "\n"]:
            temp += curr_path[i]
            i += 1
        vals.append(int(temp))
        if curr_path[i] == ",":
            i += 1
        else:
            i += 4            
    new_path = Path(vals[0], vals[1], vals[2], vals[3])
    if not new_path.isDiagonal:
        paths.append(new_path)
    else:
        diags.append(new_path)
    curr_path = input_stream.readline()

dic = {}
count = 0

def check_dic(method_x, method_y, count):
    key = curr_x * curr_y
    if key in dic.keys():
        point = dic[key].find_point(method_x, method_y)
        if point is None:
            dic[key].add_front(Node(Point(method_x, method_y)))
        else:
            point.point.occur()
            if point.point.occurrences == 2:
                count += 1
    else:
        dic[key] = LinkedList()
        dic[key].add_front(Node(Point(method_x, method_y)))

    return count

for path in paths:
    curr_x = path.start.x
    curr_y = path.start.y
    if path.horizontal:
        while curr_x <= path.end.x:
            count = check_dic(curr_x, curr_y, count)
            curr_x += 1
    else:
        while curr_y <= path.end.y:
            count = check_dic(curr_x, curr_y, count)
            curr_y += 1

print("Part One Count: ", count)

for diag in diags:
    curr_x = diag.start.x
    curr_y = diag.start.y
    x_factor = 1 if diag.start.x < diag.end.x else -1
    y_factor = 1 if diag.start.y < diag.end.y else -1
    if x_factor == 1:
        while curr_x <= diag.end.x:
            count = check_dic(curr_x, curr_y, count)
            curr_x += x_factor
            curr_y += y_factor
    else:
        while curr_x >= diag.end.x:
            count = check_dic(curr_x, curr_y, count)
            curr_x += x_factor
            curr_y += y_factor

print("Part Two Count: ", count)