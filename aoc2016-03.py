with open('aoc2016-03-input.txt') as file:
    code = file.read().strip().split('\n')

def partone():
    possible = 0
    for line in code:
        #print(line.strip().split(' '))
        [a,b,c] = [int(x) for x in line.strip().split(' ') if x != '']
        if (a+b > c) and (a+c > b) and (b+c > a):
            possible += 1
    return(possible)

def parttwo():
    def tri(a,b,c):
        return((a+b > c) and (a+c > b) and (b+c > a))

    possible = 0
    for i,line in enumerate(code):
        if i%3 == 0:
            [a1,b1,c1] = [int(x) for x in line.strip().split(' ') if x != '']
        elif i%3 == 1:
            [a2,b2,c2] = [int(x) for x in line.strip().split(' ') if x != '']
        elif i%3 == 2:
            [a3,b3,c3] = [int(x) for x in line.strip().split(' ') if x != '']
            if tri(a1,a2,a3):
                possible += 1
            if tri(b1,b2,b3):
                possible += 1
            if tri(c1,c2,c3):
                possible += 1
    return(possible)

print('Advent of Code 2016, day 3 part 1')
print(partone())
print('Advent of Code 2016, day 3 part 2')
print(parttwo())
