with open('aoc2016-21-input.txt') as file:
    instructions = file.read().strip().split('\n')

#print(instructions)

data = 'abcdefgh'
#data = 'abcde'
data = list(data)

def scramble(data):
    for row in instructions:
        #print(data, row)
        row = row.split(' ')
        if row[0] == "swap":
            if row[1] == 'position': # swap position 1 with position 0
                fr_pos, to_pos = int(row[2]), int(row[5])
                fr_ch = data[fr_pos]
                to_ch = data[to_pos]
            else: # swap letter h with letter b
                fr_ch, to_ch = row[2], row[5]
                fr_pos = int(data.index(fr_ch))
                to_pos = int(data.index(to_ch))

            data[fr_pos] = to_ch
            data[to_pos] = fr_ch

        elif row[0] == 'rotate': # rotate right 1 step
            d = -1 # right is default
            if row[1] in ['left', 'right']:
                if row[1] == 'left':
                    d = 1
                amount = int(row[2]) % len(data)
                data = data[amount*d:] + data[:amount*d]

            elif row[1] == 'based': # rotate based on position of letter c
                amount = data.index(row[6])
                if amount >= 4:
                    amount += 1
                amount += 1
                amount = amount % len(data)
                data = data[amount*d:] + data[:amount*d] 
        
        elif row[0] == 'reverse': # reverse positions 1 through 3
            fr, to = int(row[2]), int(row[4])
            data = data[:fr] + data[fr:to+1][::-1] + data[to+1:]

        elif row[0] == 'move': #move position 0 to position 3
            fr, to = int(row[2]), int(row[5])
            ch = data.pop(fr)
            data = data[:to] + [ch] + data[to:]
    return(data)

print('Day 21, part 1:', ''.join(scramble(data)))

# Part 2
data = 'abcdefgh'
#data = 'abcde'
data = list(data)

unscrambled = 'fbgdceah'
unscrambled = list(unscrambled)

import itertools

comb = itertools.permutations(data)

for c in comb:
    if scramble(list(c)) == unscrambled:
        print('Day 21, part 2:', ''.join(c))
        break