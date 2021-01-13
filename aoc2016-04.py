with open('aoc2016-04-input.txt') as file:
    code = file.read().strip().split('\n')

def partone():
    sum = 0
    for line in code:
        word = ''.join(line.split('-')[:-1])
        num, check = line.split('-')[-1].replace(']', '').split('[')
        common = set([(word.count(x), x) for x in word])
        common = sorted(list(common), key=lambda v: (-v[0], v[1]))
        five = ''.join([x for (_,x) in common[:5]])
        if five == check:
            sum += int(num)
    return(sum)

def parttwo():
    def decrypt(w, num):
        nw = ''
        shift = num % (122-96)
        for c in w:
            if c == ' ':
                n = c
            elif (ord(c) + shift) > 122:
                n = chr((ord(c) + shift) - (122-96))
            else:
                n = chr(ord(c) + shift)
            nw += n
        return(nw)
    for line in code:
        word = ' '.join(line.split('-')[:-1])
        ID, check = line.split('-')[-1].replace(']', '').split('[')
        nword = decrypt(word, int(ID))
        if 'north' in nword:
            return(ID)

print('Advent of Code 2016, day 4 part 1')
print(partone())
print('Advent of Code 2016, day 4 part 2')
print(parttwo())
