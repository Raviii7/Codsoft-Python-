import math

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Cannot divide by zero"
    
def power(x,y):
    return x**y

def square_root(x):
    return math.sqrt(x)

def calculator():

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number (Enter 0 if not needed): "))

    if choice in ('1', '2', '3', '4', '5', '6'):
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = power(num1, num2)
        elif choice == '6':
            result = square_root(num1)
        
        print(f"The result is: {result}")
    else:
        print("Invalid input. Please enter a valid choice.")

calculator()
