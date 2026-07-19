#CONDITIONAL EXPRESSIONS 
#SYNTAX = value_if_true if condition else value_if_false

age = 16
status = "Adult" if age >= 18 else "Minor"
print(status)
print("\n")



year = int(input("Enter your year: "))
print("The year is : ", year)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("It is a leap year") 
else:
       print("It is not a leap year")