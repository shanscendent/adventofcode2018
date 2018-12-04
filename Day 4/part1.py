import datetime

record = []

with open('Day 4/input.txt') as f:
    for line in f:
        date_time_str = line[1:17]
        activity = line[19:-1]
        if activity == 'wakes up':
            guard_id = 0
            action = 'wakes'
        elif activity == 'falls asleep':
            guard_id = 0
            action = 'sleeps'
        else:
            guard_id = int(activity.split(' ')[1][1:])
            action = ''
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        record.append({'time':date_time_obj, 'action':action, 'id':guard_id})

record = sorted(record, key=lambda entry: entry['time'])

class Guard():
    def __init__(self, ID):
        self.ID = ID
        self.sleep = []
        self.wake = []
        self.asleep = 0

guards = {}

for entry in record:
    time = entry['time']
    action = entry['action']
    if action == '':
        ID = entry['id']
        if ID not in guards:
            guards[ID] = Guard(ID)
    elif action == 'sleeps':
        guards[ID].sleep.append(time)
    elif action == 'wakes':
        guards[ID].wake.append(time)
        pass

chosen = [0, 0]

for ID in guards:
    guard = guards[ID]
    for n in range(len(guard.sleep)):
        delta = guard.wake[n] - guard.sleep[n]
        minutes = int(delta.seconds/60)
        guard.asleep += minutes
    if chosen[1] < guard.asleep:
        chosen[0] = ID
        chosen[1] = guard.asleep

sleep = guards[chosen[0]].sleep
wake = guards[chosen[0]].wake
counter = [0] * 60

for n in range(len(sleep)):
    for m in range(sleep[n].minute, wake[n].minute):
        counter[m] += 1

minute = counter.index(max(counter))

print(chosen[0] * minute)