print("Star 1 Solution:", 
    sum(map(lambda x: ((ord(x[2])-87) + ((((ord(x[2])-87)-(ord(x[0])-65))%3)*3)), open("rockpaperscissors.txt").readlines())))
print("Star 2 Solution:", 
    sum(map(lambda x : (((ord(x[2])-88)*3) + (((ord(x[2])-88)+(ord(x[0])-63))%3)+1), open("rockpaperscissors.txt").readlines())))