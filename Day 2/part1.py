twos = 0
threes = 0

with open('Day 2/input.txt') as f:
    for boxes in f:
        letters = list(set(boxes.strip()))
        counts = set()
        for letter in letters:
            counts.add(boxes.count(letter))
        if 2 in counts:
            twos += 1
        if 3 in counts:
            threes += 1

checksum = twos * threes
print(checksum)