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
        self.minute = 0

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

times = []

for ID in guards:
    sleep = guards[ID].sleep
    wake = guards[ID].wake
    counter = [0] * 60

    for n in range(len(sleep)):
        for m in range(sleep[n].minute, wake[n].minute):
            counter[m] += 1
    times.append([max(counter), ID])
    guards[ID].minute = counter.index(max(counter))

chosen = max(times)[1]
minute = guards[chosen].minute

print(chosen * minute)