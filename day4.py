import re

with open("day4input.txt") as f:
    data = [x.strip() for x in f.readlines()]

answer = 0
for id, card in enumerate(data):
    winning_numbers, actual_numbers = [x.strip() for x in card.split(":")[1].strip().split("|")]
    winning_numbers = [int(x) for x in re.split(r" +", winning_numbers)]
    actual_numbers = [int(x) for x in re.split(r" +", actual_numbers)]
    data[id] = (winning_numbers, actual_numbers)
    winning_numbers = set(winning_numbers)
    points = 0
    for n in actual_numbers:
        if n in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    answer += points

print("The first answer is:", answer)

cards = []
for i in range(len(data)-1, -1, -1):
    s = set(data[i][0])
    wins = 0
    for n in data[i][1]:
        if n in s:
            wins += 1
    card_sum = 0
    for j in range(wins):
        card_sum += cards[j]
    cards.insert(0, card_sum+1)

print("The second answer is:", sum(cards))