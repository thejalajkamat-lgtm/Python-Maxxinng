#find the largest of 4 numbers

num1= int(input("Enter num1:"))
num2= int(input("Enter num2:"))
num3= int(input("Enter num3:"))
num4= int(input("Enter num4:"))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print(num1, " is the greatest number")
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print(num2, " is the greatest number")
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print(num3, " is the greatest number")
else:
    print(num4, " is the greatest number")

