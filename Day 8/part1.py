metadata_list = []

def traverse(number_list, i):
    #print('NODE START', i)
    n_children = number_list[i]
    i += 1
    n_metadata = number_list[i]
    i += 1
    for _ in range(n_children):
        #print('TRAVERSING', n_children)
        #print('TRAVERSE POINT', i)
        j = traverse(number_list, i)
        i += j-i
    for _ in range(n_metadata):
        #print('METADATA', number_list[i])
        metadata_list.append(number_list[i])
        i += 1
    return i

with open('Day 8/input.txt') as f:
    for line in f:
        number_list = list(map(int, line.split()))
        traverse(number_list, 0)
        print(sum(metadata_list))