steps = set()
linksaff = {}
linksdep = {}

with open('Day 7/input.txt') as f:
    for line in f:
        step1 = line.split()[1]
        step2 = line.split()[7]
        steps.add(step1)
        steps.add(step2)
        if step1 not in linksaff:
            linksaff[step1] = set()
        linksaff[step1].add(step2)
        if step2 not in linksdep:
            linksdep[step2] = set()
        linksdep[step2].add(step1)

ordered = []
available = steps - set(linksdep.keys())
stack = []

while steps:
    available = sorted(set(available))
    print(steps)
    print(linksaff)
    print(linksdep)
    print(available)
    if available:
        step = available.pop(0)
        print(step)
        steps.remove(step)
        ordered.append(step)
        if len(steps) == 1:
            ordered.append(list(steps)[0])
            break
        for s in linksaff[step]:
            linksdep[s].remove(step)
        del linksaff[step]
        for s in linksdep:
            if not linksdep[s] and s in steps:
                available.append(s)

print(available)
print(linksaff)
print(linksdep)
print(''.join(ordered))

print(ord('A')-64, ord('Z')-64)