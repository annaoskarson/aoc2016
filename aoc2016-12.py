with open('aoc2016-12-input.txt') as file:
    code = file.read().strip().split('\n')

#    cpy x y copies x (either an integer or the value of a register) into register y.
#    inc x increases the value of register x by one.
#    dec x decreases the value of register x by one.
#    jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.

def run(registers):
    i = 0
    while i < len(code):
        row = code[i]
        command, arguments = row.split(' ', 1)
        if command == 'cpy':
            x, y = arguments.split(' ')
            if x.isalpha():
                value = registers[x]
            else:
                value = int(x)
            registers[y] = value
            i += 1
        elif command == 'inc':
            registers[arguments] += 1
            i += 1
        elif command == 'dec':
            registers[arguments] -= 1
            i += 1
        elif command == 'jnz':
            x, y = arguments.split(' ')
            if (x.isalpha() and registers[x] != 0) or (x.isnumeric() and x != 0):
                value = int(y)
                i += value
            else:
                i += 1
    return(registers['a'])

registers = {'a': 0, 'b': 0, 'c':0, 'd':0}
print('Day 12, part 1:', run(registers))

registers = {'a': 0, 'b': 0, 'c':1, 'd':0}
print('Day 12, part 2:', run(registers))
