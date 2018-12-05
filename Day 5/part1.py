# Tried recursion in part1fail.py, could not get it to work. Part 1 algorithm from meithan on reddit
# https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4iuqo/

with open('Day 5/input.txt') as f:
    polymer = list(f.readline().strip())

def react(polymer):
    new_polymer = []
    for n in range(len(polymer)):
        if len(new_polymer) > 0 and polymer[n].swapcase() == new_polymer[-1]:
            new_polymer.pop()
        else:
            new_polymer.append(polymer[n])
    return new_polymer

new_polymer = react(polymer)

print(len(new_polymer))