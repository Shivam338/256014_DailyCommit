def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

def remainder(x,y):
    return x%y

def exponential(x,y):
    return x**y ;

def selection(n,x,y):
    switcher={
        1: addition(x,y),
        2: subtraction(x,y),
        3: multiplication(x,y),
        4: division(x,y),
        5: remainder(x,y),
        6: exponential(x,y)
    }
    print(switcher.get(n,"Invalid"))

print("Press \n1. For Addition\n2. For Subtraction\n3. For Multiplication\n4. For Division\n5. For Remainder\n6. For Exponential")

operator=int(input("Enter your Choice : "))
x=int(input("Enter 1st no."))
y=int(input("Enter 2nd no."))
selection(operator,x,y)
