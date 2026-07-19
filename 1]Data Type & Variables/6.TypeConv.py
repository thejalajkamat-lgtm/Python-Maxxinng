""" Type Conversion means changing automatically
Type Casting means changinng manually """

#type conversion
a = 2
b = 4.25
print(a + b) #here 2 is considered as 2.0 i.e a float value and the answer is also a float value. This is called as type conversion


#type casting
c = int("2")  #this is now an int not a string
"""c = int("Jalaj") is ofcourse an error aka it can't be type casted"""
d = 4.25
print("c+d is ", c+d, type(c+d))

e = 3.14
e = str(e)
print("e is ", e,type(e))