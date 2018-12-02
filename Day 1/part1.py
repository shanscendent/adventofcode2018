freq = 0

with open('Day 1/input.txt') as f:
    for change in f:
        freq += int(change)

print(freq)