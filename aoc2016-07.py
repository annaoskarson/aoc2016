with open('aoc2016-07-input.txt') as file:
    code = file.read().strip().split('\n')

def partone():
    def good(ls):
        i = 0
        valid = False
        ok = True
        while i in range(len(ls)-3):
            if ls[i] == '[':
                ok = False
            elif ls[i] == ']':
                ok = True
            if ls[i+1] == ls[i+2] and ls[i] == ls[i+3] and ls[i+1] != ls[i] and ok:
                valid = True
            if ls[i+1] == ls[i+2] and ls[i] == ls[i+3] and ls[i+1] != ls[i] and not ok:
                return(False)
            i += 1
        return(valid)

    TLS = [line for line in code if good(line)]
    return(len(TLS))

def parttwo():
    def good(ls):
        hypernet = []
        supernet = True
        apas = []
        i = 0
        while i in range(len(ls)):
            if ls[i] == '[':
                start = i
                supernet = False
            if ls[i] == ']':
                hypernet.append((start,i))
                supernet = True
            if i < len(ls) - 2:
                if ls[i] == ls[i+2] and ls[i+1] != ls[i] and supernet:
                    apas.append(ls[i+1] + ls[i] + ls[i+1])
            i += 1
        for apa in apas:
            for (start,stop) in hypernet:
                if apa in ls[start:stop+1]:
                    return(True)
    SSL = [line for line in code if good(line)]
    return(len(SSL))

print('Advent of Code 2016, day 7 part 1')
print(partone())
print('Advent of Code 2016, day 7 part 2')
print(parttwo())
