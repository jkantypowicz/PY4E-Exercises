print('Hello Dumb Dumb')
#None acts as a blank entry
largest = None
smallest = None
while True:
    sval = input('Enter Number: ')
    if sval == 'done':
        break
    #clever solution from disscussion to add the else here
    else:
        try:
            fval = float(sval)
            #largest is equal to a blank value here so fval gets assigned to largest
            if largest is None:
                largest = fval
            #on the next runthrough of the loop, this checks to see if the new input is larger than the previous one. If so, it takes the largest spot 
            elif fval > largest:
                largest = fval
            #works the exact same as the largest set up
            if smallest is None:
                smallest = fval
            elif fval < smallest:
                smallest = fval
        except:
            print('Invalid input')
print(largest, smallest)

