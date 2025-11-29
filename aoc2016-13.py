#    Find x*x + 3*x + 2*x*y + y + y*y.
#    Add the office designer's favorite number (your puzzle input).
#    Find the binary representation of that sum; count the number of bits that are 1.
#        If the number of bits that are 1 is even, it's an open space.
#        If the number of bits that are 1 is odd, it's a wall.
fav = 1364
#fav = 10

you = (1,1)
goal = (31,39)
#goal = (7,4)

def isopen(pos, fav):
    x,y = pos
    number = x*x + 3*x + 2*x*y + y + y*y + fav
    binsum = bin(number)
    numbits = binsum.count('1')
    if numbits % 2: # is not dividable by 2
        return(False)
    return(True)

def inside(pos):
    x,y = pos
    return(not(x < 0 or y < 0))

def gotogoal(you, goal, fav):
    final = []
    short = set()
    path = set()
    queue = [(0, you)]
    while queue:
        queue = sorted(queue)
#        print(queue)
        steps, you = queue.pop(0)
        if you not in short and steps <= 50:
            short.add(you)
        path.add((you))

        if you == goal:
            final.append(steps)
            input(steps) # For seeing when we are there.
        x,y = you
        valid = [p for p in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if (inside(p) and isopen(p, fav) and p not in path)]
        for p in valid:
            queue.append((steps+1, p))
        pprint(path, fav)
    return(final, short)
        
def pprint(path, fav):
    print()
    xmax = max(path, key=lambda t: t[0])[0]
    ymax = max(path, key=lambda t: t[1])[1]
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(ymax+1):
        row = ''
        for x in range(xmax+1):
            if isopen((x,y), fav):
                if (x,y) in path:
                    row += 'O'
                else:
                    row += '.'
            else:
                row += '#'
        print(row)    


path = {(1,1)}

print()
ans1, ans2 = gotogoal(you, goal, fav)
print('Day 13, part 1:', min(ans1))
print('Day 13, part 2:', len(ans2))
#pprint(path, fav)

# 102 too high
# 100 too high
# 98 too high