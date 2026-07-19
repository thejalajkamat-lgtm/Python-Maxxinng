""" J A L A J - K A M A T 
    0 1 2 3 4 5 6 7 8 9 10

str = "JALAJ-KAMAT"
str[0] is 'J', str[1] is 'A'
str[0] = 'B' is not allowed    """

str = "Jalaj Kamat"
ch = str[1] #empty space (here str[5]) cannot be replaced
print(ch)
print("\n")

#SLICING
str1 = "Jalaj Nitin Kamat"
print(str1[1:5]) #str[1:4] means str1,2,3 will be printed together
print(str1[1:])  #[1:last str]
print(str1[1:len(str1)]) #[1:last str]
print(str1[:5]) 
print("\n")

""" A  P  P  L  E 
   -5 -4 -3 -2 -1 This is called as -ve Slicing """
str2 = "APPLE"
print(str2[-3:-1])