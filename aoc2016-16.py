state = '00101000101111010'

#    Call the data you have at this point "a".
#    Make a copy of "a"; call this copy "b".
#    Reverse the order of the characters in "b".
#    In "b", replace all instances of 0 with 1 and all 1s with 0.
#    The resulting data is "a", then a single 0, then "b".

def dragoncurve(value):
    a = value
    b = value[::-1]
    b = ''.join(['1' if x == '0' else '0' for x in b])
    return(a + '0' + b)

def checksum(value):
    # check each non-overlapping pair
    # if two of the same -> 1
    # else -> 0
    thesum = ''
    i = 0
    while i+1 < len(value):
        checking = value[i:i+2]
        if checking[0] == checking[1]:
            thesum += '1'
        else:
            thesum += '0'
        i += 2
    return(thesum)

def make_checksum(value):
    checking = checksum(value)
    while not(len(checking) % 2): # True if even
        checking = checksum(checking)
    return(checking)

def lengthen(value, size):
    while len(value) < size:
        value = dragoncurve(value)
    return(value[:size+1])

size = 272
#size = 20 # example
start = '00101000101111010'
#start = '10000' # example

value = lengthen(start, size)
chk = make_checksum(value)
print('Day 16, part 1:', chk)

size = 35651584 # Part 2 size
value = lengthen(start, size)
chk = make_checksum(value)
print('Day 16, part 2:', chk)


