start = 37

def split(number):
    return list(map(int, list(str(number))))

scoreboard = split(start)

n = 503761 # puzzle input
m = 10

elf1 = 0
elf2 = 1

while len(scoreboard)<n+m:
    scoreboard.extend(split(scoreboard[elf1]+scoreboard[elf2]))
    elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
    elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)

print(''.join(map(str, scoreboard[n:n+m])))