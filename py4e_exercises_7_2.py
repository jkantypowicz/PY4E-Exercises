print('Hello Dumb Dumb')

#file name input
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

#main code block borrowed heavily from discussion board

count = 0
total = 0   
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        #creates a tally of all the times 'X-DSPAM-Confidence:' comes up
        count = count +1
        #extracts the string version of the desired float value by pulling everything past the 20 mark of the 'X-DSPAM-Confidence:' string
        value = line[20:]
        #converts all desired values to floats and creats a sum to be divided by count to get the average
        total = total + float(value)
#print(count,total)
print('Average spam confidence:',total/count)    


