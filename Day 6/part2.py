coords = []

with open('Day 6/input.txt') as f:
    for line in f:
        coord = tuple(map(int, line.split(',')))
        coords.append(coord)

size = [0, 0]
size[0] = max([x[0] for x in coords])+1
size[1] = max([x[1] for x in coords])+1

counter = 0

for m in range(size[0]):
    for n in range(size[1]):
        dist_total = 0
        for coord in coords:
            dist_total += abs(coord[0]-m)+abs(coord[1]-n)
        if dist_total < 10000:
            counter += 1

print(counter)