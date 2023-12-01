import re
with open("day1input.txt") as f:
    data = [x.strip() for x in f.readlines()]
answer = 0
for line in data:    
    left = re.search(r"\d", line)[0]
    right = re.search(r"\d", line[::-1])[0]
    n = int(left + right)
    answer += n
print("The first answer is:", answer)

answer = 0
letters_to_digit = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
for line in data:
    left = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    right = left[-1]
    left = left[0]
    if left.isalpha():
        left = letters_to_digit[left]
    if right.isalpha():
        right = letters_to_digit[right]
    n = int(left + right)
    answer += n
print("The second answer is:", answer)