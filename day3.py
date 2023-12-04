import re
with open("day3input.txt") as f:
    grid = [x.strip() for x in f.readlines()]
answer = 0
gears = {}
for i in range(len(grid)):
    numbers = re.finditer(r"\d+", grid[i])
    for n in numbers:
        part_found = False
        for j in range(n.start()-1, n.end()+1):
            for k in range(i-1, i+2):
                if 0 <= j < len(grid[i]) and 0 <= k < len(grid) and grid[k][j] == "*":
                    if (k, j) not in gears.keys():
                        gears[(k, j)] = list()
                    gears[(k, j)].append(n.group(0))
                    
                if not part_found and 0 <= j < len(grid[i]) and 0 <= k < len(grid) and not grid[k][j].isdigit() and grid[k][j] != ".":
                    answer += int(n.group(0))
                    part_found = True

print("The first answer is:", answer)
answer = 0
for key in gears.keys():
    if len(gears[key]) == 2:
        answer += int(gears[key][0]) * int(gears[key][1])
print("The second answer is:", answer)