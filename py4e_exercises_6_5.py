print('Hello Dumb Dumb')

text = "X-DSPAM-Confidence:    0.8475"
#print(text)
beginning = text.find('0')
#print(beginning)
end = text.find('5')
#print(end)
svalue = text[beginning:end+1]
#print(svalue)
fvalue = float(svalue)
print(fvalue)