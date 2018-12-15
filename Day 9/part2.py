players = 458
last_marble = 72019
last_marble = last_marble * 100

i = 0 # marble number
circle = [0]
scores = [0] * players
c = 0 # current position in circle

while i < last_marble:
    for p in range(players):
        i += 1
        if i > last_marble:
            break
        if i % 23 == 0:
            c = (c - 9) % len(circle)
            scores[p] += i + circle.pop(c)
        else:
            circle.insert(c, i)
        
        #print(i, c, circle)
        c = (c + 2) % len(circle)
            
print(max(scores))