#WAF to print the length of a list.(list is a parameter)
from math import factorial


cities = ["Mumbai", "Pune", "Banglore", "Chennai", "Nagpur"]
heroes = ["Thor", "Ironman", "Captain America", "Jalaj Kamat"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes)
  



#WAP to print the elements of a list in a single line. (list is the parameter)
cities = ["Mumbai", "Pune", "Banglore", "Chennai", "Nagpur"]
heroes = ["Thor", "Ironman", "Captain America", "Jalaj Kamat"]
def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(cities)
print() #for a new line after printing cities
print_list(heroes)




#WAP to find the factorial of n.(n is the parameter)
print()
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(5)




#WAP to convert USD into INR.
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")
converter(100)




#WAP to take input and print the string ODD if the number in the input is odd else print string EVEN.
num = int(input("Enter a number:"))

def odd_even(n):
    if n%2 == 0:
        print("EVEN")
    else:
        print("ODD")

odd_even(num)




#CALCULATOR
def add(a, b):
    sum = a+b
    return sum

def subtract(a, b):
    diff = a-b
    return diff

def multiply(a, b):
    mul = a*b
    return mul

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def average(a, b):
    avg = (a+b)/2
    return avg

def calculator():
    print("--- Python Calculator ---")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Average")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print(f"Sum of 2 numbers is: {a} + {b} = {add(a, b)}")
        elif choice == '2':
            print(f"Difference of 2 numbers is: {a} - {b} = {subtract(a, b)}")
        elif choice == '3':
            print(f"Multiplication of 2 numbers is: {a} * {b} = {multiply(a, b)}")
        elif choice == '4':
            result = divide(a, b)
            print(f"Division of 2 numbers is: {a} / {b} = {result}")
        elif choice == '5':
            print(f"Average of {a} and {b} is {average(a, b)}")
    else:
        print("Invalid Input")

calculator()  # Run the calculator
