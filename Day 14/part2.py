start = 37

def split(number):
    return list(map(int, list(str(number))))

scoreboard = split(start)

check = '503761' # puzzle input

elf1 = 0
elf2 = 1
i = -1
a = 0

while True:
    i += 1
    scoreboard.extend(split(scoreboard[elf1]+scoreboard[elf2]))
    elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
    elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)

    if i % 100000 == 0:
        b = len(scoreboard)
        strboard = ''.join(map(str,scoreboard[a:b]))
        a = b
        print(i)
        if check in strboard:
           break

strboard = ''.join(map(str,scoreboard))
print(strboard.find(str(check)))