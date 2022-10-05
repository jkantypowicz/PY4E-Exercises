fname = input('Enter file: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)
dic = dict()

for line in hand:
    if not line.startswith('From'): continue
    if line.startswith('From:'):
        words = line.split()
        sender = words[1]
        dic[sender] = dic.get(sender,0) + 1

bigcount = None
bigword = None
for word,count in dic.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)



