def calculate():
    total = float(input("what is your bill total? (i.e. $22.45) $ "))
    tip = float(input("what is the tip percentage (%)? "))
    global calc
    calc = (total * (tip / 100)) + total
    print(f'your bill total after a {tip} % tip is ${calc}')
    split()
    return calc

def split():
    t = calc
    ask = input("do you want to split the bill with anyone? type y or n\n > ")
    if ask == 'y':
        ask2 = int(input("how many people do you want to split the bill with?\n > "))
        final = (t / ask2)
        print("each person's cut is $", final)

#TODO: define again(), allowing users to calculate again
def again():
    q = input("do you want to calculate the tip again? (y or n)\n > ")
    if q == 'y':
        print('\n')
        calculate()
    else:
        ####
        
#TODO: create a menu displaying different available calculations
        
calculate()


