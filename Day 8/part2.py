metadata_list = []
metadata_dict = {}
child_dict = {}

def traverse(number_list, i):
    node = i
    metadata_dict[node] = []
    child_dict[node] = []
    n_children = number_list[i]
    i += 1
    n_metadata = number_list[i]
    i += 1
    for _ in range(n_children):
        child_dict[node].append(i)
        j = traverse(number_list, i)
        i += j-i
    for _ in range(n_metadata):
        metadata_list.append(number_list[i])
        metadata_dict[node].append(number_list[i])
        i += 1
    return i

with open('Day 8/input.txt') as f:
    for line in f:
        number_list = list(map(int, line.split()))
        traverse(number_list, 0)

def traversevalue(child_dict, metadata_dict, node):
    value = 0

    for entry in metadata_dict[node]:
        if entry-1 < len(child_dict[node]):
            value += traversevalue(child_dict, metadata_dict, child_dict[node][entry-1])
        elif not child_dict[node]:
            value += entry
    return value

value = traversevalue(child_dict, metadata_dict, 0)
print(value)