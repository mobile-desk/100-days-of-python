def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b




def calc(a,b):
    aa = add(a,b) 
    ss = subtract(a,b)
    mm = multiply(a,b) 
    dd = divide(a,b) 

    r = f"For {a} and {b} as case studies: {a} + {b} = {aa}, {a} - {b} = {ss}, {a} * {b} = {mm}, {a} / {b} = {dd}"
    return r


a = float(input("Enter your value here: "))
b = float(input("Enter your value here: "))

print(calc(a, b))