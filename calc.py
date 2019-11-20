import os
import signal

def calculate():
    while True:
        try:
            total = float(input("what is your bill total? (i.e. $22.45) $ "))
            tip = float(input("what is the tip percentage (%)? "))
        except ValueError:
            print("enter a number please")
            continue
        else:
            break
        
    global calc
    calc = (total * (tip / 100)) + total
    print(f'your bill total after a {tip}% tip is ${calc}')
    split()
    return calc

def split():
    t = calc
    while True:
        try:
            ask = input("do you want to split the bill with anyone? type y or n\n > ")
        except ValueError:
            print("type in y or n")
            continue
        if ask not in ['y', 'n']:
            print("type in y or n")
            continue
        else:
            break
        
    if ask == 'y':
        ask2 = int(input("how many people do you want to split the bill with?\n > "))
        final = (t / ask2)
        print("each person's cut is $", final)
    else:
        again()
    again()

def again():
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
        os.kill(os.getpid(),signal.SIGKILL)
        
#TODO: create a menu displaying different available calculations
        
calculate()


