import re
file = open('regex_sum_1633416.txt')
numlist = list()
for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    for x in numbers:
        num = int(x)
        numlist.append(num)
print(sum(numlist))