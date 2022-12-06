file = open("tuningtrouble.txt")
word = file.readline()
chars = {c : i for i, c in enumerate(word[:3])}
start = 0
end = 3
while end - start < 4:
    if word[end] in chars:
        if chars[word[end]] >= start:
            start = chars[word[end]] + 1
    chars[word[end]] = end
    end += 1
print("Star 1 Solution:", end)
chars = {c : i for i, c in enumerate(word[:13])}
start = min(chars.values())
end = 13
while end - start < 14:
    if word[end] in chars:
        if chars[word[end]] >= start:
            start = chars[word[end]] + 1
    chars[word[end]] = end
    end += 1
print("Star 2 Solution:", end)
file.close()