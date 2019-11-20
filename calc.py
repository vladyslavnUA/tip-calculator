def calculate():
    total = float(input("what is your bill total? (i.e. $22.45) $ "))
    tip = float(input("what is the tip percentage (%)? "))
    global calc
    calc = (total * (tip / 100)) + total
    print(f'your bill total after a {tip} % tip is ${calc}')
    split()
    return calc
