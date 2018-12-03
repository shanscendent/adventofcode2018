claims = []

with open('Day 3/input.txt') as f:
    for line in f:
        line = line.strip()
        temp1 = line.split(' @ ')
        temp2 = temp1[1].split(': ')
        ID = temp1[0][1:]
        left = temp2[0].split(',')[0]
        top = temp2[0].split(',')[1]
        wide = temp2[1].split('x')[0]
        tall = temp2[1].split('x')[1]
        claims.append(list(map(int, [ID, left, top, wide, tall])))

w_list = []
h_list = []

for claim in claims:
    w_list.append(claim[1] + claim[3])
    h_list.append(claim[2] + claim[4])

w = max(w_list)
h = max(h_list)
fabric = [[0] * h for x in range(w)]

for claim in claims:
    a = claim[1]
    b = claim[1] + claim[3]
    c = claim[2]
    d = claim[2] + claim[4]
    for n in range(a, b):
        for m in range(c, d):
            fabric[n][m] += 1

count = 0

for row in fabric:
    for item in row:
        if item >=2:
            count += 1

print(count)