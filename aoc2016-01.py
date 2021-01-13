with open('aoc2016-01-input.txt') as file:
    intext = file.read().strip().split(',')

#intext = ['R5', 'L5', 'R5', 'R3'] #12
#intext = ['R2', 'R2', 'R2'] #2
#intext = ['R8', 'R4', 'R4', 'R8']

two = 0
def partone():
    global two
    first = True
    face = 0
    x, y = 0, 0
    been = [(x, y)]
    for dir in intext:
        dir = dir.strip()
        turn = dir[0]
        go = int(dir[1:])
        if turn == 'L':
            face = (face - 90) % 360
        elif turn == 'R':
            face = (face + 90) % 360

        for step in range(1, go+1):
            if face == 0:
                y += 1
            elif face == 90:
                x += 1
            elif face == 180:
                y -= 1
            elif face == 270:
                x -= 1
            if (x,y) in been and first:
                two = abs(x) + abs(y)
                first = False
            been.append((x,y))

    return(abs(x) + abs(y))

print('Advent of Code 2016, day 1 part 1')
print(partone())
print('Advent of Code 2016, day 1 part 2')
print(two)
