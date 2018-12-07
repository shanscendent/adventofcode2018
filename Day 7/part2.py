# INCOMPLETE

steps = set()
linksaff = {}
linksdep = {}

with open('Day 7/sample.txt') as f:
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
workers = [0] * 5
timecounter = 0
assigned = [''] * 5
toremove = ''

for i in range(4):
    available = sorted(set(available))
    #print(steps)
    #print(linksaff)
    #print(linksdep)
    #print(available)
    if available :
        print(available)
        for step in available:
            print(step)
            if 0 in workers:
                for n in range(5):
                    if workers[n] == 0:
                        workers[n] += ord(step) - 64
                        assigned[n] = step
                        break
                step = available.pop(0)
                steps.remove(step)
                ordered.append(step)

    print('ASSIGNED', assigned)
    interval = min([x for x in workers if x != 0])

    for n in range(5):
        workers[n] += -interval

    for n in range(5):
        if workers[n] < 0:
            workers[n] = 0
        elif workers[n] == 0 and assigned[n]:
            toremove = assigned[n]
            assigned[n] = ''
    print('NEW WORKERS', workers)
    timecounter += interval
    print(workers)
        #if len(steps) == 1:
        #    ordered.append(list(steps)[0])
        #    break
    step = toremove
    if toremove:
        for s in linksaff[step]:
            linksdep[s].remove(step)
        del linksaff[step]
        for s in linksdep:
            if not linksdep[s] and s in steps:
                print('appending')
                available.append(s)
        toremove = ''

print(available)
print(linksaff)
print(linksdep)
print(''.join(ordered))
print(timecounter)