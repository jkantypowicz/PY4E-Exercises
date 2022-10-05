fname = open('mbox-short.txt')

lst = list()

for line in fname:
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue
    words = line.split()
    lst.append(words[1])
    print(words[1])
print('There were',len(lst),'lines in the file with from as the first word') 



