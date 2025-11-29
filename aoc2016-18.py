with open('aoc2016-18-input.txt') as file:
    startrow = file.read().strip().split('\n')[0]

# safe tiles (.) and traps (^)

# Trap if either of these:
#    Its left and center tiles are traps, but its right tile is not.
#    Its center and right tiles are traps, but its left tile is not.
#    Only its left tile is a trap.
#    Only its right tile is a trap.

def nextrow(row):
    row2 = ''
    for i in range(len(row)):
        center = row[i]
        if i == 0:
            left = '.'
            right = row[i+1]
        elif i == len(row) - 1:
            left = row[i-1]
            right = '.'
        else:
            left = row[i-1]
            right = row[i+1]
        tiles = left + center + right
        #print(tiles)

        if tiles in ['^^.', '.^^', '^..', '..^']:
            row2 += '^'
        else:
            row2 += '.'
    return(row2)

#row = '..^^.' # Test
#row = '.^^.^.^^^^' # Test
safe = 0
row = startrow
for i in range(40):
    safe += sum([1 for c in row if c == '.'])
    print(row)
    row = nextrow(row)
print('Day 18, part 1:', safe)

safe = 0
row = startrow
for i in range(400000):
    safe += sum([1 for c in row if c == '.'])
    #print(row)
    row = nextrow(row)
print('Day 18, part 2:', safe)
