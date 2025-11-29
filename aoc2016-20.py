with open('aoc2016-20-input.txt') as file:
    numbers = sorted([tuple(map(int, row.split('-'))) for row in file.read().strip().split('\n')])

#print(numbers)

# Välj högsta talet i range +1.
# Kolla i nästa range. MEN den kan ju vara inuti en range ...
# Får sortera på vad rangerna slutar på? OCH börjar på ...

end = 4294967295
lowest = 0
i = 0

all_ip = []
#all_ip.append(lowest)


while any([lowest in range(row[0], row[1]+1) for row in numbers]):
    lowest = numbers[i+1][1]+1
    i += 1
print('Day 20, part 1:', lowest)

# Alternative version.
lowest = 0
i = 0
while True:
    if lowest < numbers[i][0]:
        break
    lowest = max(numbers[i][1]+1, lowest)
    i +=1
print('Day 20, part 1:', lowest)

# Part 2

def findlowest(ranges, lowest, i):
    while i < len(ranges) and lowest < end:
        if lowest < ranges[i][0]:
            return(lowest, i)
        lowest = max(ranges[i][1]+1, lowest)
        i += 1
    return(lowest, i)

start = 0
eaten = 0
lowlist = []
while True:
    number, eaten = findlowest(numbers, start, eaten)
    if number >= end:
        break
    lowlist.append(number)
    start = number + 1

print('Day 20, part 2:', len(lowlist))