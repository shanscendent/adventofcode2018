# Not working

with open('Day 5/sample1.txt') as f:
    polymer = list(f.readline())

print(len(polymer))

def react(polymer, n):
    if polymer[n].swapcase() == polymer[n+1]:
        #print('ORI', polymer)
        print(n, polymer[n], polymer[n+1])
        del polymer[n]
        del polymer[n]
        print('REM')
    if n >= 0 and polymer[n-1].swapcase() == polymer[n]:
        print('RECURSION')
        react(polymer, n-1)
    return

for n in range(len(polymer)):
    print(n, len(polymer))
    if n+1 >= len(polymer):
        break
    react(polymer, n)

print(''.join(polymer))
print(len(polymer))