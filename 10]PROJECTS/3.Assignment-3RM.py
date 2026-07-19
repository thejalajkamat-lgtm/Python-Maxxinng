#Q1]LEAP YEAR: Write a simple program to determne if the year is a leap year or not using user input
# Note:
#Leap Year occurs once every 4 year
#A year is a leap year if it is divisible by 4, but not if it is divisible by 100 unless it is also divisible by 400
# year = int(input("Enter your year: "))
# print("The year is : ", year)

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("It is a leap year") 
# else:
#        print("It is not a leap year")


#Q2]LOGIN AUTHENTICATION using conditional statement. Assume you have a predefined username and password.
#Write a program that prompts the user to enter a username and password and checks whether they match. Provide appropriate messages for the following cases:1)Both username and password are correct    2)USername is correct but password is incorrect      3)Username is incorrect

name = input("Enter your username: ")
password = input("Enter your password: ")
if name == 'Jalaj'or'jalaj' and password =='karlmarn69palantir':
        print("Correct username and password")
elif name != 'Jalaj'or'jalaj' and password=='karlmarn69palantir':
        print("Incorrect username")
elif name == 'Jalaj'or'jalaj' and password!='karlmarn69palantir':
        print("password is incorrect")
else:
        print("Invalid password and name")

