with open('aoc2016-02-input.txt') as file:
    code = file.read().strip().split('\n')

def partone():
    def move(num, dir):
        if dir == 'U' and num not in [1,2,3]:
            num -= 3
        elif dir == 'D' and num not in [7,8,9]:
            num += 3
        elif dir == 'R' and num not in [3,6,9]:
            num += 1
        elif dir == 'L' and num not in [1,4,7]:
            num -= 1
        return(num)

    ns = ''
    num = 5
    for line in code:
        for c in line:
            #print(num, c)
            num = move(num,c)
        ns += str(num)
    return(ns)

def parttwo():
    def move(num, dir):
        if dir == 'U' and num not in [5,2,1,4,9]:
            if num in [6,7,8,10,11,12]:
                num -= 4
            elif num in [3,13]:
                num -= 2
        elif dir == 'D' and num not in [5,10,13,12,9]:
            if num in [1,11]:
                num += 2
            elif num in [2,3,4,6,7,8]:
                num += 4
        elif dir == 'R' and num not in [1,4,9,12,13]:
            num += 1
        elif dir == 'L' and num not in [1,2,5,10,13]:
            num -= 1
        return(num)
    
    ns = ''
    num = 5
    for line in code:
        for c in line:
            num = move(num,c)
        if num in [10,11,12,13]:
            n = str(hex(num))[2:]
        else:
            n = str(num)
        ns += n
    return(ns)

print('Advent of Code 2016, day 2 part 1')
print(partone())
print('Advent of Code 2016, day 2 part 2')
print(parttwo())
