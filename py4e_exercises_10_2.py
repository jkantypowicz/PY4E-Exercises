fname = input('Enter file: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)
dic = dict()

for line in hand:
    if line.startswith('From '):
        words = line.split()
        wrd = words[5]
        wrd_split = wrd.split(':')
        hour = wrd_split[0]
        dic[hour] = dic.get(hour,0) + 1

tmp = list()
x = sorted(dic.items())
for (k,v) in x:
    print(k,v)


