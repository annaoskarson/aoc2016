import hashlib
code = 'rrrbmfta'
#code = 'hijkl'
#code = 'ihgpwlah'

doors = hashlib.md5((code).encode())

# up, down, left, right
# b, c, d, e, or f means open
# other means closed and locked

def inside(p):
    xmin, xmax, ymin, ymax = (0, 3, 0, 3)
    x,y = p
    return(xmin <= x <= xmax and ymin <= y <= ymax)

def isopen(room):
    checkopen = hashlib.md5((room).encode()).hexdigest()[:4]
    # up, down, left, right
    op = ''
    for i,x in enumerate(checkopen):
        if x in 'bcdef':
            op += '1'
        else:
            op += '0'
    return(op)

def walk(start, goal):
    queue = [(0, start, '')]
    while queue:
        queue = sorted(queue)
        steps, pos, path = queue.pop(0)
        if pos == goal:
            return(path)
        
        x,y = pos
        opendoors = isopen(code + path)
        # Check if it is possible to go there, if it is inside
        # up, down, left, right
        dir_char = 'UDLR'
        dirs = [(0,-1), (0,1), (-1,0), (1,0)]
        for i,d in enumerate(opendoors):
            to = (x + dirs[i][0], y + dirs[i][1])
            if d == '1' and inside(to):
                queue.append((steps + 1, to, path + dir_char[i]))

start = (0,0)
goal = (3,3)

path = walk(start, goal)
#l = max(paths, key=len)  
print('Day 17, part 1:', path)
#print('Day 17, part 2:', len(l)) 
#print(walk(start, goal))

def walk2(start, goal, longest):
    queue = [(0, start, '')]
    while queue:
        #queue = sorted(queue)
        steps, pos, path = queue.pop(0)
        if pos == goal:
            if steps > longest:
                longest = steps
                print(longest, len(queue))
        
        else: # Still alive!
            x,y = pos
            opendoors = isopen(code + path)
            # Check if it is possible to go there, if it is inside
            # up, down, left, right
            dir_char = 'UDLR'
            dirs = [(0,-1), (0,1), (-1,0), (1,0)]
            for i,d in enumerate(opendoors):
                to = (x + dirs[i][0], y + dirs[i][1])
                if d == '1' and inside(to):
                    queue.append((steps + 1, to, path + dir_char[i]))
    return(longest)


longest = walk2(start, goal, 0)
print('Day 17, part 2:', longest)
