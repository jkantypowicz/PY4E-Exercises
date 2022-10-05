print("Hello Dumb Dumb")

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
reg = fh * fr
otp = (fh - 40) * (fr * 0.5)
if fh > 40:
    print("Overtime ", reg + otp)
    
else:
    print("Regular ", reg)
    