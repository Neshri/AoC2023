import math

with open("day2input.txt") as f:
    data = [x.strip() for x in f.readlines()]

# 12 red, 13 green, 14 blue
test_amount = {"red": 12, "green": 13, "blue": 14}
answer = 0
answer_two = 0
for i in range(len(data)):
    minimum_colors = {"red": 0, "green": 0, "blue": 0}
    game = data[i].split(":")[1].split(";")
    for turn in game:
        for color in turn.split(","):
            number, color = color.strip().split(" ")
            number = int(number)
            if number > minimum_colors[color]:
                minimum_colors[color] = number
    possible = True
    for color in test_amount.keys():
        if minimum_colors[color] > test_amount[color]:
            possible = False
            break
    if possible:
        answer += (i + 1)
    answer_two += math.prod(minimum_colors.values())

print("The first answer is:", answer)
print("The second answer is:", answer_two)