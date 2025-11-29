with open('aoc2016-11-input.txt') as file:
    start = file.read().strip().split('\n')

#print(start)

def makemap(text):
    floors = dict()
    for i,row in enumerate(text):
        print(row)
        floor = i + 1
        floors[floor] = set()
        words = row.split(' ')
        for j,word in enumerate(words):
            if word == 'a':
                matter = words[j+1][0].upper()
                thing = words[j+2][0].upper()
                floors[floor].add(matter + thing)
    return(floors)


def issafe(inelevator, checkfloor):
    allthings = inelevator | checkfloor

    for thing in allthings:
    # Om chip utan sin RTG är vid andra RTG, chip kommer att stekas.
        if thing[1] == 'M':
            if not (thing[0] + 'G' in (allthings - {thing})) and \
                any([item[1] == 'G' for item in (allthings - {thing})]):
                return(False)
        return(True)

def canmove(e, themap, direction):
    onfloor = e[0]
    tofloor = onfloor + direction
    if len(e[1]) < 1:
        return(False)
    elif len(e[1]) > 2:
        return(False)
    if tofloor < 1 or tofloor > 4:
        return(False)
    elif issafe(e[1], themap[tofloor]):
        return(True)
    else:
        return(False)

def move(e, themap, direction):
    if canmove(e, themap, direction):
        new = (e[0] + direction, e[1])
        return(new)
    else:
        return(e)

themap = makemap(start)
elevator = (1, set())
print(elevator, themap)
print(issafe({'SG'}, {'TM', 'TG'}))

print(move(elevator, themap, 1))
print(move(elevator, themap, -1))

def run(elevator, themap):
    steps = 0
    done = False
    while not(done):
        if elevator[0] == 4 and all([len(floor) == 0 for floor in [themap[1], themap[2], themap[3]]]):
            # Done!
            return(steps)
