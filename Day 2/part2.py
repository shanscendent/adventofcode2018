ID_list = []
ID_set = []

with open('Day 2/input.txt') as f:
    for boxes in f:
        letters = list(boxes.strip())
        ID_list.append(letters)
        letters = set(letters)
        ID_set.append(letters)

for i in range(len(ID_set)-1):
    for j in range(i+1, len(ID_set)):
        diff = ID_set[i].difference(ID_set[j])
        if len(diff) == 1:
            box1 = ID_list[i]
            box2 = ID_list[j]
            index = []
            for k in range(len(box1)):
                if box1[k] != box2[k]:
                    index.append(k)
            if len(index) == 1:
                box1.pop(index[0])
                print(''.join(box1))