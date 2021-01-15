with open('aoc2016-08-input.txt') as file:
    code = file.read().strip().split('\n')

def partone():
    maxx, maxy = 50, 6
    lights = set()
    for line in code:
        if line.startswith('rect'):
            x, y = map(int, line.split(' ')[1].split('x'))
            for h in range(0,x):
                for v in range(0,y):
                    lights.add((h,v))
        elif line.startswith('rotate column'):
            x, num = map(int, [line.split(' ')[2][2:], line.split(' ')[-1]])
            minus = set()
            plus = set()
            for (x1,y1) in lights:
                if x1 == x:
                    y = (y1 + num) % maxy
                    minus.add((x1,y1))
                    plus.add((x,y))
            lights = lights - minus | plus
        elif line.startswith('rotate row'):
            y, num = map(int, [line.split(' ')[2][2:], line.split(' ')[-1]])
            minus = set()
            plus = set()
            for (x1,y1) in lights:
                if y1 == y:
                    x = (x1 + num) % maxx
                    minus.add((x1,y1))
                    plus.add((x,y))
            lights = lights - minus | plus

    return(lights)

one = partone()

def parttwo(lights):
    text = ''
    for y in range(0, 6):
        row = ''
        for x in range(0,50):
            if (x,y) in lights:
                pixel = 'M'
            else:
                pixel = ' '
            row += pixel
        text = text + row + '\n'
    return(text)

print('Advent of Code 2016, day 7 part 1')
print(len(one))
print('Advent of Code 2016, day 7 part 2')
print(parttwo(one))
