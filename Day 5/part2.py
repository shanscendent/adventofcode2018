with open('Day 5/input.txt') as f:
    polymer = list(f.readline().strip())

def strip(polymer, character):
    new_polymer = []
    for n in range(len(polymer)):
        if polymer[n].lower() != character:
            new_polymer.append(polymer[n])
    return new_polymer

def react(polymer):
    new_polymer = []
    for n in range(len(polymer)):
        if len(new_polymer) > 0 and polymer[n].swapcase() == new_polymer[-1]:
            new_polymer.pop()
        else:
            new_polymer.append(polymer[n])
    return new_polymer

lengths = []

for c in range(ord('a'), ord('z')+1):
    stripped_polymer = strip(polymer, chr(c))
    new_polymer = react(stripped_polymer)
    lengths.append(len(new_polymer))

print(min(lengths))