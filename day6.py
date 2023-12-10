import re
import math

with open("day6input.txt") as f:
    data = [x.strip() for x in f.readlines()]
races = [[int(x)] for x in re.split(r" +", data[0])[1:]]
dists = [int(x) for x in re.split(r" +", data[1])[1:]]
for i in range(len(races)):
    races[i].append(dists[i])

# Y = (t-x) * x = t*x - x^2
# 0 = x^2 - t*x + y
# x = t/2 +- sqrt(t^2/4 - y)
answer = 1
for race in races:
    min_hold = math.ceil(race[0] / 2 - math.sqrt(race[0]**2/4 - race[1]))
    if race[1] >= race[0]*min_hold - min_hold**2:
        min_hold += 1
    max_hold = math.floor(race[0] / 2 + math.sqrt(race[0]**2/4 - race[1]))
    if race[1] >= race[0]*max_hold - max_hold**2:
        max_hold -= 1
    answer *= int(max_hold - min_hold) + 1
print("The first answer is:", answer)
race = int(data[0].split(":")[1].strip().replace(" ", ""))
dist = int(data[1].split(":")[1].strip().replace(" ", ""))
race = [race, dist]
min_hold = math.ceil(race[0] / 2 - math.sqrt(race[0]**2/4 - race[1]))
if race[1] >= race[0]*min_hold - min_hold**2:
    min_hold += 1
max_hold = math.floor(race[0] / 2 + math.sqrt(race[0]**2/4 - race[1]))
if race[1] >= race[0]*max_hold - max_hold**2:
    max_hold -= 1
answer = int(max_hold - min_hold) + 1
print("The second answer is:", answer)