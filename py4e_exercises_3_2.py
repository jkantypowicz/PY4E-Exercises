print("Hello Dumb Dumb")

s = input("Enter Score: ")
try:
    sf = float(s)
except:
    print("Error, please enter a proper score")
    quit()
if sf > 10:
    print("Error, please enter a proper score")
elif sf >= 0.9:
    print("A")
elif sf >= 0.8:
    print("B")
elif sf >= 0.7:
    print("C")
elif sf >= 0.6:
    print("D")
elif sf < 0.6:
    print("F")