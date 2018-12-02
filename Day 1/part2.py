freq = 0
frequencies = set()
found = False

while not found:
    with open('Day 1/input.txt') as f:
        for change in f:
            freq += int(change)
            if freq in frequencies:
                print(freq)
                found = True
                break
            frequencies.add(freq)