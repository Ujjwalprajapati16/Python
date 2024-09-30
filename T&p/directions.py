x = 3
y = 3
start = "2-2-E"
path = "r m l m l m r m"

start = start.split("-")
path = path.split(" ")

for i in path:
    if i == "l":
        if start[2] == "N":
            start[2] = "W"
        elif start[2] == "W":
            start[2] = "S"
        elif start[2] == "S":
            start[2] = "E"
        elif start[2] == "E":
            start[2] = "N"
    elif i == "r":
        if start[2] == "N":
            start[2] = "E"
        elif start[2] == "E":
            start[2] = "S"
        elif start[2] == "S":
            start[2] = "W"
        elif start[2] == "W":
            start[2] = "N"
    elif i == "m":
        if start[2] == "N":
            start[1] = str(int(start[1]) + 1)
        elif start[2] == "E":
            start[0] = str(int(start[0]) + 1)
        elif start[2] == "S":
            start[1] = str(int(start[1]) - 1)
        elif start[2] == "W":
            start[0] = str(int(start[0]) - 1)
        
            
if int(start[0]) > x or int(start[1]) > y:
    print("ERROR")
else :
    print("-".join(start))
    
# print(path)
# print(start)