with open('aoc2016-06-input.txt') as file:
    code = file.read().strip().split('\n')

import collections
result = {}

def partone():
    global result
    for i in range(len(code[0])):
        result[i] = collections.Counter()
    for line in code:
        for i,c in enumerate(line):
            result[i][c] += 1

    word = ''
    for i in range(len(result)):
        word += result[i].most_common(1)[0][0]
    return(word)

def parttwo():
    word = ''
    for i in range(len(result)):
        word += result[i].most_common()[-1][0]
    return(word)

print('Advent of Code 2016, day 6 part 1')
print(partone())
print('Advent of Code 2016, day 6 part 2')
print(parttwo())
