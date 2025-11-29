number = int('3012210')
#number = 5

out = set() # This makes it go fast.

elf = 1
while True:
    left = 1
    while ((elf+left) % number) in out:
        left += 1
    empty = (elf + left) % number
    out.add(empty)
    #print(elf, 'takes from', empty, 'Out now:', len(out))
    if len(out) == number - 1: # We are done, only one left
        print('Day 19, part 1:', elf) # The winning elf.
        break

    elf = empty
    while elf in out:
        elf = (elf + 1) % number

# Part 2.
ingame = list(range(1, number+1))

chair = 0 # Start with number 1, sits on chair 0 from the start.
while True:
    # Find the one to steal from
    eliminate = (chair + (len(ingame) // 2)) % len(ingame)
    #print('left:', ingame, 'this elf', ingame[chair], 'steals from', ingame[eliminate])
    chair = (chair + 1) % len(ingame) # Måste göra det här innan jag poppar, annars blir det fel!
    ingame.pop(eliminate)
    if eliminate < chair: # Hm, det här lirar lite konstigt ihop med felet ovan.
        chair -= 1
    #print('still in game', len(ingame), ingame)
    if len(ingame) == 1:
        print('Day 19, part 2:', ingame[0]) # The winning elf
        break
    if len(ingame) % 10000 == 0:
        print('Number of elfs left:', len(ingame))
    # Koden tar jättelång tid att köra!
