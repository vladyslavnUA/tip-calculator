import os
import signal

def calculate():
    #validate user input for float
    while True:
        try:
            total = float(input("what is your bill total? (i.e. $22.45) $ "))
            tip = float(input("what is the tip percentage (%)? "))
        except ValueError:
            print("enter a number please")
            continue
        else:
            break
    #global calc is available throughout the script
    global calc
    #entire calculation
    calc = (total * (tip / 100)) + total
    round(calc, 2)
    print(f'your bill total after a {tip}% tip is ${calc}')
    split()
    #return calc so it can be user later
    return calc

def split():
    t = calc
    #validate user input for letter
    while True:
        try:
            ask = input("do you want to split the bill with anyone? type y or n\n > ")
        except ValueError:
            print("type in y or n")
            continue
        if ask not in ['y', 'n']:
            print("type in y or n")
            #will keep asking the user
            continue
        else:
            break
    #calculating total with # of people
    if ask == 'y':
        while True:
            try:
                ask2 = int(input("how many people do you want to split the bill with?\n > "))
                break
            except ValueError:
                print("please enter an integer. (hint: an integer has no decimals)")
                continue
            else:
                break
        final = (t / ask2)
        #rounding to two decimals
        round(final, 2)
        print("each person's cut is $", final)
    else:
        again()
    again()

def again():
    #validating user input for letter
    while True:
        try:
            q = input("do you want to calculate the tip again? (y or n)\n > ")
        except ValueError:
            print("type in y or n")
            continue
        if ask not in ['y', 'n']:
            print("type in y or n")
            continue
        else:
            break
        
    if q == 'y':
        calculate()
    else:
        print('[ending program...]')
        #ends the program
        os.kill(os.getpid(),signal.SIGKILL)
        
#TODO: create a menu displaying different available calculations
        
calculate()


