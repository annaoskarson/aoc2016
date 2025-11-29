with open('aoc2016-15-input.txt') as file:
    code = file.read().strip().split('\n')

discs = {}
for row in code:
    disc_id = int(row.split(' ')[1][1])
    disc_max = int(row.split(' ')[3])
    disc_start = int(row.split(' ')[-1][0])
    discs[disc_id] = (disc_start, disc_max)

def positions(time):
    pos = []
    for dn in discs:
        d_start, d_max = discs[dn]
        pos.append((d_start + time + dn) % d_max)
    return(pos)

t = 0
while True:
    state = positions(t)
    if all(val == 0 for val in state):
        print('Day 15, part 1:', t)
        break
    t += 1

discs[len(discs)+1] = (0, 11)

t = 0
while True:
    state = positions(t)
    #print(state)
    if all(val == 0 for val in state):
        print('Day 15, part 2:', t)
        break
    t += 1
