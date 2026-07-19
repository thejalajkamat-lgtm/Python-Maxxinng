#Nesting means ek sentence ke andar dusre sentence ko lena and it is completely valid in Python
age = float(input("Enter the age:"))
print("The age is: ", age)

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

#If age>15 can ride scooter, if age>18 can drive car, if age>50 cannot drive car, if age>60 cannot ride scooter
age = float(input("Enter the age:"))
print("The age is: ", age)

if(age > 60):
    print("You cannot ride a scoter")
    print("You cannot drive a car")

elif(age > 50):
     print("You can ride a scoter")
     print("You cannot ride a car")

elif(age > 18):
     print("You can ride a scoter")
     print("You can ride a car")

elif(age > 15):
     print("You can ride a scoter")
     print("You cannot drive a car")

else:
     print("You can neither ride a scooter nor drive a car.")
     

