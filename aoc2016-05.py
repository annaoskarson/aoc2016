import hashlib

code = 'cxdnnyjw'

def partone():
    passw = ''
    num = 0
    while len(passw) < 8:
        md5sum = hashlib.md5(code+str(num)).hexdigest()
        if md5sum[:5] == '00000':
            passw += str(md5sum[5])
        num += 1
    return(passw)

def parttwo():
    passw = ['','','','','','','','']
    num = 0
    length = 0
    while length < 8:
        md5sum = hashlib.md5(code+str(num)).hexdigest()
        if md5sum[:5] == '00000' and md5sum[5].isdigit() and int(md5sum[5]) in range(0,8):
            if passw[int(md5sum[5])] == '':
                passw[int(md5sum[5])] = str(md5sum[6])
                length += 1
        num += 1
    return(''.join(passw))

print('Advent of Code 2016, day 5 part 1')
print(partone())
print('Advent of Code 2016, day 5 part 2')
print(parttwo())
