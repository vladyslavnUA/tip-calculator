import os
import signal
import math

def welcome():
    #time.sleep(1)
    print()
    print("welcome to the tip calculator. here you will be able to "
          "calculate your total based on the tip percentage and how "
          "many people you want to split it with. created by vladyslav nykoliuk")
    print()
    omenu()
    
#def backone():
    #
    
def calculate():
    #validate user input for float
    while True:
        try:
            total = float(input("what is your bill total? (i.e. $22.45) $ "))
        except ValueError:
            print("please enter a number")
            continue
        else:
            break
        #validate tip percentage
    while True:
        try:
            tip = float(input("what is the tip percentage (%)? "))
        except ValueError:
            print("please enter a number")
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
            if ask not in ['y', 'n']:
                print("type in y or n")
                #will keep asking the user
                continue
        except ValueError:
            print("type in y or n")
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
            if q not in ['y', 'n']:
                print("type in y or n")
                continue
        except ValueError:
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

def about():
    print("about this project")
    print("")
    print("this is a personal project, created by vladyslav nykoliuk, originally published "
          "on github (https://github.com/vladyslavnUA/tip-calculator). if you have any suggestions, "
          "questions or features you would like to add, feel free to open a pull request on my repository")
    print("")

    #validating user input for number
    while True:
        try:
            to_home = int(input("enter any # to go back to the main menu. > "))
            print("")
            
            if to_home == '1':
                welcome()
        except ValueError:
            print("unknown option selected!")
            continue
        else:
            break
    
def omenu():
    print("     ******** MAIN MENU ********          ")
    menu = {}
    menu['   [1]: '] = "calculate total + tip"
    menu['   [2]: '] = "about"
    menu['   [3]: '] = "quit/exit"
    print("")
    while True:
        options = menu.keys()
        sorted(options)
        for entry in options:
            print(entry, menu[entry])
            
        print("")
        selection = input("enter your choice > ")
        
        if selection == '1':
            print("")
            calculate()
        elif selection == '2':
            print("")
            about()
        elif selection == '3':
            print('[ending program...]')
            #ends the program
            os.kill(os.getpid(),signal.SIGKILL)
            break
        else: 
            print("unknown option selected!")
#calculate()
welcome()

