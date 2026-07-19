def sum(a,b):
        return a+b
def dif(a,b):
        return a-b
def mul(a,b):
        return a*b
def div(a,b):
        return a/b
def avg(a,b):
        return ((a+b)/2)
def calculator():
        a = int(input("enter the first number: "))
        b = int(input("Enter the second number: "))
        op = input("Enter a choice: 1.Sum  2.Difference  3.Multiplication  4.Division  5.Average: ")
        if(op == '1'):
                print(f"sum of two numbers is {sum(a,b)}")
        elif(op == '2'):
                print(f"Difference of the two number is {dif(a,b)}")
        elif(op == '3'):
                print(f"Multiplication of the two numbers is {mul(a,b)}")
        elif(op == '4'):
                print(f"Division of two numbers is {div(a,b)}")
        elif(op == 5):
                print(f"The average of the two numbers is {avg(a,b)}")
        else:
                print("Invalid number or operator")
calculator()
