class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def __str__(self):
        return "File named " + self.name + " with size " + str(self.size)

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = []

    def add_file(self, name, size):
        self.files.append(File(name, size))

    def add_directory(self, name):
        if name not in self.children:
            self.children[name] = Directory(name, self)
        return self.children[name]

    def get_child(self, name):
        return self.add_directory(name)

    def get_size(self):
        output = 0
        for child in self.children.values():
            output += child.get_size()
        for file in self.files:
            output += file.get_size()
        return output

    def get_size_star1(self):
        output = 0
        for file in self.files:
            output += file.get_size()
            if output > 100000:
                return 0
        for child in self.children.values():
            output += child.get_size()
            if output > 100000:
                return 0
        return output

    def __str__(self):
        indents = 1
        temp = self.parent
        while temp != None:
            indents += 1
            temp = temp.parent
        padding = "\t" * indents
        output = "Directory " + self.name + ":\n"
        for child in self.children.values():
            output += padding + str(child) + "\n"
        for file in self.files:
            output += padding + str(file) + "\n"
        return output

file = open("nospace.txt")
lines = file.readlines()
list = False
root_dir = Directory("root", None)
curr_dir = root_dir
all_dirs = [root_dir]
for line in lines[1:]:
    line = line.replace("\n", "")
    args = line.split(" ")
    if args[0] == "$":
        list = False
        if args[1] == "ls":
            list = True
        if args[1] == "cd":
            if args[2] == "..":
                curr_dir = curr_dir.parent
            else:
                curr_dir = curr_dir.get_child(args[2])
    elif list:
        if args[0] == "dir":
            all_dirs.append(curr_dir.add_directory(args[1]))
        else:
            curr_dir.add_file(args[1], int(args[0]))
part1_output = 0
for dir in all_dirs:
    part1_output += dir.get_size_star1()
print("Star 1 Solution:", part1_output)
unused_space = 70000000 - root_dir.get_size()
needed_free_space = 30000000 - unused_space
part2_output = all_dirs[0].get_size()
for dir in all_dirs[1:]:
    curr = dir.get_size()
    if curr >= needed_free_space and curr < part2_output:
        part2_output = curr
print("Star 2 Solution:", part2_output)
file.close()