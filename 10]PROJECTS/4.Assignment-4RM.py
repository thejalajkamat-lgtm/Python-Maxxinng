#Write a Python program to create a calculator that can perform at least 5 different mathematical operations such as addition, subtraction, multiplication, division and average. Ensure that the program is user friendly, prompting for input and displaying the results

def sum_2_num(num1, num2):
    result1 = num1 + num2
    return result1
def sub_2_num(num1, num2):
    result2 = num1 - num2
    return result2
def mul_2_num(num1, num2):
    result3 = num1 * num2
    return result3
def div_2_num(num1, num2):
    result4 = num1 / num2
    return result4
def avg_2_num(num1, num2):
    result5 = (num1 + num2)/2
    return result5

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

print("Enter your operator : ")
operator = input()

if operator == "+":
    print("Sum of the numbers is: ", sum_2_num(num1, num2))
elif operator == "-":
    print("Subtraction of the numbers is: ", sub_2_num(num1, num2))
elif operator == "*":
    print("Multiplication of the numbers is: ", mul_2_num(num1, num2))
elif operator == "/":
    print("Division of the numbers is: ", div_2_num(num1, num2))
elif operator == "avg":
    print("Average of the numbers is: ", avg_2_num(num1, num2))
else:
    print("Invalid operator!")