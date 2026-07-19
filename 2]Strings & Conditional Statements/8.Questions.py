#Check if no is odd or even
num = int(input("Enter the number:"))
print("The number is: ", num)

rem = num % 2

if(rem == 0):
    print("The number is even")
else:
    print("The number is odd")

#Check the greatest of 3 numbers
num1= int(input("Enter num1:"))
num2= int(input("Enter num2:"))
num3= int(input("Enter num3:"))

if(num1 > num2 and num1 > num3):
    print(num1, " is the greatest number")
elif(num2> num1 and num2 > num3):
    print(num2, " is the greatest number")
else:
    print(num3," is the greatest number")