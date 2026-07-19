"""   if-elif-else (SYNTAX)
    
    if(condition):
        Statement1
    elif(condition):
        Statement2
    else:
        StatementN   """

age = int(input("Enter your age: "))
print("Your age is :", age)

if (age >= 18) :
    print("Can Vote & apply for License")
else:
 print("Cannot Vote & cannot apply for License")
 print("\n")

 #use elif as well
light = str(input("Enter the color of the traffic light:"))
print("The color of the traffic light is ", light)

if (light=="red"):
    print("STOP!!")
elif(light=="yellow"):
    print("LOOK!!")
elif(light == "green"):
    print("GO!!")
else :
    print("Invalid colour")