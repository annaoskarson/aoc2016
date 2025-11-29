import hashlib, re

salt = 'cuanljph'
#salt = 'abc'

hashtable = {}
hashtable2016 = {}

# Could do a fivetable, with index and fivecharacters. Like fivetable[3] = ['4', 'e']
# More usable the other way, maybe ...
# fivetable['e'] = [3, 513, 8382]

# To generate keys, you first get a stream of random data by taking the MD5 of a pre-arranged salt (your puzzle input) 
# and an increasing integer index (starting with 0, and represented in decimal); 
# the resulting MD5 hash should be represented as a string of lowercase hexadecimal digits.
def generate(stuff):
    global hashtable
    #print(len(hashtable))
    if stuff in hashtable:
        return(hashtable[stuff])
    key = hashlib.md5((stuff).encode())
    hashtable[stuff] = key.hexdigest()
    return(key.hexdigest())

#    It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
#    One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.

def three(key):
    three = [match.group() for match in re.finditer(r'(.)\1{2,2}', key)]#[0][0]
    if three:
        return(three[0][0])
    else:
        return(None)

def five(key, value):
    #print(value)
#    five = [match.group() for match in re.finditer(r'(.)\1{4,}', key)]
    five = re.search(r'' + value + '{5}', key)
    #print(five)
    if five:
        return(True)
    else:
        return(None)

dig = 0
fives = []
while True:
    this = generate(salt + str(dig))
    #print('this', this)
    triplet = three(this)
    if triplet:
        #print('triplet', dig, triplet)        
        for j in range(dig+1, dig + 1001):
            that = generate(salt + str(j))
            if five(that, triplet):                
                fives.append(dig)
                #print('five', len(fives), dig, j, triplet, this, that)
                break
    #print(len(fives))
    if len(fives) == 64:
        print('Day 14, part 1:', fives[-1])
        #input(fives[-1])
        break
    dig += 1

# PART 2

dig = 0
fives = []
while True:
    start = generate(salt + str(dig))
    this = start
    if start in hashtable2016:
        this = hashtable2016[start]
    else:
        for times in range(2016):
            this = generate(this)
        hashtable2016[start] = this

    triplet = three(this)
    if triplet:
        #print('triplet', dig, triplet)        
        for j in range(dig+1, dig + 1001):            
            start = generate(salt + str(j))
            that = start
            if start in hashtable2016:
                that = hashtable2016[start]
            else:
                for times in range(2016):
                    that = generate(that)
                hashtable2016[start] = that

            if five(that, triplet):
                fives.append(dig)
                #print('five', len(fives), dig, j, triplet, this, that)
                break

    if len(fives) == 64:
        print('Day 14, part 2:', fives[-1])
        #print(fives[-1])
        break
    dig += 1
