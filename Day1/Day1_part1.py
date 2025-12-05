x = 50
count = 0
rotation = []

with open("puzzle_input.txt") as file:
    for line in file:

        key = (line[0])
        value = int(line[1:])

        rotation.append((key,value))

for n in rotation:
    if n[0] == "R":
        x = (x + n[1]) % 100
        if x == 0:
            count = count + 1
    else:
        x = (x - n[1]) % 100
        if x == 0:
            count = count + 1
print(count)