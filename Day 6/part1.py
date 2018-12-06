coords = []
coord_dict = {}

with open('Day 6/input.txt') as f:
    for line in f:
        coord = tuple(map(int, line.split(',')))
        coords.append(coord)
        coord_dict[coord] = []

size = [0, 0]
size[0] = max([x[0] for x in coords])+1
size[1] = max([x[1] for x in coords])+1

infinite_set = set()

for m in range(size[0]):
    for n in range(size[1]):
        dist_list = []
        for coord in coords:
            dist_list.append(abs(coord[0]-m)+abs(coord[1]-n))
        sorted_dist_list = sorted(dist_list)
        if sorted_dist_list[0] != sorted_dist_list[1]:
            coord = coords[dist_list.index(sorted_dist_list[0])]
            coord_dict[coord].append(tuple([m,n]))
            if m == 0 or n == 0 or m == size[0]-1 or n == size[1]-1:
                infinite_set.add(coord)

areas = []

for coord in coord_dict:
    if coord not in infinite_set:
        areas.append(len(coord_dict[coord]))

print(max(areas))