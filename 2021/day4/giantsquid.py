class Node:
    def __init__(self, val):
        self.val = val
        self.marked = False

    def mark(self):
        self.marked = True

    def is_marked(self):
        return self.marked

    def val_match(self, input):
        if self.val == input:
            return True
        return False

class Bingo:
    def __init__(self, rows):
        self.matrix = []
        self.sum = 0
        for row in rows:
            curr = []
            for i in range(0,14,3):
                if row[i] == " ":
                    curr.append(Node(int(row[i+1])))
                    self.sum += int(row[i+1])
                else:
                    curr.append(Node(int(row[i:i+2])))
                    self.sum += int(row[i:i+2])
            self.matrix.append(curr)
        self.complete = False
    
    def find_val(self, inp):
        for r in range(5):
            for c in range(5):
                if self.matrix[r][c].val_match(inp):
                    output = inp
                    # Check row
                    for x in range(5):
                        if not self.matrix[r][x].is_marked() and x != c:
                            break
                        if x == 4:
                            self.complete = True
                            return (self.sum - inp) * inp
                    # Check column
                    for x in range(5):
                        if not self.matrix[x][c].is_marked() and x != c:
                            break
                        if x == 4:
                            self.complete = True
                            return (self.sum - inp) * inp
                    self.matrix[r][c].mark()
                    self.sum -= inp
                    return 0
        return 0

    def get_element(self, r, c):
        return self.matrix[r][c].val

    def is_complete(self):
        return self.complete
                

# Parse numbers to draw
input_stream = open("giantsquid.txt")
drawn_numbers = input_stream.readline()
draw = []
val = ""
for char in drawn_numbers:
    if char == ",":
        draw.append(int(val))
        val = ""
    else:
        val += char
draw.append(int(val)) # Draw now contains all numbers to be drawn in order

# Parse bingo cards
curr = ""
bingo_cards = []
while (curr != "end"):
    if (curr in ["", " ", "\n"]):
        curr = input_stream.readline()
    else:
        rows = []
        for i in range(5):
            rows.append(curr[:14])
            curr = input_stream.readline()
        bingo_cards.append(Bingo(rows))


# At this point, we have bingo_cards (all bingo cards in order) and draw (numbers to draw in order).
# Now we simply have to complete the process of drawing each number sequentially.
def both():
    first = False
    last_winner = 0
    for num in draw:
        for card in bingo_cards:
            if not card.is_complete():
                pot_output = card.find_val(num)
                if pot_output != 0:
                    last_winner = pot_output
                    if not first:
                        print("Part One Count: ", last_winner)
                        first = True
    print("Part Two Count: ", last_winner)



# Note: Due to the OOP nature of this solution, only one part method can be run each time the program is run to achieve accurate results.
both()